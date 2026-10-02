"""The Wefunder client — the stable, hand-written surface over the generated layer.

Wires: a single API base (the edge gateway routes live/sandbox by token mode, so the SDK
never routes by prefix), a pinned ``Wefunder-Version``, the retry/refresh transport, token
rotation, typed-error unwrapping, and lazy auto-pagination. Resource namespaces cover the
common paths; ``raw`` exposes every generated operation as an escape hatch.
"""

from __future__ import annotations

import datetime
import enum
import json
import typing
from collections.abc import AsyncIterator, Callable, Iterator, Mapping
from typing import Any, Literal

import httpx

from ._generated.api.attribution_partners import get_attribution_me
from ._generated.api.campaigns import list_campaigns
from ._generated.api.explore import get_offering, list_offerings
from ._generated.api.intents import create_intent, get_intent, list_intents, preview_intent
from ._generated.api.investments import get_investment, get_offering_stats, list_investments
from ._generated.api.portfolio import get_portfolio, list_portfolio_positions
from ._generated.api.syndicate_portfolio import get_syndicate_portfolio, list_syndicate_portfolio_positions
from ._generated.api.syndicates import get_syndicate, list_syndicates
from ._generated.api.users import get_current_user
from ._generated.api.webhook_endpoints import (
    create_webhook_endpoint,
    delete_webhook_endpoint,
    get_webhook_endpoint,
    list_webhook_endpoints,
    reenable_webhook_endpoint,
    rotate_webhook_endpoint_secret,
    test_webhook_endpoint,
    update_webhook_endpoint,
)
from ._generated.client import AuthenticatedClient
from ._generated.models.create_webhook_endpoint_body import CreateWebhookEndpointBody
from ._generated.models.test_webhook_endpoint_body import TestWebhookEndpointBody
from ._generated.models.update_webhook_endpoint_body import UpdateWebhookEndpointBody
from ._generated.types import UNSET, Response, Unset
from ._retry import AsyncRetryTransport, RetryOptions, RetryTransport
from .errors import WefunderError, error_from_httpx, error_from_response
from .oauth import (
    Now,
    TokenSet,
    async_client_credentials_grant,
    client_credentials_grant,
    resolve_token_base,
)
from .pagination import Cursor, acollect, apaginate, collect, paginate
from .token_manager import AsyncTokenManager, TokenManager, TokenStore

# Version-free base — the edge gateway serves the API at the host root; ``/api/v2`` remains
# a working back-compat alias. The API version is pinned via the ``Wefunder-Version``
# header, not the path.
DEFAULT_API_BASE_URL = "https://api.wefunder.com"
DEFAULT_API_VERSION = "2025-01-15"
API_VERSION_HEADER = "Wefunder-Version"

Mode = Literal["live", "test", "unknown"]


def mode_for_token(token: str) -> Mode:
    """``live`` / ``test`` from the access-token prefix. UX only — never used for routing."""
    if token.startswith("at_live_"):
        return "live"
    if token.startswith("at_test_"):
        return "test"
    return "unknown"


# ---- shared helpers -----------------------------------------------------------------------


def _coerce_kwargs(fn: Callable[..., Any], kwargs: dict[str, Any]) -> dict[str, Any]:
    """Let callers pass plain values for typed query params: strings for enums
    (``sort="newest"``) and ISO-8601 strings for ``datetime``/``date`` params."""
    try:
        hints = typing.get_type_hints(fn)
    except Exception:  # pragma: no cover - defensive; generated code always resolves
        return kwargs
    out = dict(kwargs)
    for name, value in kwargs.items():
        hint = hints.get(name)
        if hint is None or not isinstance(value, str):
            continue
        for candidate in typing.get_args(hint) or (hint,):
            if not isinstance(candidate, type):
                continue
            if issubclass(candidate, enum.Enum):
                out[name] = candidate(value)
                break
            if candidate is datetime.datetime:
                out[name] = datetime.datetime.fromisoformat(value.replace("Z", "+00:00"))
                break
            if candidate is datetime.date:
                out[name] = datetime.date.fromisoformat(value)
                break
    return out


def _data_of(envelope: Any) -> Any:
    """Single-resource envelopes are ``{data: Entity}``; return the entity for ergonomics."""
    if isinstance(envelope, Mapping):
        return envelope.get("data")
    data = getattr(envelope, "data", UNSET)
    return None if isinstance(data, Unset) else data


def _unwrap(response: Response[Any]) -> Any:
    """Return ``parsed`` on success; raise :class:`WefunderError` on any 4xx/5xx.

    A 2xx the spec doesn't document (so the generated parser returns ``None``) falls back
    to the decoded JSON body rather than silently yielding ``None``."""
    if response.status_code >= 400:
        raise error_from_response(int(response.status_code), response.headers, response.content)
    if response.parsed is None and response.content:
        try:
            return json.loads(response.content)
        except ValueError:
            return None
    return response.parsed


def _webhook_body(url: str, events: list[str], mode: str | None) -> CreateWebhookEndpointBody:
    return CreateWebhookEndpointBody.from_dict({"url": url, "events": list(events), **({"mode": mode} if mode else {})})


class _Base:
    """Construction shared by the sync and async clients."""

    def __init__(
        self,
        *,
        access_token: str | None,
        tokens: TokenSet | None,
        api_version: str,
        base_url: str,
    ) -> None:
        token_set = tokens or (TokenSet(access_token=access_token) if access_token else None)
        if token_set is None:
            raise ValueError("Wefunder: provide `access_token` or `tokens`.")
        self._initial_tokens = token_set
        self.mode: Mode = mode_for_token(token_set.access_token)
        self._api_version = api_version
        self._base_url = base_url.rstrip("/")

    def _generated_client(self) -> AuthenticatedClient:
        # The transport owns the Authorization header (it reads the managed token per
        # attempt), so the generated client's own token is a placeholder.
        # attrs `alias=` fields (base_url/headers) are invisible to pyright's attrs plugin.
        return AuthenticatedClient(  # pyright: ignore[reportCallIssue]
            base_url=self._base_url, token="managed", headers={API_VERSION_HEADER: self._api_version}
        )


# ---- sync client ------------------------------------------------------------------------------


class Wefunder(_Base):
    """Synchronous client. Construct with ``access_token=`` (no auto-refresh), ``tokens=`` +
    ``client_id`` (auto-refresh with rotation), or :meth:`from_client_credentials`."""

    def __init__(
        self,
        *,
        access_token: str | None = None,
        tokens: TokenSet | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        client_credentials: Mapping[str, Any] | None = None,
        api_version: str = DEFAULT_API_VERSION,
        base_url: str = DEFAULT_API_BASE_URL,
        authorize_base_url: str | None = None,
        token_base_url: str | None = None,
        oauth_base_url: str | None = None,
        store: TokenStore | None = None,
        on_token_refresh: Callable[[TokenSet], Any] | None = None,
        retry: RetryOptions | None = None,
        timeout: httpx.Timeout | float | None = 30.0,
        transport: httpx.BaseTransport | None = None,
        now: Now | None = None,
        sleep: Callable[[float], Any] | None = None,
        random: Callable[[], float] | None = None,
    ) -> None:
        super().__init__(access_token=access_token, tokens=tokens, api_version=api_version, base_url=base_url)
        del authorize_base_url  # only /authorize uses it; see oauth.create_authorization_url
        token_base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
        inner = transport or httpx.HTTPTransport()

        re_mint: Callable[[], TokenSet] | None = None
        if client_credentials is not None and client_id and client_secret:
            scopes = client_credentials.get("scopes")
            re_mint = lambda: client_credentials_grant(  # noqa: E731
                client_id=client_id,
                client_secret=client_secret,
                scopes=scopes,
                token_base_url=token_base,
                transport=transport,
                now=now,
            )
        self._tm = TokenManager(
            self._initial_tokens,
            client_id=client_id,
            client_secret=client_secret,
            re_mint=re_mint,
            on_token_refresh=on_token_refresh,
            store=store,
            transport=transport,
            now=now,
            token_base_url=token_base,
        )
        now_ms = (lambda: now() * 1000) if now else None
        self._http = httpx.Client(
            base_url=self._base_url,
            headers={API_VERSION_HEADER: api_version},
            timeout=timeout,
            transport=RetryTransport(
                inner, token_manager=self._tm, retry=retry, sleep=sleep, now_ms=now_ms, random=random
            ),
        )
        self._gen = self._generated_client().set_httpx_client(self._http)

        self.users = _Users(self)
        self.offerings = _Offerings(self)
        self.investments = _Investments(self)
        self.portfolio = _Portfolio(self)
        self.campaigns = _Campaigns(self)
        self.syndicates = _Syndicates(self)
        self.intents = _Intents(self)
        self.attribution = _Attribution(self)
        self.webhook_endpoints = _WebhookEndpoints(self)

    @classmethod
    def from_client_credentials(
        cls,
        *,
        client_id: str,
        client_secret: str,
        scopes: list[str] | tuple[str, ...] | None = None,
        **kwargs: Any,
    ) -> Wefunder:
        """Mint an application token now and auto-re-mint on expiry/401 (cc tokens have no
        refresh token). Extra ``kwargs`` are forwarded to the constructor."""
        tokens = client_credentials_grant(
            client_id=client_id,
            client_secret=client_secret,
            scopes=scopes,
            token_base_url=kwargs.get("token_base_url"),
            oauth_base_url=kwargs.get("oauth_base_url"),
            transport=kwargs.get("transport"),
            now=kwargs.get("now"),
            timeout=kwargs.get("timeout", 30.0),
        )
        return cls(
            tokens=tokens,
            client_id=client_id,
            client_secret=client_secret,
            client_credentials={"scopes": scopes},
            **kwargs,
        )

    # -- plumbing ------------------------------------------------------------------------------

    @property
    def tokens(self) -> TokenSet:
        """The current token set (rotated refresh token included)."""
        return self._tm.current

    @property
    def token_manager(self) -> TokenManager:
        """The :class:`TokenManager` (for ``mark_persisted()`` after a :class:`WefunderTokenPersistenceError`)."""
        return self._tm

    @property
    def raw(self) -> AuthenticatedClient:
        """The generated client, for any operation without a namespace::

        from wefunder._generated.api.syndicate_members import list_syndicate_members
        page = wf.unwrap(list_syndicate_members.sync_detailed(client=wf.raw, syndicate_id="syn_…"))
        """
        return self._gen

    def unwrap(self, response: Response[Any]) -> Any:
        """Apply the namespaces' error handling to a raw generated ``Response``."""
        return _unwrap(response)

    def call(self, op: Any, /, **kwargs: Any) -> Any:
        """``wf.unwrap(op.sync_detailed(client=wf.raw, **kwargs))`` with string→enum coercion."""
        fn = op.sync_detailed
        return _unwrap(fn(client=self._gen, **_coerce_kwargs(fn, kwargs)))

    def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """Escape hatch for any path (preview ops, brand-new endpoints): full envelope —
        auth + recovery, ``Wefunder-Version``, retries, typed errors. Returns parsed JSON
        (``None`` for an empty body). ``body`` is sent as JSON unless it is bytes/str."""
        kwargs: dict[str, Any] = {
            "params": {k: v for k, v in (query or {}).items() if v is not None},
            "headers": dict(headers or {}),
        }
        if body is not None:
            if isinstance(body, (bytes, str)):
                kwargs["content"] = body
            else:
                kwargs["json"] = body
        response = self._http.request(method.upper(), path, **kwargs)
        if response.status_code >= 400:
            raise error_from_httpx(response)
        return response.json() if response.content else None

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> Wefunder:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()


class _Namespace:
    def __init__(self, wf: Wefunder) -> None:
        self._wf = wf


class _Users(_Namespace):
    def me(self) -> Any:
        """``GET /users/me`` (needs ``read:profile``; a client_credentials token gets 403)."""
        return _data_of(self._wf.call(get_current_user))


class _Offerings(_Namespace):
    def list(self, **query: Any) -> Any:
        """One page of ``GET /explore`` (``sort``, ``cursor``, filters). Returns the envelope."""
        return self._wf.call(list_offerings, **query)

    def all(self, **query: Any) -> Iterator[Any]:
        """Every offering, lazily, ``query`` preserved across pages."""
        return paginate(lambda cursor: self.list(**query, **({"cursor": cursor} if cursor is not None else {})))

    def get(self, offering_id: str) -> Any:
        return _data_of(self._wf.call(get_offering, external_id=offering_id))

    def stats(self, offering_id: str) -> Any:
        return _data_of(self._wf.call(get_offering_stats, offering_id=offering_id))


class _Investments(_Namespace):
    """The Investment Delta API. ``list()`` without a cursor bootstraps; ``next_cursor`` is
    always present (persist it after every sync) and ``has_more`` terminates."""

    def list(self, **query: Any) -> Any:
        return self._wf.call(list_investments, **query)

    def all(self, **query: Any) -> Iterator[Any]:
        return paginate(lambda cursor: self.list(**query, **({"cursor": cursor} if cursor is not None else {})))

    def collect(self, **query: Any) -> list[Any]:
        return list(self.all(**query))

    def get(self, investment_id: str) -> Any:
        return _data_of(self._wf.call(get_investment, id=investment_id))


class _PortfolioPositions(_Namespace):
    def list(self, **query: Any) -> Any:
        return self._wf.call(list_portfolio_positions, **query)

    def all(self, **query: Any) -> Iterator[Any]:
        return paginate(lambda cursor: self.list(**query, **({"cursor": cursor} if cursor is not None else {})))


class _Portfolio(_Namespace):
    def __init__(self, wf: Wefunder) -> None:
        super().__init__(wf)
        self.positions = _PortfolioPositions(wf)

    def get(self, **query: Any) -> Any:
        """The portfolio summary (``status``, ``company`` filters)."""
        return _data_of(self._wf.call(get_portfolio, **query))


class _Campaigns(_Namespace):
    def list(self, **query: Any) -> Any:
        return self._wf.call(list_campaigns, **query)

    def all(self, **query: Any) -> Iterator[Any]:
        return paginate(lambda cursor: self.list(**query, **({"cursor": cursor} if cursor is not None else {})))


class _Syndicates(_Namespace):
    def list(self, **query: Any) -> Any:
        return self._wf.call(list_syndicates, **query)

    def all(self, **query: Any) -> Iterator[Any]:
        return paginate(lambda cursor: self.list(**query, **({"cursor": cursor} if cursor is not None else {})))

    def get(self, syndicate_id: str) -> Any:
        return _data_of(self._wf.call(get_syndicate, syndicate_id=syndicate_id))

    def portfolio(self, syndicate_id: str, **query: Any) -> Any:
        return _data_of(self._wf.call(get_syndicate_portfolio, syndicate_id=syndicate_id, **query))

    def portfolio_positions(self, syndicate_id: str, **query: Any) -> Iterator[Any]:
        return paginate(
            lambda cursor: self._wf.call(
                list_syndicate_portfolio_positions,
                syndicate_id=syndicate_id,
                **query,
                **({"cursor": cursor} if cursor is not None else {}),
            )
        )


class _Intents(_Namespace):
    def list(self, **query: Any) -> Any:
        return self._wf.call(list_intents, **query)

    def all(self, **query: Any) -> Iterator[Any]:
        return paginate(lambda cursor: self.list(**query, **({"cursor": cursor} if cursor is not None else {})))

    def get(self, intent_id: str) -> Any:
        return _data_of(self._wf.call(get_intent, intent_id=intent_id))

    def create(self, body: Mapping[str, Any]) -> Any:
        from ._generated.models.create_intent_body import CreateIntentBody

        return _data_of(self._wf.call(create_intent, body=CreateIntentBody.from_dict(dict(body))))

    def preview(self, body: Mapping[str, Any]) -> Any:
        from ._generated.models.preview_intent_body import PreviewIntentBody

        return _data_of(self._wf.call(preview_intent, body=PreviewIntentBody.from_dict(dict(body))))


class _Attribution(_Namespace):
    def me(self) -> Any:
        return _data_of(self._wf.call(get_attribution_me))


class _WebhookEndpoints(_Namespace):
    """Endpoints belong to your application and are managed through the LIVE API
    (``write:webhooks``). The signing secret is returned only on create and rotate."""

    def create(self, *, url: str, events: list[str], mode: str | None = None) -> Any:
        return _data_of(self._wf.call(create_webhook_endpoint, body=_webhook_body(url, events, mode)))

    def list(self) -> Any:
        """The list envelope (``meta.quota`` is the max endpoints per app)."""
        return self._wf.call(list_webhook_endpoints)

    def get(self, endpoint_id: str) -> Any:
        return _data_of(self._wf.call(get_webhook_endpoint, external_id=endpoint_id))

    def update(self, endpoint_id: str, **changes: Any) -> Any:
        """``events`` replaces the list wholesale."""
        body = UpdateWebhookEndpointBody.from_dict(changes)
        return _data_of(self._wf.call(update_webhook_endpoint, external_id=endpoint_id, body=body))

    def remove(self, endpoint_id: str) -> Any:
        return _data_of(self._wf.call(delete_webhook_endpoint, external_id=endpoint_id))

    def rotate_secret(self, endpoint_id: str) -> Any:
        """A new secret; the old one keeps signing for 24h and deliveries carry both ``v1``s."""
        return _data_of(self._wf.call(rotate_webhook_endpoint_secret, external_id=endpoint_id))

    def reenable(self, endpoint_id: str) -> Any:
        return _data_of(self._wf.call(reenable_webhook_endpoint, external_id=endpoint_id))

    def test(self, endpoint_id: str, event: str | None = None) -> Any:
        """Send a real, signed example event to the endpoint and report the outcome."""
        body: TestWebhookEndpointBody | Unset = TestWebhookEndpointBody.from_dict({"event": event}) if event else UNSET
        return _data_of(self._wf.call(test_webhook_endpoint, external_id=endpoint_id, body=body))


# ---- async client -----------------------------------------------------------------------------


class AsyncWefunder(_Base):
    """asyncio client. Same plumbing as :class:`Wefunder` (auth, recovery, retries, typed
    errors, ``raw``/``request``); namespaces cover users, offerings, investments, portfolio,
    and webhook_endpoints — reach the rest through :meth:`call` / :attr:`raw`."""

    def __init__(
        self,
        *,
        access_token: str | None = None,
        tokens: TokenSet | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        client_credentials: Mapping[str, Any] | None = None,
        api_version: str = DEFAULT_API_VERSION,
        base_url: str = DEFAULT_API_BASE_URL,
        authorize_base_url: str | None = None,
        token_base_url: str | None = None,
        oauth_base_url: str | None = None,
        store: TokenStore | None = None,
        on_token_refresh: Callable[[TokenSet], Any] | None = None,
        retry: RetryOptions | None = None,
        timeout: httpx.Timeout | float | None = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
        now: Now | None = None,
        sleep: Callable[[float], Any] | None = None,
        random: Callable[[], float] | None = None,
    ) -> None:
        super().__init__(access_token=access_token, tokens=tokens, api_version=api_version, base_url=base_url)
        del authorize_base_url
        token_base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
        inner = transport or httpx.AsyncHTTPTransport()

        re_mint: Callable[[], Any] | None = None
        if client_credentials is not None and client_id and client_secret:
            scopes = client_credentials.get("scopes")
            re_mint = lambda: async_client_credentials_grant(  # noqa: E731
                client_id=client_id,
                client_secret=client_secret,
                scopes=scopes,
                token_base_url=token_base,
                transport=transport,
                now=now,
            )
        self._tm = AsyncTokenManager(
            self._initial_tokens,
            client_id=client_id,
            client_secret=client_secret,
            re_mint=re_mint,
            on_token_refresh=on_token_refresh,
            store=store,
            transport=transport,
            now=now,
            token_base_url=token_base,
        )
        now_ms = (lambda: now() * 1000) if now else None
        self._http = httpx.AsyncClient(
            base_url=self._base_url,
            headers={API_VERSION_HEADER: api_version},
            timeout=timeout,
            transport=AsyncRetryTransport(
                inner, token_manager=self._tm, retry=retry, sleep=sleep, now_ms=now_ms, random=random
            ),
        )
        self._gen = self._generated_client().set_async_httpx_client(self._http)

        self.users = _AsyncUsers(self)
        self.offerings = _AsyncOfferings(self)
        self.investments = _AsyncInvestments(self)
        self.portfolio = _AsyncPortfolio(self)
        self.webhook_endpoints = _AsyncWebhookEndpoints(self)

    @classmethod
    async def from_client_credentials(
        cls,
        *,
        client_id: str,
        client_secret: str,
        scopes: list[str] | tuple[str, ...] | None = None,
        **kwargs: Any,
    ) -> AsyncWefunder:
        tokens = await async_client_credentials_grant(
            client_id=client_id,
            client_secret=client_secret,
            scopes=scopes,
            token_base_url=kwargs.get("token_base_url"),
            oauth_base_url=kwargs.get("oauth_base_url"),
            transport=kwargs.get("transport"),
            now=kwargs.get("now"),
            timeout=kwargs.get("timeout", 30.0),
        )
        return cls(
            tokens=tokens,
            client_id=client_id,
            client_secret=client_secret,
            client_credentials={"scopes": scopes},
            **kwargs,
        )

    @property
    def tokens(self) -> TokenSet:
        return self._tm.current

    @property
    def raw(self) -> AuthenticatedClient:
        return self._gen

    def unwrap(self, response: Response[Any]) -> Any:
        return _unwrap(response)

    async def call(self, op: Any, /, **kwargs: Any) -> Any:
        fn = op.asyncio_detailed
        return _unwrap(await fn(client=self._gen, **_coerce_kwargs(fn, kwargs)))

    async def request(
        self,
        method: str,
        path: str,
        *,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        kwargs: dict[str, Any] = {
            "params": {k: v for k, v in (query or {}).items() if v is not None},
            "headers": dict(headers or {}),
        }
        if body is not None:
            if isinstance(body, (bytes, str)):
                kwargs["content"] = body
            else:
                kwargs["json"] = body
        response = await self._http.request(method.upper(), path, **kwargs)
        if response.status_code >= 400:
            raise error_from_httpx(response)
        return response.json() if response.content else None

    async def aclose(self) -> None:
        await self._http.aclose()

    async def __aenter__(self) -> AsyncWefunder:
        return self

    async def __aexit__(self, *exc: object) -> None:
        await self.aclose()


class _AsyncNamespace:
    def __init__(self, wf: AsyncWefunder) -> None:
        self._wf = wf

    def _pages(self, op: Any, **query: Any) -> AsyncIterator[Any]:
        async def fetch(cursor: Cursor | None) -> Any:
            return await self._wf.call(op, **query, **({"cursor": cursor} if cursor is not None else {}))

        return apaginate(fetch)


class _AsyncUsers(_AsyncNamespace):
    async def me(self) -> Any:
        return _data_of(await self._wf.call(get_current_user))


class _AsyncOfferings(_AsyncNamespace):
    async def list(self, **query: Any) -> Any:
        return await self._wf.call(list_offerings, **query)

    def all(self, **query: Any) -> AsyncIterator[Any]:
        return self._pages(list_offerings, **query)

    async def get(self, offering_id: str) -> Any:
        return _data_of(await self._wf.call(get_offering, external_id=offering_id))

    async def stats(self, offering_id: str) -> Any:
        return _data_of(await self._wf.call(get_offering_stats, offering_id=offering_id))


class _AsyncInvestments(_AsyncNamespace):
    async def list(self, **query: Any) -> Any:
        return await self._wf.call(list_investments, **query)

    def all(self, **query: Any) -> AsyncIterator[Any]:
        return self._pages(list_investments, **query)

    async def collect(self, **query: Any) -> list[Any]:
        return [item async for item in self.all(**query)]

    async def get(self, investment_id: str) -> Any:
        return _data_of(await self._wf.call(get_investment, id=investment_id))


class _AsyncPortfolioPositions(_AsyncNamespace):
    async def list(self, **query: Any) -> Any:
        return await self._wf.call(list_portfolio_positions, **query)

    def all(self, **query: Any) -> AsyncIterator[Any]:
        return self._pages(list_portfolio_positions, **query)


class _AsyncPortfolio(_AsyncNamespace):
    def __init__(self, wf: AsyncWefunder) -> None:
        super().__init__(wf)
        self.positions = _AsyncPortfolioPositions(wf)

    async def get(self, **query: Any) -> Any:
        return _data_of(await self._wf.call(get_portfolio, **query))


class _AsyncWebhookEndpoints(_AsyncNamespace):
    async def create(self, *, url: str, events: list[str], mode: str | None = None) -> Any:
        return _data_of(await self._wf.call(create_webhook_endpoint, body=_webhook_body(url, events, mode)))

    async def list(self) -> Any:
        return await self._wf.call(list_webhook_endpoints)

    async def get(self, endpoint_id: str) -> Any:
        return _data_of(await self._wf.call(get_webhook_endpoint, external_id=endpoint_id))

    async def update(self, endpoint_id: str, **changes: Any) -> Any:
        body = UpdateWebhookEndpointBody.from_dict(changes)
        return _data_of(await self._wf.call(update_webhook_endpoint, external_id=endpoint_id, body=body))

    async def remove(self, endpoint_id: str) -> Any:
        return _data_of(await self._wf.call(delete_webhook_endpoint, external_id=endpoint_id))

    async def rotate_secret(self, endpoint_id: str) -> Any:
        return _data_of(await self._wf.call(rotate_webhook_endpoint_secret, external_id=endpoint_id))

    async def reenable(self, endpoint_id: str) -> Any:
        return _data_of(await self._wf.call(reenable_webhook_endpoint, external_id=endpoint_id))

    async def test(self, endpoint_id: str, event: str | None = None) -> Any:
        body: TestWebhookEndpointBody | Unset = TestWebhookEndpointBody.from_dict({"event": event}) if event else UNSET
        return _data_of(await self._wf.call(test_webhook_endpoint, external_id=endpoint_id, body=body))


__all__ = [
    "API_VERSION_HEADER",
    "DEFAULT_API_BASE_URL",
    "DEFAULT_API_VERSION",
    "AsyncWefunder",
    "Mode",
    "Wefunder",
    "WefunderError",
    "acollect",
    "collect",
    "mode_for_token",
]
