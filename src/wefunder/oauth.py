"""OAuth 2.0 helpers: authorization_code + PKCE (user flows) and client_credentials
(server-to-server, ``read:public``). Refresh tokens ROTATE — every refresh returns a NEW
refresh token that must be persisted (the client / TokenManager does this for you).

HOST SPLIT — ``/authorize`` and ``/token`` live on different hosts by purpose:

* ``/token`` (+ refresh) is on the API gateway. The edge routes test/live by the
  credential's mode (form-body ``client_id``), so ONE token host serves both modes; never
  route by prefix here.
* ``/authorize`` is the browser consent redirect. Live consent is on ``wefunder.com``;
  sandbox (``pk_test_``) consent is on ``oauth.wefunder-sandbox.com``.
  :func:`create_authorization_url` picks by ``client_id`` prefix.

All hosts remain independently overridable (``authorize_base_url`` / ``token_base_url``;
``oauth_base_url`` sets both). Precedence: specific > alias > default.
"""

from __future__ import annotations

import base64
import hashlib
import secrets
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any
from urllib.parse import urlencode

import httpx

#: Host for the LIVE browser ``/authorize`` redirect (``pk_live_`` / default).
DEFAULT_AUTHORIZE_BASE_URL = "https://wefunder.com/oauth"
#: Host for the SANDBOX browser ``/authorize`` redirect (``pk_test_``). Canonical, client_id-derivable.
SANDBOX_AUTHORIZE_BASE_URL = "https://oauth.wefunder-sandbox.com/oauth"
#: Host for ``/token`` (+ refresh). The gateway routes test/live by the client_id mode.
DEFAULT_TOKEN_BASE_URL = "https://api.wefunder.com/oauth"

SANDBOX_CLIENT_ID_PREFIX = "pk_test_"

Now = Callable[[], float]  # unix seconds


def resolve_token_base(*, token_base_url: str | None = None, oauth_base_url: str | None = None, **_: Any) -> str:
    return token_base_url or oauth_base_url or DEFAULT_TOKEN_BASE_URL


def default_authorize_base(client_id: str) -> str:
    """Sandbox consent host for ``pk_test_`` client ids, live otherwise."""
    return SANDBOX_AUTHORIZE_BASE_URL if client_id.startswith(SANDBOX_CLIENT_ID_PREFIX) else DEFAULT_AUTHORIZE_BASE_URL


@dataclass(slots=True)
class TokenSet:
    access_token: str
    refresh_token: str | None = None
    #: Unix seconds at which the access token expires (if the server said).
    expires_at: float | None = None
    scope: str | None = None
    token_type: str | None = None

    @classmethod
    def from_token_response(cls, raw: Mapping[str, Any], now: float) -> TokenSet:
        expires_in = raw.get("expires_in")
        return cls(
            access_token=str(raw["access_token"]),
            refresh_token=raw.get("refresh_token"),
            expires_at=(now + float(expires_in)) if expires_in else None,
            scope=raw.get("scope"),
            token_type=raw.get("token_type"),
        )


class OAuthTokenError(Exception):
    """The token endpoint answered non-2xx."""

    def __init__(self, status: int, body: str) -> None:
        super().__init__(f"OAuth token request failed ({status}): {body}")
        self.status = status
        self.body = body


# ---- PKCE (authorization_code) --------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Pkce:
    code_verifier: str
    code_challenge: str
    code_challenge_method: str = "S256"


def _b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode("ascii")


def pkce_challenge(code_verifier: str) -> str:
    """RFC 7636 S256: ``base64url(sha256(ascii(verifier)))`` without padding."""
    return _b64url(hashlib.sha256(code_verifier.encode("ascii")).digest())


def generate_pkce() -> Pkce:
    """A fresh PKCE verifier/challenge pair (RFC 7636, S256)."""
    verifier = _b64url(secrets.token_bytes(32))
    return Pkce(code_verifier=verifier, code_challenge=pkce_challenge(verifier))


def create_authorization_url(
    *,
    client_id: str,
    redirect_uri: str,
    scopes: list[str] | tuple[str, ...],
    state: str,
    pkce: Pkce | None = None,
    code_challenge: str | None = None,
    authorize_base_url: str | None = None,
    oauth_base_url: str | None = None,
    token_base_url: str | None = None,  # accepted for symmetry; never affects /authorize
) -> str:
    """The URL to redirect a user to for the authorization_code + PKCE flow.

    ``state`` is an opaque CSRF token you generate and verify on the callback. Pass the
    :class:`Pkce` you generated (or just its ``code_challenge``) and keep the verifier in
    the user's session for :func:`exchange_code`.
    """
    del token_base_url
    challenge = code_challenge or (pkce.code_challenge if pkce else None)
    if not challenge:
        raise ValueError("create_authorization_url: provide `pkce` or `code_challenge`")
    base = authorize_base_url or oauth_base_url or default_authorize_base(client_id)
    query = urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": " ".join(scopes),
            "state": state,
            "code_challenge": challenge,
            "code_challenge_method": "S256",
        }
    )
    return f"{base}/authorize?{query}"


# ---- token endpoint -------------------------------------------------------------------


def _token_request(base: str, params: Mapping[str, str]) -> tuple[str, dict[str, str], dict[str, str]]:
    return (f"{base}/token", {"Content-Type": "application/x-www-form-urlencoded"}, dict(params))


def _parse_token_response(response: httpx.Response, now: float) -> TokenSet:
    if response.status_code < 200 or response.status_code >= 300:
        raise OAuthTokenError(response.status_code, response.text)
    return TokenSet.from_token_response(response.json(), now)


def _post_token(
    base: str,
    params: Mapping[str, str],
    transport: httpx.BaseTransport | None,
    now: Now | None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    url, headers, data = _token_request(base, params)
    with httpx.Client(transport=transport, timeout=timeout) as http:
        response = http.post(url, headers=headers, data=data)
    return _parse_token_response(response, (now or time.time)())


async def _apost_token(
    base: str,
    params: Mapping[str, str],
    transport: httpx.AsyncBaseTransport | None,
    now: Now | None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    url, headers, data = _token_request(base, params)
    async with httpx.AsyncClient(transport=transport, timeout=timeout) as http:
        response = await http.post(url, headers=headers, data=data)
    return _parse_token_response(response, (now or time.time)())


def _exchange_params(
    client_id: str, client_secret: str | None, code: str, redirect_uri: str, code_verifier: str
) -> dict[str, str]:
    params = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "code": code,
        "redirect_uri": redirect_uri,
        "code_verifier": code_verifier,
    }
    if client_secret:
        params["client_secret"] = client_secret
    return params


def _cc_params(client_id: str, client_secret: str, scopes: list[str] | tuple[str, ...] | None) -> dict[str, str]:
    params = {"grant_type": "client_credentials", "client_id": client_id, "client_secret": client_secret}
    if scopes:
        params["scope"] = " ".join(scopes)
    return params


def _refresh_params(client_id: str, client_secret: str | None, refresh_token: str) -> dict[str, str]:
    params = {"grant_type": "refresh_token", "client_id": client_id, "refresh_token": refresh_token}
    if client_secret:
        params["client_secret"] = client_secret
    return params


def exchange_code(
    *,
    client_id: str,
    code: str,
    redirect_uri: str,
    code_verifier: str,
    client_secret: str | None = None,
    token_base_url: str | None = None,
    oauth_base_url: str | None = None,
    transport: httpx.BaseTransport | None = None,
    now: Now | None = None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    """Exchange an authorization code (+ PKCE verifier) for a token set. Public (PKCE)
    clients omit ``client_secret``; confidential clients pass it."""
    base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
    return _post_token(
        base, _exchange_params(client_id, client_secret, code, redirect_uri, code_verifier), transport, now, timeout
    )


def client_credentials_grant(
    *,
    client_id: str,
    client_secret: str,
    scopes: list[str] | tuple[str, ...] | None = None,
    token_base_url: str | None = None,
    oauth_base_url: str | None = None,
    transport: httpx.BaseTransport | None = None,
    now: Now | None = None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    """Mint an application token (server-to-server). cc tokens carry no refresh token."""
    base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
    return _post_token(base, _cc_params(client_id, client_secret, scopes), transport, now, timeout)


def refresh_token(
    *,
    client_id: str,
    refresh_token: str,
    client_secret: str | None = None,
    token_base_url: str | None = None,
    oauth_base_url: str | None = None,
    transport: httpx.BaseTransport | None = None,
    now: Now | None = None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    """Refresh an access token. CRITICAL: the result carries a NEW refresh token
    (rotation) — persist it. Reusing the old one after rotation is a permanent 401."""
    base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
    return _post_token(base, _refresh_params(client_id, client_secret, refresh_token), transport, now, timeout)


async def async_exchange_code(
    *,
    client_id: str,
    code: str,
    redirect_uri: str,
    code_verifier: str,
    client_secret: str | None = None,
    token_base_url: str | None = None,
    oauth_base_url: str | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
    now: Now | None = None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    """Async :func:`exchange_code`."""
    base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
    return await _apost_token(
        base, _exchange_params(client_id, client_secret, code, redirect_uri, code_verifier), transport, now, timeout
    )


async def async_client_credentials_grant(
    *,
    client_id: str,
    client_secret: str,
    scopes: list[str] | tuple[str, ...] | None = None,
    token_base_url: str | None = None,
    oauth_base_url: str | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
    now: Now | None = None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    """Async :func:`client_credentials_grant`."""
    base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
    return await _apost_token(base, _cc_params(client_id, client_secret, scopes), transport, now, timeout)


async def async_refresh_token(
    *,
    client_id: str,
    refresh_token: str,
    client_secret: str | None = None,
    token_base_url: str | None = None,
    oauth_base_url: str | None = None,
    transport: httpx.AsyncBaseTransport | None = None,
    now: Now | None = None,
    timeout: httpx.Timeout | float | None = 30.0,
) -> TokenSet:
    """Async :func:`refresh_token`."""
    base = resolve_token_base(token_base_url=token_base_url, oauth_base_url=oauth_base_url)
    return await _apost_token(base, _refresh_params(client_id, client_secret, refresh_token), transport, now, timeout)
