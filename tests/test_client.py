"""Hermetic client tests beyond the conformance vectors: wiring of the namespaces to the
generated ops (paths, query forwarding, enum coercion, envelope unwrapping) and the
`request()` escape hatch."""

from __future__ import annotations

import json
from typing import Any

import httpx
import pytest

from wefunder import API_VERSION_HEADER, AsyncWefunder, Wefunder, WefunderError


class Recorder:
    def __init__(self, respond: Any) -> None:
        self.requests: list[httpx.Request] = []
        self.respond = respond
        self.transport = httpx.MockTransport(self.handler)

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        body = self.respond(request) if callable(self.respond) else self.respond
        if isinstance(body, httpx.Response):
            return body
        return httpx.Response(200, json=body)


def test_default_host_version_header_and_bearer() -> None:
    rec = Recorder({"data": {"id": "usr_1", "type": "user", "attributes": {"name": "A"}}})
    wf = Wefunder(access_token="at_test_x", transport=rec.transport)
    me = wf.users.me()
    req = rec.requests[0]
    assert str(req.url) == "https://api.wefunder.com/users/me"
    assert req.headers[API_VERSION_HEADER] == "2025-01-15"
    assert req.headers["authorization"] == "Bearer at_test_x"
    assert wf.mode == "test"
    assert me.id == "usr_1" and me.attributes.name == "A"


def test_list_forwards_query_and_coerces_enum_strings() -> None:
    rec = Recorder({"data": [{"id": "ofr_1", "type": "offering"}], "meta": {"has_more": False, "next_cursor": None}})
    wf = Wefunder(access_token="at_test_x", transport=rec.transport)
    page = wf.offerings.list(sort="newest", testing_the_waters=True)
    q = rec.requests[0].url.params
    assert rec.requests[0].url.path == "/explore"
    assert q["sort"] == "newest" and q["testing_the_waters"] == "true"
    assert page.data[0].id == "ofr_1"


def test_all_preserves_query_across_pages_and_sends_cursor() -> None:
    def respond(request: httpx.Request) -> Any:
        if "cursor" in request.url.params:
            return {"data": [{"id": "ofr_2", "type": "offering"}], "meta": {"has_more": False, "next_cursor": None}}
        return {"data": [{"id": "ofr_1", "type": "offering"}], "meta": {"has_more": True, "next_cursor": 25}}

    rec = Recorder(respond)
    wf = Wefunder(access_token="at_test_x", transport=rec.transport)
    ids = [o.id for o in wf.offerings.all(sort="most_raised")]
    assert ids == ["ofr_1", "ofr_2"]
    assert [r.url.params.get("sort") for r in rec.requests] == ["most_raised", "most_raised"]
    assert rec.requests[1].url.params["cursor"] == "25"


def test_typed_error_from_envelope() -> None:
    rec = Recorder(
        httpx.Response(
            403,
            json={"error": {"type": "insufficient_scope", "message": "needs read:profile", "request_id": "req_body"}},
            headers={"x-wf-request-id": "req_header"},
        )
    )
    wf = Wefunder(access_token="at_test_x", transport=rec.transport)
    with pytest.raises(WefunderError) as info:
        wf.users.me()
    err = info.value
    assert (err.status, err.type, err.request_id) == (403, "insufficient_scope", "req_header")
    assert "insufficient_scope" in str(err) and "req_header" in str(err)


def test_webhook_endpoints_paths_and_bodies() -> None:
    def respond(request: httpx.Request) -> Any:
        if request.method == "DELETE":
            return {"data": {"id": "whe_1", "type": "webhook_endpoint", "removed": True}}
        if request.url.path == "/webhook_endpoints" and request.method == "GET":
            return {"data": [], "meta": {"count": 0, "quota": 10}}
        body = {
            "data": {
                "id": "whe_1",
                "type": "webhook_endpoint",
                "attributes": {"url": "https://e.com/h", "secret": "whsec_once"},
            }
        }
        created = request.method == "POST" and request.url.path == "/webhook_endpoints"
        return httpx.Response(201 if created else 200, json=body)  # create is documented as 201

    rec = Recorder(respond)
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    created = wf.webhook_endpoints.create(url="https://e.com/h", events=["offering.opened"], mode="live")
    assert created.attributes.secret == "whsec_once"
    assert json.loads(rec.requests[0].content) == {
        "url": "https://e.com/h",
        "events": ["offering.opened"],
        "mode": "live",
    }
    assert wf.webhook_endpoints.list().meta.quota == 10
    wf.webhook_endpoints.get("whe_1")
    wf.webhook_endpoints.update("whe_1", events=["investment.executed"])
    wf.webhook_endpoints.rotate_secret("whe_1")
    wf.webhook_endpoints.reenable("whe_1")
    wf.webhook_endpoints.test("whe_1", "offering.opened")
    wf.webhook_endpoints.test("whe_1")
    assert wf.webhook_endpoints.remove("whe_1").removed is True
    seen = [f"{r.method} {r.url.path}" for r in rec.requests[1:]]
    assert seen == [
        "GET /webhook_endpoints",
        "GET /webhook_endpoints/whe_1",
        "PATCH /webhook_endpoints/whe_1",
        "POST /webhook_endpoints/whe_1/rotate_secret",
        "POST /webhook_endpoints/whe_1/reenable",
        "POST /webhook_endpoints/whe_1/test",
        "POST /webhook_endpoints/whe_1/test",
        "DELETE /webhook_endpoints/whe_1",
    ]
    assert json.loads(rec.requests[3].content) == {"events": ["investment.executed"]}
    assert json.loads(rec.requests[6].content) == {"event": "offering.opened"}
    assert rec.requests[7].content == b""


def test_request_escape_hatch() -> None:
    rec = Recorder(lambda r: {"echo": json.loads(r.content), "path": r.url.path, "q": dict(r.url.params)})
    wf = Wefunder(access_token="at_test_x", transport=rec.transport)
    out = wf.request(
        "POST", "/partner/spvs", query={"dry_run": "1", "skip": None}, body={"a": 1}, headers={"Idempotency-Key": "k1"}
    )
    assert out == {"echo": {"a": 1}, "path": "/partner/spvs", "q": {"dry_run": "1"}}
    req = rec.requests[0]
    assert req.headers["idempotency-key"] == "k1"
    assert req.headers["content-type"] == "application/json"
    assert req.headers["authorization"] == "Bearer at_test_x"


def test_request_raises_typed_error() -> None:
    rec = Recorder(httpx.Response(404, json={"error": {"type": "not_found", "message": "nope", "request_id": "req_1"}}))
    wf = Wefunder(access_token="at_test_x", transport=rec.transport)
    with pytest.raises(WefunderError, match="not_found"):
        wf.request("GET", "/nothing")


def test_investments_delta_collect_stops_on_has_more() -> None:
    def respond(request: httpx.Request) -> Any:
        if "cursor" not in request.url.params:
            return {
                "data": [{"id": "inv_1", "visible": True, "observed_at": "2026-09-01T00:00:00Z"}],
                "meta": {"mode": "delta", "has_more": True, "next_cursor": "c1"},
            }
        return {
            "data": [{"id": "inv_2", "visible": False, "observed_at": "2026-09-02T00:00:00Z"}],
            "meta": {"mode": "delta", "has_more": False, "next_cursor": "c2"},
        }

    rec = Recorder(respond)
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    ids = [i.id for i in wf.investments.collect(company_id="co_1", updated_since="2026-09-01T00:00:00Z")]
    assert ids == ["inv_1", "inv_2"] and len(rec.requests) == 2
    q = rec.requests[1].url.params
    assert q["company_id"] == "co_1" and q["cursor"] == "c1" and q["updated_since"].startswith("2026-09-01")


async def test_async_client_mirrors_sync() -> None:
    def respond(request: httpx.Request) -> Any:
        if request.url.path == "/users/me":
            return {"data": {"id": "usr_1", "type": "user"}}
        if "cursor" in request.url.params:
            return {"data": [{"id": "ofr_2"}], "meta": {"has_more": False, "next_cursor": None}}
        return {"data": [{"id": "ofr_1"}], "meta": {"has_more": True, "next_cursor": 25}}

    rec = Recorder(respond)
    async with AsyncWefunder(access_token="at_test_x", transport=rec.transport) as wf:
        me = await wf.users.me()
        ids = [o.id async for o in wf.offerings.all(sort="newest")]
        out = await wf.request("GET", "/users/me")
    assert me.id == "usr_1" and ids == ["ofr_1", "ofr_2"] and out["data"]["id"] == "usr_1"
    assert rec.requests[0].headers["authorization"] == "Bearer at_test_x"


def test_requires_a_token() -> None:
    with pytest.raises(ValueError):
        Wefunder()
