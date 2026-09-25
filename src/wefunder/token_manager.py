"""Holds the live token state and owns token recovery + persistence.

Two recovery strategies, picked automatically:

* **refresh_token** (user flows): rotates — every refresh returns a NEW refresh token,
  persisted BEFORE the retried request can use it (the critical invariant).
* **re-mint** (client_credentials): cc tokens have NO refresh token, but a client built via
  ``Wefunder.from_client_credentials`` holds the grant inputs, so it mints a fresh token on
  expiry/401 instead of raising.

Either way, concurrent callers coalesce: a burst of 401s performs ONE recovery. The
transport passes the token it just used; if the manager already holds a different token,
another caller recovered in the meantime and the current token is returned without a
round-trip (no rotation race, no thundering herd).
"""

from __future__ import annotations

import asyncio
import inspect
import threading
import time
from collections.abc import Awaitable, Callable
from typing import Any, Protocol

from .errors import WefunderAuthError
from .oauth import Now, TokenSet, async_refresh_token, refresh_token, resolve_token_base

DEFAULT_EXPIRY_LEEWAY_SECONDS = 30.0


class TokenStore(Protocol):
    """Pluggable persistence for the rotating token set (DB row, secrets manager, …).
    ``save`` may be sync or async."""

    def save(self, tokens: TokenSet) -> Any: ...


async def _maybe_await(value: Any) -> Any:
    if inspect.isawaitable(value):
        return await value
    return value


class _TokenManagerBase:
    def __init__(
        self,
        tokens: TokenSet,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        on_token_refresh: Callable[[TokenSet], Any] | None = None,
        store: TokenStore | None = None,
        now: Now | None = None,
        expiry_leeway_seconds: float = DEFAULT_EXPIRY_LEEWAY_SECONDS,
        token_base_url: str | None = None,
        oauth_base_url: str | None = None,
    ) -> None:
        self._tokens = tokens
        self._client_id = client_id
        self._client_secret = client_secret
        self._on_token_refresh = on_token_refresh
        self._store = store
        self._now = now or time.time
        self._leeway = expiry_leeway_seconds
        self._token_base_url = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)

    @property
    def current(self) -> TokenSet:
        return self._tokens

    def _can_rotate(self) -> bool:
        return bool(self._tokens.refresh_token and self._client_id)

    def _near_expiry(self) -> bool:
        exp = self._tokens.expires_at
        return exp is not None and self._now() >= exp - self._leeway

    def _keep_refresh_token(self, nxt: TokenSet, previous: str | None) -> TokenSet:
        # Some servers omit a fresh refresh_token on rotation-disabled flows; keep the
        # previous one rather than dropping our ability to refresh.
        if not nxt.refresh_token:
            nxt.refresh_token = previous
        return nxt

    def _no_recovery(self) -> WefunderAuthError:
        return WefunderAuthError("Access token expired and no refresh token / re-mint capability is configured.")


class TokenManager(_TokenManagerBase):
    """Thread-safe (sync) token manager."""

    def __init__(
        self,
        tokens: TokenSet,
        *,
        re_mint: Callable[[], TokenSet] | None = None,
        transport: Any = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(tokens, **kwargs)
        self._re_mint = re_mint
        self._transport = transport
        self._lock = threading.Lock()

    @property
    def can_refresh(self) -> bool:
        """True if an expired token can be recovered (rotate a refresh token or re-mint)."""
        return self._can_rotate() or self._re_mint is not None

    def get_access_token(self) -> str:
        """A valid access token, refreshing proactively if expired / within the leeway."""
        if self._near_expiry() and self.can_refresh:
            self.refresh(stale_token=self._tokens.access_token)
        return self._tokens.access_token

    def refresh(self, *, stale_token: str | None = None) -> TokenSet:
        """Recover the token (after a 401 or proactively). Coalesces concurrent callers:
        if ``stale_token`` is no longer the current token, someone else already recovered
        and the current set is returned without a network round-trip."""
        with self._lock:
            if stale_token is not None and self._tokens.access_token != stale_token:
                return self._tokens
            previous_refresh = self._tokens.refresh_token
            if self._can_rotate():
                nxt = refresh_token(
                    client_id=self._client_id or "",
                    client_secret=self._client_secret,
                    refresh_token=previous_refresh or "",
                    token_base_url=self._token_base_url,
                    transport=self._transport,
                    now=self._now,
                )
                nxt = self._keep_refresh_token(nxt, previous_refresh)
            elif self._re_mint is not None:
                nxt = self._re_mint()
            else:
                raise self._no_recovery()
            self._tokens = nxt
            if self._store is not None:
                self._store.save(nxt)
            if self._on_token_refresh is not None:
                self._on_token_refresh(nxt)
            return nxt


class AsyncTokenManager(_TokenManagerBase):
    """asyncio token manager. ``re_mint``, ``store.save`` and ``on_token_refresh`` may be
    coroutine functions or plain callables."""

    def __init__(
        self,
        tokens: TokenSet,
        *,
        re_mint: Callable[[], Awaitable[TokenSet] | TokenSet] | None = None,
        transport: Any = None,
        **kwargs: Any,
    ) -> None:
        super().__init__(tokens, **kwargs)
        self._re_mint = re_mint
        self._transport = transport
        self._lock: asyncio.Lock | None = None

    def _get_lock(self) -> asyncio.Lock:
        # Created lazily so the manager can be built outside a running loop.
        if self._lock is None:
            self._lock = asyncio.Lock()
        return self._lock

    @property
    def can_refresh(self) -> bool:
        return self._can_rotate() or self._re_mint is not None

    async def get_access_token(self) -> str:
        if self._near_expiry() and self.can_refresh:
            await self.refresh(stale_token=self._tokens.access_token)
        return self._tokens.access_token

    async def refresh(self, *, stale_token: str | None = None) -> TokenSet:
        async with self._get_lock():
            if stale_token is not None and self._tokens.access_token != stale_token:
                return self._tokens
            previous_refresh = self._tokens.refresh_token
            if self._can_rotate():
                nxt = await async_refresh_token(
                    client_id=self._client_id or "",
                    client_secret=self._client_secret,
                    refresh_token=previous_refresh or "",
                    token_base_url=self._token_base_url,
                    transport=self._transport,
                    now=self._now,
                )
                nxt = self._keep_refresh_token(nxt, previous_refresh)
            elif self._re_mint is not None:
                nxt = await _maybe_await(self._re_mint())
            else:
                raise self._no_recovery()
            self._tokens = nxt
            if self._store is not None:
                await _maybe_await(self._store.save(nxt))
            if self._on_token_refresh is not None:
                await _maybe_await(self._on_token_refresh(nxt))
            return nxt
