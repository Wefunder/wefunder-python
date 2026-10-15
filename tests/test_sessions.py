"""`wf.join_sessions` + `wf.investment_sessions` (beta since wefunder #24129), sync and async."""

from __future__ import annotations

import asyncio
import json

import httpx

from wefunder import AsyncWefunder, Wefunder

JS = {
    "id": "js_1",
    "type": "join_session",
    "attributes": {"status": "pending", "email": "m@example.com", "url": "https://wefunder.com/join/session/js_1"},
}
IS = {
    "id": "is_1",
    "type": "investment_session",
    "attributes": {"status": "pending", "url": "https://wefunder.com/invest/session/is_1"},
}


class Recorder:
    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []
        self.transport = httpx.MockTransport(self.handler)

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        path = request.url.path
        if request.method == "POST" and path.endswith("/join_sessions"):
            return httpx.Response(201, json={"data": JS})
        if path == "/syndicates/syn_1/join_sessions":
            if request.url.params.get("cursor"):
                return httpx.Response(200, json={"data": [{**JS, "id": "js_2"}], "meta": {"has_more": False}})
            return httpx.Response(200, json={"data": [JS], "meta": {"has_more": True, "next_cursor": "c2"}})
        if path.startswith("/syndicates/syn_1/join_sessions/"):
            return httpx.Response(200, json={"data": JS})
        if request.method == "POST":
            return httpx.Response(201, json={"data": IS})
        if request.method == "DELETE":
            return httpx.Response(200, json={"data": {**IS, "attributes": {**IS["attributes"], "status": "canceled"}}})
        if path == "/investment_sessions":
            return httpx.Response(200, json={"data": [IS], "meta": {"has_more": False}})
        if path == "/offerings/ofr_1/investment_sessions":
            if request.url.params.get("cursor"):
                return httpx.Response(200, json={"data": [{**IS, "id": "is_2"}], "meta": {"has_more": False}})
            return httpx.Response(200, json={"data": [IS], "meta": {"has_more": True, "next_cursor": 9}})
        return httpx.Response(200, json={"data": IS})

    @property
    def seen(self) -> list[str]:
        return [f"{r.method} {r.url.path}" for r in self.requests]


def test_join_sessions_untyped_responses_unwrap_to_dicts_and_paths_are_right() -> None:
    rec = Recorder()
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    assert [s["id"] for s in wf.join_sessions.all("syn_1", per_page=1)] == ["js_1", "js_2"]
    created = wf.join_sessions.create("syn_1", {"email": "m@example.com", "require_approval": True})
    assert created["attributes"]["url"].startswith("https://wefunder.com/join/session/")
    assert wf.join_sessions.get("syn_1", "js_1")["id"] == "js_1"
    assert rec.seen == [
        "GET /syndicates/syn_1/join_sessions",
        "GET /syndicates/syn_1/join_sessions",
        "POST /syndicates/syn_1/join_sessions",
        "GET /syndicates/syn_1/join_sessions/js_1",
    ]
    assert rec.requests[0].url.params["per_page"] == "1"
    assert json.loads(rec.requests[2].content) == {"join_session": {"email": "m@example.com", "require_approval": True}}


def test_investment_sessions_filters_bodies_idempotency_and_paths() -> None:
    rec = Recorder()
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    assert wf.investment_sessions.list(status="in_progress", spv_id="spv_1").data[0].id == "is_1"
    assert rec.requests[0].url.params["status"] == "in_progress"
    assert [s.id for s in wf.investment_sessions.all_for_offering("ofr_1", status="completed")] == ["is_1", "is_2"]
    assert rec.requests[1].url.params["status"] == "completed"
    created = wf.investment_sessions.create(
        "ofr_1", {"email": "i@example.com", "allocation_cents": 250000}, idempotency_key="k1"
    )
    assert created.id == "is_1"
    assert wf.investment_sessions.get("is_1").id == "is_1"
    assert wf.investment_sessions.cancel("is_1").attributes.status == "canceled"
    assert rec.seen[3:] == [
        "POST /offerings/ofr_1/investment_sessions",
        "GET /investment_sessions/is_1",
        "DELETE /investment_sessions/is_1",
    ]
    assert json.loads(rec.requests[3].content) == {
        "investment_session": {"email": "i@example.com", "allocation_cents": 250000}
    }
    assert rec.requests[3].headers["idempotency-key"] == "k1"


def test_async_sessions_mirror_sync() -> None:
    async def run() -> None:
        rec = Recorder()
        async with AsyncWefunder(access_token="at_live_x", transport=rec.transport) as wf:
            assert [s["id"] async for s in wf.join_sessions.all("syn_1")] == ["js_1", "js_2"]
            assert (await wf.join_sessions.create("syn_1", {"email": "m@example.com"}))["id"] == "js_1"
            assert [s.id async for s in wf.investment_sessions.all_for_offering("ofr_1")] == ["is_1", "is_2"]
            assert (await wf.investment_sessions.cancel("is_1")).attributes.status == "canceled"

    asyncio.run(run())
