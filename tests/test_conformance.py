"""Runs the cross-language conformance vectors (conformance/*.json, vendored from
Wefunder/wefunder-node at conformance/PIN) against this SDK. Every Wefunder SDK must pass
every case identically — do NOT "fix" a vector to match the shell; if a case fails, the
shell (or the API contract) changed."""

from __future__ import annotations

import asyncio
import hashlib
import json
import re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest

from wefunder import (
    DEFAULT_API_BASE_URL,
    DEFAULT_API_VERSION,
    DEFAULT_AUTHORIZE_BASE_URL,
    DEFAULT_TOKEN_BASE_URL,
    REQUEST_ID_HEADER,
    SANDBOX_AUTHORIZE_BASE_URL,
    AsyncWefunder,
    OAuthTokenError,
    RetryOptions,
    TokenManager,
    TokenSet,
    WebhookSignatureError,
    Wefunder,
    WefunderError,
    check_webhook_signature,
    client_credentials_grant,
    construct_event,
    create_authorization_url,
    exchange_code,
    generate_pkce,
    mode_for_token,
    paginate,
    parse_signature_header,
    pkce_challenge,
    refresh_token,
    sign_webhook,
    verify_webhook,
)
from wefunder._retry import AsyncRetryTransport, RetryTransport, rate_limit_wait_ms
from wefunder.errors import error_from_response
from wefunder.token_manager import AsyncTokenManager

VECTORS = Path(__file__).resolve().parent.parent / "conformance"


def load(name: str) -> Any:
    return json.loads((VECTORS / name).read_text())


def secs(unix: float):
    return lambda: float(unix)


def expect_subset(actual: Any, expected: Any, path: str = "") -> None:
    """Every key in ``expected`` must match ``actual``; ``None`` means absent-or-null."""
    for key, value in expected.items():
        got = actual.get(key) if isinstance(actual, dict) else getattr(actual, key, None)
        where = f"{path}.{key}" if path else key
        if value is None:
            assert got is None, f"{where}: expected null, got {got!r}"
        elif isinstance(value, dict) and isinstance(got, dict):
            expect_subset(got, value, where)
        else:
            assert got == value, f"{where}: expected {value!r}, got {got!r}"


def ids(cases: list[dict[str, Any]], key: str = "name") -> list[str]:
    return [str(c.get(key) or c.get("note") or i) for i, c in enumerate(cases)]


def sig_header(headers: dict[str, Any]) -> str | None:
    return next((str(v) for k, v in headers.items() if k.lower() == "wefunder-signature"), None)


# ---------------------------------------------------------------------------- webhooks
WEBHOOKS = load("webhooks.json")


def test_webhooks_constants() -> None:
    assert WEBHOOKS["header_name"].lower() == "wefunder-signature"


@pytest.mark.parametrize("c", WEBHOOKS["verify"], ids=ids(WEBHOOKS["verify"]))
def test_webhooks_verify(c: dict[str, Any]) -> None:
    opts = {"now": secs(c["now"]), "tolerance_seconds": c["tolerance_seconds"]}
    try:
        event = construct_event(c["payload"], c["headers"], c["secret"], **opts)
        result = "ok"
    except WebhookSignatureError as err:
        event = None
        result = err.reason
    assert result == c["expect"]["result"]
    if c["expect"].get("event"):
        assert event is not None
        expect_subset(event, c["expect"]["event"])
    header = sig_header(c["headers"])
    if header and c["expect"]["result"] != "invalid_payload":
        failure = check_webhook_signature(c["payload"], header, c["secret"], **opts)
        assert (failure or "ok") == c["expect"]["result"]
        assert verify_webhook(c["payload"], c["secret"], header=header, **opts) is (c["expect"]["result"] == "ok")


@pytest.mark.parametrize("c", WEBHOOKS["parse_header"], ids=[repr(c["header"]) for c in WEBHOOKS["parse_header"]])
def test_webhooks_parse_header(c: dict[str, Any]) -> None:
    parsed = parse_signature_header(c["header"])
    if c["expect"] is None:
        assert parsed is None
    else:
        assert parsed is not None
        assert parsed.timestamp == c["expect"]["timestamp"]
        assert list(parsed.signatures) == c["expect"]["signatures"]


@pytest.mark.parametrize("c", WEBHOOKS["sign"], ids=ids(WEBHOOKS["sign"]))
def test_webhooks_sign(c: dict[str, Any]) -> None:
    header = sign_webhook(
        c["payload"], c["secret"], timestamp=c["timestamp"], additional_secrets=c.get("additional_secrets", ())
    )
    assert header == c["expect_header"]


LEGACY = load("legacy_webhooks.json")


@pytest.mark.parametrize("c", LEGACY["verify"], ids=ids(LEGACY["verify"]))
def test_legacy_verify(c: dict[str, Any]) -> None:
    kwargs: dict[str, Any] = {"tolerance_seconds": c["tolerance_seconds"]}
    if "now" in c:
        kwargs["now"] = secs(c["now"])
    assert (
        verify_webhook(c["payload"], c["secret"], signature=c["signature"], timestamp=c["timestamp"], **kwargs)
        is c["expect_valid"]
    )


@pytest.mark.parametrize("c", LEGACY["construct"], ids=ids(LEGACY["construct"]))
def test_legacy_construct(c: dict[str, Any]) -> None:
    try:
        event = construct_event(c["payload"], c["headers"], c["secret"], now=secs(c["now"]))
    except WebhookSignatureError as err:
        assert err.reason == c["expect"]["result"]
        return
    assert c["expect"]["result"] == "ok"
    expect_subset(event, c["expect"]["event"])


# ------------------------------------------------------------------------------ errors
ERRORS = load("errors.json")


def test_errors_constants() -> None:
    assert REQUEST_ID_HEADER.lower() == ERRORS["request_id_header"].lower()


@pytest.mark.parametrize("c", ERRORS["cases"], ids=ids(ERRORS["cases"]))
def test_errors(c: dict[str, Any]) -> None:
    err = error_from_response(c["status"], c["headers"], c["body"])
    assert isinstance(err, WefunderError)
    expected = dict(c["expect"])
    message = expected.pop("message", None)
    expect_subset(
        {
            "status": err.status,
            "type": err.type,
            "request_id": err.request_id,
            "details": err.details,
            "remediation": err.remediation,
        },
        expected,
    )
    if message is not None:
        assert err.message == message
    else:
        assert isinstance(err.message, str)


# -------------------------------------------------------------------------- pagination
PAGINATION = load("pagination.json")


def same_cursor(a: Any, b: Any) -> bool:
    return type(a) is type(b) and a == b


@pytest.mark.parametrize("c", PAGINATION["cases"], ids=ids(PAGINATION["cases"]))
def test_pagination(c: dict[str, Any]) -> None:
    sent: list[Any] = []

    def fetch(cursor: Any) -> Any:
        sent.append(cursor)
        for page in c["pages"]:
            if (page["cursor"] is None and cursor is None) or same_cursor(page["cursor"], cursor):
                return page["response"]
        raise AssertionError(f"unexpected cursor {cursor!r}")

    assert list(paginate(fetch)) == c["expect"]["items"]
    assert sent == c["expect"]["cursors_sent"]
    assert all(same_cursor(a, b) for a, b in zip(sent, c["expect"]["cursors_sent"], strict=True))


# ------------------------------------------------------------------------------- retry
RETRY = load("retry.json")


@pytest.mark.parametrize(
    "c", RETRY["rate_limit_wait_ms"]["cases"], ids=ids(RETRY["rate_limit_wait_ms"]["cases"], "note")
)
def test_rate_limit_wait_ms(c: dict[str, Any]) -> None:
    assert rate_limit_wait_ms(c["header"], c["now_ms"], c["max_delay_ms"]) == c["expect_ms"]


def _retry_options(c: dict[str, Any]) -> RetryOptions | None:
    r = c.get("retry")
    return (
        RetryOptions(max_retries=r["max_retries"], base_delay_ms=r["base_delay_ms"], max_delay_ms=r["max_delay_ms"])
        if r
        else None
    )


class _Script:
    def __init__(self, c: dict[str, Any]) -> None:
        self.responses = list(c["responses"])
        self.calls = 0
        self.bodies: list[str] = []
        self.auths: list[str | None] = []
        self.sleeps: list[float] = []

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.calls += 1
        self.auths.append(request.headers.get("authorization"))
        self.bodies.append(request.content.decode())
        nxt = self.responses.pop(0)
        if nxt.get("network_error"):
            raise httpx.ConnectError("network_error", request=request)
        return httpx.Response(nxt["status"], headers=nxt.get("headers", {}), content=(nxt.get("body") or "").encode())

    def check(self, c: dict[str, Any], status: int | None, threw: str | None, oauth_calls: int) -> None:
        e = c["expect"]
        if e.get("throws"):
            assert threw == e["throws"]
        else:
            assert status == e["final_status"]
        assert self.calls == e["calls"]
        assert self.sleeps == e["sleeps_ms"]
        if "bodies_seen" in e:
            assert self.bodies == e["bodies_seen"]
        if "authorization_seen" in e:
            assert self.auths == e["authorization_seen"]
        if "oauth_calls" in e:
            assert oauth_calls == e["oauth_calls"]


def _request(c: dict[str, Any]) -> httpx.Request:
    headers = {"Authorization": f"Bearer {c['token_manager']['access_token']}"} if c.get("token_manager") else {}
    return httpx.Request(c["method"], "https://api.test/x", headers=headers, content=(c.get("body") or "").encode())


@pytest.mark.parametrize("c", RETRY["cases"], ids=ids(RETRY["cases"]))
def test_retry_sync(c: dict[str, Any]) -> None:
    script = _Script(c)
    oauth_calls = 0
    tm = None
    if c.get("token_manager"):
        t = c["token_manager"]

        def oauth(request: httpx.Request) -> httpx.Response:
            nonlocal oauth_calls
            oauth_calls += 1
            return httpx.Response(200, json=t["oauth_response"])

        tm = TokenManager(
            TokenSet(t["access_token"], t["refresh_token"]),
            client_id=t["client_id"],
            transport=httpx.MockTransport(oauth),
        )
    transport = RetryTransport(
        httpx.MockTransport(script.handler),
        token_manager=tm,
        retry=_retry_options(c),
        sleep=script.sleeps.append,
        now_ms=lambda: c.get("now_ms", 0),
        random=lambda: c.get("random", 0),
    )
    status = threw = None
    try:
        status = transport.handle_request(_request(c)).status_code
    except httpx.TransportError as err:
        threw = str(err)
    script.check(c, status, threw, oauth_calls)


@pytest.mark.parametrize("c", RETRY["cases"], ids=ids(RETRY["cases"]))
async def test_retry_async(c: dict[str, Any]) -> None:
    script = _Script(c)
    oauth_calls = 0
    tm = None
    if c.get("token_manager"):
        t = c["token_manager"]

        def oauth(request: httpx.Request) -> httpx.Response:
            nonlocal oauth_calls
            oauth_calls += 1
            return httpx.Response(200, json=t["oauth_response"])

        tm = AsyncTokenManager(
            TokenSet(t["access_token"], t["refresh_token"]),
            client_id=t["client_id"],
            transport=httpx.MockTransport(oauth),
        )

    async def sleep(ms: float) -> None:
        script.sleeps.append(ms)

    transport = AsyncRetryTransport(
        httpx.MockTransport(script.handler),
        token_manager=tm,
        retry=_retry_options(c),
        sleep=sleep,
        now_ms=lambda: c.get("now_ms", 0),
        random=lambda: c.get("random", 0),
    )
    status = threw = None
    try:
        status = (await transport.handle_async_request(_request(c))).status_code
    except httpx.TransportError as err:
        threw = str(err)
    script.check(c, status, threw, oauth_calls)


# ---------------------------------------------------------------------- token recovery
RECOVERY = load("token_recovery.json")


@pytest.mark.parametrize("c", RECOVERY["token_set_conversion"]["cases"], ids=lambda c: c["raw"]["access_token"])
def test_token_set_conversion(c: dict[str, Any]) -> None:
    tokens = client_credentials_grant(
        client_id="c",
        client_secret="s",
        transport=httpx.MockTransport(lambda r: httpx.Response(200, json=c["raw"])),
        now=lambda: c["now_ms"] / 1000,
    )
    expect_subset(
        {
            "access_token": tokens.access_token,
            "refresh_token": tokens.refresh_token,
            "expires_at_ms": None if tokens.expires_at is None else round(tokens.expires_at * 1000),
            "token_type": tokens.token_type,
            "scope": tokens.scope,
        },
        c["expect"],
    )


class _Scenario:
    def __init__(self, s: dict[str, Any]) -> None:
        self.s = s
        self.oauth_responses = list(s["oauth_responses"])
        self.oauth_params: list[dict[str, str]] = []
        self.api_bearers: list[str | None] = []
        self.persisted: list[str | None] = []
        self.transport = httpx.MockTransport(self.handler)

    def handler(self, request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/oauth/token"):
            self.oauth_params.append({k: v[0] for k, v in parse_qs(request.content.decode()).items()})
            assert self.oauth_responses, "unexpected OAuth call"
            return httpx.Response(200, json=self.oauth_responses.pop(0))
        bearer = request.headers.get("authorization")
        self.api_bearers.append(bearer)
        api = self.s["api"]
        if api.get("reject_bearer") and bearer == api["reject_bearer"]:
            return httpx.Response(401, content=b"{}")
        return httpx.Response(200, content=api["accept_body"].encode(), headers={"content-type": "application/json"})

    class Store:
        def __init__(self, sink: list[str | None]) -> None:
            self.sink = sink

        def save(self, tokens: TokenSet) -> None:
            self.sink.append(tokens.refresh_token)

    def client_kwargs(self) -> dict[str, Any]:
        kw: dict[str, Any] = {"transport": self.transport}
        if "now_ms" in self.s:
            kw["now"] = lambda: self.s["now_ms"] / 1000
        return kw

    def check(self, wf: Any, result: str, error_status: int | None) -> None:
        e = self.s["expect"]
        assert result == e["result"]
        if "error_status" in e:
            assert error_status == e["error_status"]
        assert len(self.oauth_params) == e["oauth_calls"]
        if "oauth_grant_types" in e:
            assert [p["grant_type"] for p in self.oauth_params] == e["oauth_grant_types"]
        for got, want in zip(self.oauth_params, e.get("oauth_params", []), strict=False):
            expect_subset(got, want)
        if "final_access_token" in e:
            assert wf.tokens.access_token == e["final_access_token"]
        if "final_refresh_token" in e:
            assert wf.tokens.refresh_token == e["final_refresh_token"]
        if "persisted_refresh_tokens" in e:
            assert self.persisted == e["persisted_refresh_tokens"]
        if "last_api_bearer" in e:
            assert self.api_bearers[-1] == e["last_api_bearer"]
        if "api_calls" in e:
            assert len(self.api_bearers) == e["api_calls"]


def _tokens(t: dict[str, Any]) -> TokenSet:
    exp = t.get("expires_at_ms")
    return TokenSet(t["access_token"], t.get("refresh_token"), None if exp is None else exp / 1000)


@pytest.mark.parametrize("s", RECOVERY["scenarios"], ids=ids(RECOVERY["scenarios"]))
def test_token_recovery_sync(s: dict[str, Any]) -> None:
    sc = _Scenario(s)
    client = s["client"]
    if "client_credentials" in client:
        cc = client["client_credentials"]
        wf = Wefunder.from_client_credentials(
            client_id=cc["client_id"], client_secret=cc["client_secret"], scopes=cc.get("scopes"), **sc.client_kwargs()
        )
        call = wf.offerings.list
    else:
        wf = Wefunder(
            tokens=_tokens(client["tokens"]),
            client_id=client.get("client_id"),
            client_secret=client.get("client_secret"),
            store=_Scenario.Store(sc.persisted),
            **sc.client_kwargs(),
        )
        call = wf.users.me
    result, error_status = "ok", None
    try:
        with ThreadPoolExecutor(max_workers=s["concurrent_requests"]) as pool:
            list(pool.map(lambda _: call(), range(s["concurrent_requests"])))
    except WefunderError as err:
        result, error_status = "error", err.status
    sc.check(wf, result, error_status)


@pytest.mark.parametrize("s", RECOVERY["scenarios"], ids=ids(RECOVERY["scenarios"]))
async def test_token_recovery_async(s: dict[str, Any]) -> None:
    sc = _Scenario(s)
    client = s["client"]
    if "client_credentials" in client:
        cc = client["client_credentials"]
        wf = await AsyncWefunder.from_client_credentials(
            client_id=cc["client_id"], client_secret=cc["client_secret"], scopes=cc.get("scopes"), **sc.client_kwargs()
        )
        call = wf.offerings.list
    else:
        wf = AsyncWefunder(
            tokens=_tokens(client["tokens"]),
            client_id=client.get("client_id"),
            client_secret=client.get("client_secret"),
            store=_Scenario.Store(sc.persisted),
            **sc.client_kwargs(),
        )
        call = wf.users.me
    result, error_status = "ok", None
    try:
        await asyncio.gather(*(call() for _ in range(s["concurrent_requests"])))
    except WefunderError as err:
        result, error_status = "error", err.status
    sc.check(wf, result, error_status)


# ------------------------------------------------------------------------------- oauth
OAUTH = load("oauth.json")


def test_oauth_constants() -> None:
    k = OAUTH["constants"]
    assert k["api_base_url"] == DEFAULT_API_BASE_URL
    assert k["default_api_version"] == DEFAULT_API_VERSION
    assert k["authorize_base_url_live"] == DEFAULT_AUTHORIZE_BASE_URL
    assert k["authorize_base_url_sandbox"] == SANDBOX_AUTHORIZE_BASE_URL
    assert k["token_base_url"] == DEFAULT_TOKEN_BASE_URL


@pytest.mark.parametrize("c", OAUTH["mode_from_token"], ids=lambda c: repr(c["token"]))
def test_mode_from_token(c: dict[str, Any]) -> None:
    assert mode_for_token(c["token"]) == c["expect"]


def test_pkce() -> None:
    p = OAUTH["pkce"]
    assert pkce_challenge(p["verifier"]) == p["challenge"]
    generated = generate_pkce()
    assert generated.code_challenge_method == p["method"]
    assert re.fullmatch(p["verifier_charset_regex"], generated.code_verifier)
    assert pkce_challenge(generated.code_verifier) == generated.code_challenge


@pytest.mark.parametrize("c", OAUTH["authorize_url"], ids=ids(OAUTH["authorize_url"]))
def test_authorize_url(c: dict[str, Any]) -> None:
    url = create_authorization_url(
        client_id=c["client_id"],
        redirect_uri=c["redirect_uri"],
        scopes=c["scopes"],
        state=c["state"],
        code_challenge=c["code_challenge"],
        authorize_base_url=c.get("authorize_base_url"),
        token_base_url=c.get("token_base_url"),
        oauth_base_url=c.get("oauth_base_url"),
    )
    parts = urlsplit(url)
    assert f"{parts.scheme}://{parts.netloc}{parts.path}" == c["expect"]["base"]
    params = {k: v[0] for k, v in parse_qs(parts.query).items()}
    for key, value in c["expect"].get("params", {}).items():
        assert params[key] == value, key


def _capture() -> tuple[list[httpx.Request], httpx.MockTransport]:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        return httpx.Response(200, json={"access_token": "at_test_x"})

    return seen, httpx.MockTransport(handler)


@pytest.mark.parametrize("c", OAUTH["token_host"], ids=ids(OAUTH["token_host"]))
def test_token_host(c: dict[str, Any]) -> None:
    seen, transport = _capture()
    o = c["overrides"]
    client_credentials_grant(
        client_id="c",
        client_secret="s",
        transport=transport,
        token_base_url=o.get("token_base_url"),
        oauth_base_url=o.get("oauth_base_url"),
    )
    assert str(seen[0].url) == c["expect_url"]


@pytest.mark.parametrize("c", OAUTH["token_requests"]["cases"], ids=ids(OAUTH["token_requests"]["cases"]))
def test_token_requests(c: dict[str, Any]) -> None:
    seen, transport = _capture()
    if c["grant"] == "client_credentials":
        client_credentials_grant(
            client_id=c["client_id"], client_secret=c["client_secret"], scopes=c.get("scopes"), transport=transport
        )
    elif c["grant"] == "authorization_code":
        exchange_code(
            client_id=c["client_id"],
            client_secret=c.get("client_secret"),
            code=c["code"],
            redirect_uri=c["redirect_uri"],
            code_verifier=c["code_verifier"],
            transport=transport,
        )
    else:
        refresh_token(
            client_id=c["client_id"],
            client_secret=c.get("client_secret"),
            refresh_token=c["refresh_token"],
            transport=transport,
        )
    req = seen[0]
    assert req.method == "POST"
    assert req.headers["content-type"].startswith("application/x-www-form-urlencoded")
    params = {k: v[0] for k, v in parse_qs(req.content.decode()).items()}
    assert params == c["expect"]["params"]
    for absent in c["expect"].get("absent", []):
        assert absent not in params


def test_token_request_error() -> None:
    e = OAUTH["token_requests"]["error"]
    transport = httpx.MockTransport(lambda r: httpx.Response(e["status"], content=e["body"].encode()))
    with pytest.raises(OAuthTokenError, match=e["expect_message_includes"]):
        refresh_token(client_id="c", refresh_token="r", transport=transport)


# ---------------------------------------------------------------------------- manifest
def test_vendored_vectors_match_manifest() -> None:
    manifest = load("manifest.json")
    for name, sha in manifest["files"].items():
        assert hashlib.sha256((VECTORS / name).read_bytes()).hexdigest() == sha, (
            f"{name} differs from the pinned manifest — run scripts/sync_conformance.py"
        )
