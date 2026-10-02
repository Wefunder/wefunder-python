"""Rotated tokens must be durable BEFORE any caller can use them (wefunder-ruby#1, applied to every SDK).
Every configured persistence path (store.save AND on_token_refresh) must succeed before publication."""

from __future__ import annotations

import asyncio
import threading
import time
from typing import Any

import httpx
import pytest

from wefunder import (
    AsyncTokenManager,
    AsyncWefunder,
    TokenManager,
    TokenSet,
    Wefunder,
    WefunderTokenPersistenceError,
    async_exchange_code,
    exchange_code,
)
from wefunder._retry import RetryTransport

OAUTH = httpx.MockTransport(lambda r: httpx.Response(200, json={"access_token": "at_live_NEW", "refresh_token": "r2"}))


def tokens() -> TokenSet:
    return TokenSet("at_live_OLD", "r1")


def manager(path: str, persist: Any) -> TokenManager:
    if path == "store":
        store = type("Store", (), {"save": staticmethod(persist)})()
        return TokenManager(tokens(), client_id="c", transport=OAUTH, store=store)
    return TokenManager(tokens(), client_id="c", transport=OAUTH, on_token_refresh=persist)


def test_store_sees_old_token_current_while_saving() -> None:
    observed: list[tuple[str, str]] = []
    holder: dict[str, TokenManager] = {}

    def save(s: TokenSet) -> None:
        observed.append((s.access_token, holder["tm"].current.access_token))

    holder["tm"] = manager("store", save)
    holder["tm"].refresh()
    assert observed == [("at_live_NEW", "at_live_OLD")]


@pytest.mark.parametrize("path", ["store", "callback"])
def test_barrier_reader_never_sees_undurable_token(path: str) -> None:
    entered, release = threading.Event(), threading.Event()

    def persist(_s: TokenSet) -> None:
        entered.set()
        release.wait(5)

    tm = manager(path, persist)
    results: dict[str, str] = {}
    refresher = threading.Thread(target=lambda: results.__setitem__("refresh", tm.refresh().access_token))
    refresher.start()
    assert entered.wait(5)
    reader = threading.Thread(target=lambda: results.__setitem__("read", tm.get_access_token()))
    reader.start()
    time.sleep(0.05)
    assert reader.is_alive()
    assert tm.current.access_token == "at_live_OLD"
    release.set()
    refresher.join(5)
    reader.join(5)
    assert results == {"refresh": "at_live_NEW", "read": "at_live_NEW"}


@pytest.mark.parametrize("path", ["store", "callback"])
def test_failing_path_keeps_set_pending_and_retries(path: str) -> None:
    attempts = {"n": 0}

    def persist(_s: TokenSet) -> None:
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise OSError("disk full")

    tm = manager(path, persist)
    with pytest.raises(WefunderTokenPersistenceError) as info:
        tm.refresh()
    assert info.value.tokens.refresh_token == "r2"
    assert "disk full" in str(info.value)
    assert tm.current.access_token == "at_live_OLD"
    assert tm.pending_tokens is not None and tm.pending_tokens.access_token == "at_live_NEW"
    assert tm.get_access_token() == "at_live_NEW"
    assert attempts["n"] == 2
    assert tm.pending_tokens is None


def test_callback_runs_before_publication_after_store() -> None:
    order: list[str] = []
    holder: dict[str, TokenManager] = {}
    store = type(
        "Store", (), {"save": staticmethod(lambda s: order.append(f"save current={holder['tm'].current.access_token}"))}
    )()
    holder["tm"] = TokenManager(
        tokens(),
        client_id="c",
        transport=OAUTH,
        store=store,
        on_token_refresh=lambda s: order.append(f"callback current={holder['tm'].current.access_token}"),
    )
    holder["tm"].refresh()
    assert order == ["save current=at_live_OLD", "callback current=at_live_OLD"]


def test_mark_persisted_bound_to_saved_set_stale_ack_cannot_publish_r3() -> None:
    mint = {"n": 0}

    def oauth(_r: httpx.Request) -> httpx.Response:
        mint["n"] += 1
        return httpx.Response(
            200, json={"access_token": f"at_live_{mint['n'] + 1}", "refresh_token": f"r{mint['n'] + 1}"}
        )

    fail = {"next": True}

    def save(_s: TokenSet) -> None:
        if fail["next"]:
            fail["next"] = False
            raise OSError("down")

    store = type("Store", (), {"save": staticmethod(save)})()
    tm = TokenManager(tokens(), client_id="c", transport=httpx.MockTransport(oauth), store=store)
    with pytest.raises(WefunderTokenPersistenceError) as err_a:  # r1 -> r2, save fails; A holds r2
        tm.refresh()
    assert err_a.value.tokens.refresh_token == "r2"
    assert tm.get_access_token() == "at_live_2"  # B retries persistence and publishes r2
    fail["next"] = True
    with pytest.raises(WefunderTokenPersistenceError) as err_b:  # r2 -> r3, save fails
        tm.refresh()
    assert err_b.value.tokens.refresh_token == "r3"
    assert tm.mark_persisted(err_a.value.tokens) is False  # stale r2 ack must not publish r3
    assert tm.pending_tokens is not None and tm.pending_tokens.refresh_token == "r3"
    assert tm.current.refresh_token == "r2"
    assert tm.mark_persisted(err_b.value.tokens) is True
    assert tm.current.refresh_token == "r3" and tm.pending_tokens is None


def test_transport_never_sends_undurable_token() -> None:
    api_calls: list[str | None] = []

    def api(request: httpx.Request) -> httpx.Response:
        api_calls.append(request.headers.get("authorization"))
        return httpx.Response(401, content=b"{}")

    store = type("Store", (), {"save": staticmethod(lambda s: (_ for _ in ()).throw(OSError("disk full")))})()
    tm = TokenManager(tokens(), client_id="c", transport=OAUTH, store=store)
    transport = RetryTransport(httpx.MockTransport(api), token_manager=tm)
    with pytest.raises(WefunderTokenPersistenceError):
        transport.handle_request(httpx.Request("GET", "https://api.test/x"))
    assert api_calls == ["Bearer at_live_OLD"]


def test_public_client_surfaces_persistence_error_and_mark_persisted_recovers() -> None:
    fail = {"on": True}

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path.endswith("/oauth/token"):
            return httpx.Response(200, json={"access_token": "at_live_NEW", "refresh_token": "r2"})
        if request.headers.get("authorization") == "Bearer at_live_OLD":
            return httpx.Response(401, content=b"{}")
        return httpx.Response(200, json={"data": {"id": "usr_1", "type": "user"}})

    class FlakyStore:
        def save(self, s: TokenSet) -> None:
            if fail["on"]:
                raise OSError("db down")

    wf = Wefunder(
        tokens=TokenSet("at_live_OLD", "r1", 1e10),
        client_id="c",
        store=FlakyStore(),
        transport=httpx.MockTransport(handler),
    )
    with pytest.raises(WefunderTokenPersistenceError) as info:
        wf.users.me()
    assert wf.token_manager.mark_persisted(info.value.tokens) is True
    fail["on"] = False
    assert wf.users.me().id == "usr_1"


@pytest.mark.parametrize("path", ["store", "callback"])
async def test_async_manager_callback_and_store_gate_publication(path: str) -> None:
    attempts = {"n": 0}

    async def persist(_s: TokenSet) -> None:
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise OSError("disk full")

    kwargs: dict[str, Any] = (
        {"store": type("Store", (), {"save": staticmethod(persist)})()}
        if path == "store"
        else {"on_token_refresh": persist}
    )
    tm = AsyncTokenManager(tokens(), client_id="c", transport=OAUTH, **kwargs)
    with pytest.raises(WefunderTokenPersistenceError):
        await tm.refresh()
    assert tm.current.access_token == "at_live_OLD"
    assert await tm.get_access_token() == "at_live_NEW"
    assert attempts["n"] == 2


async def test_async_barrier_reader_waits_for_in_flight_save() -> None:
    entered, release = asyncio.Event(), asyncio.Event()

    async def save(_s: TokenSet) -> None:
        entered.set()
        await release.wait()

    tm = AsyncTokenManager(
        tokens(), client_id="c", transport=OAUTH, store=type("Store", (), {"save": staticmethod(save)})()
    )
    refreshing = asyncio.create_task(tm.refresh())
    await entered.wait()
    reader = asyncio.create_task(tm.get_access_token())
    await asyncio.sleep(0.02)
    assert not reader.done()
    assert tm.current.access_token == "at_live_OLD"
    release.set()
    assert (await refreshing).access_token == "at_live_NEW"
    assert await reader == "at_live_NEW"


# ---- timeout propagation (sync + async): refresh, 401 re-mint, code exchange, initial mint


def recorder() -> tuple[list[httpx.Request], httpx.MockTransport]:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.path.endswith("/oauth/token"):
            return httpx.Response(200, json={"access_token": "at_live_NEW", "refresh_token": "r2", "expires_in": 7200})
        if request.headers.get("authorization") in ("Bearer at_live_OLD", "Bearer at_test_OLD"):
            return httpx.Response(401, content=b"{}")
        return httpx.Response(200, json={"data": [], "meta": {}})

    return seen, httpx.MockTransport(handler)


def connect_timeouts(seen: list[httpx.Request]) -> list[float | None]:
    return [r.extensions["timeout"]["connect"] for r in seen if r.url.path.endswith("/oauth/token")]


def test_timeout_reaches_refresh_remint_exchange_and_initial_mint_sync() -> None:
    seen, transport = recorder()
    wf = Wefunder(
        tokens=TokenSet("at_live_OLD", "r1", 1e10), client_id="c", client_secret="s", transport=transport, timeout=11.0
    )
    wf.offerings.list()  # 401 -> refresh
    cc = Wefunder.from_client_credentials(client_id="c", client_secret="s", transport=transport, timeout=7.0)
    cc.offerings.list()  # initial mint (at_live_NEW accepted) -> no re-mint needed; force one:
    exchange_code(
        client_id="c", code="x", redirect_uri="https://a/cb", code_verifier="v", transport=transport, timeout=3.0
    )
    assert connect_timeouts(seen) == [11.0, 7.0, 3.0]


async def test_timeout_reaches_refresh_and_exchange_async() -> None:
    seen, transport = recorder()
    wf = AsyncWefunder(tokens=TokenSet("at_live_OLD", "r1", 1e10), client_id="c", transport=transport, timeout=11.0)
    await wf.offerings.list()
    await async_exchange_code(
        client_id="c", code="x", redirect_uri="https://a/cb", code_verifier="v", transport=transport, timeout=3.0
    )
    assert connect_timeouts(seen) == [11.0, 3.0]
