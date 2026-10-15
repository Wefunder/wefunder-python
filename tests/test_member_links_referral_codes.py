"""`wf.member_links` + `wf.referral_codes` (Wefunder-Version 2026-10-15), sync and async."""

from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx

from wefunder import DEFAULT_API_VERSION, AsyncWefunder, Wefunder

LINK = {"id": "il_1", "type": "member_link", "attributes": {"reference": "member_8812", "state": "created"}}
CODE = {
    "id": "ref_1",
    "type": "referral_code",
    "attributes": {"label": "October", "active": True, "link_parameter": "wfr=ref_1"},
}


class Recorder:
    def __init__(self, respond: Any) -> None:
        self.requests: list[httpx.Request] = []
        self.respond = respond
        self.transport = httpx.MockTransport(self.handler)

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        body = self.respond(request)
        return body if isinstance(body, httpx.Response) else httpx.Response(200, json=body)

    @property
    def seen(self) -> list[str]:
        return [f"{r.method} {r.url.path}" for r in self.requests]


def respond(request: httpx.Request) -> Any:
    path = request.url.path
    if path == "/offerings/ofr_1/member_links" and request.method == "POST":
        return httpx.Response(201, json={"data": LINK})
    if path == "/offerings/ofr_1/member_links":
        if request.url.params.get("cursor"):
            return {"data": [{**LINK, "id": "il_2"}], "meta": {"has_more": False, "next_cursor": None}}
        return {"data": [LINK], "meta": {"has_more": True, "next_cursor": 7}}
    if path == "/member_links/il_1/cancel":
        return {"data": {**LINK, "attributes": {**LINK["attributes"], "state": "canceled"}}}
    if path == "/referral_codes" and request.method == "GET":
        return {"data": [CODE], "meta": {"has_more": False, "next_cursor": None, "active_limit": 50}}
    if path == "/referral_codes/ref_1/stats":
        return {
            "data": {
                "id": "ref_1",
                "type": "referral_code_stats",
                "attributes": {
                    "label": "October",
                    "companies": [{"company": "co_1", "level": "anonymized", "weeks": []}],
                },
            },
            "meta": {"has_more": False, "next_cursor": None},
        }
    if path.startswith("/referral_codes"):
        return httpx.Response(201 if request.method == "POST" else 200, json={"data": CODE})
    return {"data": LINK}


def test_default_version_is_2026_10_15_and_sent() -> None:
    rec = Recorder(lambda r: {"data": {"id": "usr_1"}})
    Wefunder(access_token="at_test_x", transport=rec.transport).users.me()
    assert DEFAULT_API_VERSION == "2026-10-15"
    assert rec.requests[0].headers["wefunder-version"] == "2026-10-15"


def test_member_links_paths_bodies_and_idempotency() -> None:
    rec = Recorder(respond)
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    assert [link.id for link in wf.member_links.all("ofr_1")] == ["il_1", "il_2"]
    created = wf.member_links.create("ofr_1", {"reference": "member_8812"}, idempotency_key="k1")
    assert created.id == "il_1"
    assert wf.member_links.get("il_1").id == "il_1"
    assert wf.member_links.cancel("il_1").attributes.state == "canceled"
    wf.member_links.create("ofr_1")  # no body, no key
    assert rec.seen == [
        "GET /offerings/ofr_1/member_links",
        "GET /offerings/ofr_1/member_links",
        "POST /offerings/ofr_1/member_links",
        "GET /member_links/il_1",
        "POST /member_links/il_1/cancel",
        "POST /offerings/ofr_1/member_links",
    ]
    assert json.loads(rec.requests[2].content) == {"member_link": {"reference": "member_8812"}}
    assert rec.requests[2].headers["idempotency-key"] == "k1"
    assert rec.requests[5].content == b""
    assert "idempotency-key" not in rec.requests[5].headers


def test_referral_codes_paths_bodies_and_stats_envelope() -> None:
    rec = Recorder(respond)
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    assert wf.referral_codes.list(active=True, per_page=10).data[0].id == "ref_1"
    assert rec.requests[0].url.params["active"] == "true"
    created = wf.referral_codes.create({"label": "October", "company_id": "co_1", "utm": {"source": "newsletter"}})
    assert created.attributes.link_parameter == "wfr=ref_1"
    wf.referral_codes.get("ref_1")
    wf.referral_codes.update("ref_1", active=False)
    stats = wf.referral_codes.stats("ref_1", company_id="co_1")
    assert stats.data.attributes.companies[0].company == "co_1"
    assert stats.meta.has_more is False
    assert rec.seen == [
        "GET /referral_codes",
        "POST /referral_codes",
        "GET /referral_codes/ref_1",
        "PATCH /referral_codes/ref_1",
        "GET /referral_codes/ref_1/stats",
    ]
    assert json.loads(rec.requests[1].content) == {
        "label": "October",
        "company_id": "co_1",
        "utm": {"source": "newsletter"},
    }
    assert json.loads(rec.requests[3].content) == {"active": False}
    assert rec.requests[4].url.params["company_id"] == "co_1"


def test_async_namespaces_mirror_sync() -> None:
    async def run() -> None:
        rec = Recorder(respond)
        async with AsyncWefunder(access_token="at_live_x", transport=rec.transport) as wf:
            assert [link.id async for link in wf.member_links.all("ofr_1")] == ["il_1", "il_2"]
            created = await wf.member_links.create("ofr_1", {"reference": "m"}, idempotency_key="k")
            assert created.id == "il_1"
            assert (await wf.member_links.cancel("il_1")).attributes.state == "canceled"
            assert [c.id async for c in wf.referral_codes.all()] == ["ref_1"]
            assert (await wf.referral_codes.update("ref_1", label="New")).id == "ref_1"
            assert (await wf.referral_codes.stats("ref_1")).meta.has_more is False
        assert json.loads(rec.requests[2].content) == {"member_link": {"reference": "m"}}

    asyncio.run(run())
