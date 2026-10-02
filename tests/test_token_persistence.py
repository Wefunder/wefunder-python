"""Rotated tokens must be durable BEFORE any caller can use them (wefunder-ruby#1, applied to every SDK)."""

from __future__ import annotations

import threading
import time

import httpx
import pytest

from wefunder import AsyncTokenManager, TokenManager, TokenSet, WefunderTokenPersistenceError
from wefunder._retry import RetryTransport
from wefunder.client import Wefunder

OAUTH = httpx.MockTransport(lambda r: httpx.Response(200, json={"access_token": "at_live_NEW", "refresh_token": "r2"}))


def tokens() -> TokenSet:
    return TokenSet("at_live_OLD", "r1")


class Store:
    def __init__(self, fail_first: bool = False) -> None:
        self.observed: list[tuple[str, str | None]] = []
        self.attempts = 0
        self.fail_first = fail_first
        self.manager: TokenManager | None = None

    def save(self, s: TokenSet) -> None:
        self.attempts += 1
        self.observed.append((s.access_token, self.manager.current.access_token if self.manager else None))
        if self.fail_first and self.attempts == 1:
            raise OSError("disk full")


def test_store_sees_old_token_current_while_saving() -> None:
    store = Store()
    tm = TokenManager(tokens(), client_id="c", transport=OAUTH, store=store)
    store.manager = tm
    tm.refresh()
    assert store.observed == [("at_live_NEW", "at_live_OLD")]
    assert tm.current.access_token == "at_live_NEW"


def test_barrier_concurrent_reader_never_sees_undurable_token() -> None:
    entered = threading.Event()
    release = threading.Event()

    class Blocking:
        def save(self, s: TokenSet) -> None:
            entered.set()
            release.wait(5)

    tm = TokenManager(tokens(), client_id="c", transport=OAUTH, store=Blocking())
    results: dict[str, str] = {}
    refresher = threading.Thread(target=lambda: results.__setitem__("refresh", tm.refresh().access_token))
    refresher.start()
    assert entered.wait(5)
    reader = threading.Thread(target=lambda: results.__setitem__("read", tm.get_access_token()))
    reader.start()
    time.sleep(0.05)
    assert reader.is_alive()  # waits on the lock instead of reading the pending set
    assert tm.current.access_token == "at_live_OLD"
    release.set()
    refresher.join(5)
    reader.join(5)
    assert results == {"refresh": "at_live_NEW", "read": "at_live_NEW"}


def test_failing_store_keeps_set_pending_and_retries_on_next_call() -> None:
    store = Store(fail_first=True)
    tm = TokenManager(tokens(), client_id="c", transport=OAUTH, store=store)
    with pytest.raises(WefunderTokenPersistenceError) as info:
        tm.refresh()
    assert info.value.tokens.refresh_token == "r2"
    assert "disk full" in str(info.value)
    assert tm.current.access_token == "at_live_OLD"  # not published
    assert tm.pending_tokens is not None and tm.pending_tokens.access_token == "at_live_NEW"
    assert tm.get_access_token() == "at_live_NEW"  # save retried, no second rotation
    assert store.attempts == 2
    assert tm.pending_tokens is None


def test_mark_persisted_publishes_out_of_band_save() -> None:
    class Failing:
        def save(self, s: TokenSet) -> None:
            raise OSError("disk full")

    tm = TokenManager(tokens(), client_id="c", transport=OAUTH, store=Failing())
    with pytest.raises(WefunderTokenPersistenceError):
        tm.refresh()
    tm.mark_persisted()
    assert tm.current.access_token == "at_live_NEW"
    assert tm.pending_tokens is None


def test_transport_surfaces_persistence_error_instead_of_using_pending_token() -> None:
    class Failing:
        def save(self, s: TokenSet) -> None:
            raise OSError("disk full")

    api_calls: list[str | None] = []

    def api(request: httpx.Request) -> httpx.Response:
        api_calls.append(request.headers.get("authorization"))
        return httpx.Response(401, content=b"{}")

    tm = TokenManager(tokens(), client_id="c", transport=OAUTH, store=Failing())
    transport = RetryTransport(httpx.MockTransport(api), token_manager=tm)
    with pytest.raises(WefunderTokenPersistenceError):
        transport.handle_request(httpx.Request("GET", "https://api.test/x"))
    assert api_calls == ["Bearer at_live_OLD"]  # the undurable token was never sent


async def test_async_manager_gates_publication_on_persistence() -> None:
    attempts = 0

    class Store:
        async def save(self, s: TokenSet) -> None:
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise OSError("disk full")

    tm = AsyncTokenManager(tokens(), client_id="c", transport=OAUTH, store=Store())
    with pytest.raises(WefunderTokenPersistenceError):
        await tm.refresh()
    assert tm.current.access_token == "at_live_OLD"
    assert await tm.get_access_token() == "at_live_NEW"
    assert attempts == 2


def test_client_timeout_reaches_oauth_round_trips() -> None:
    seen: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request)
        if request.url.path.endswith("/oauth/token"):
            return httpx.Response(200, json={"access_token": "at_test_x", "expires_in": 7200})
        return httpx.Response(200, json={"data": [], "meta": {}})

    wf = Wefunder.from_client_credentials(
        client_id="c", client_secret="s", transport=httpx.MockTransport(handler), timeout=11.0
    )
    wf.offerings.list()
    assert [r.extensions["timeout"]["connect"] for r in seen] == [11.0, 11.0]
