"""`wf.installations` (sync + async): paths, bodies, envelope handling, and the already-installed
fallback (409 already_installed → mint for details.installation, same scopes)."""

from __future__ import annotations

import asyncio
import json
from typing import Any

import httpx
import pytest

from wefunder import AsyncWefunder, Wefunder, WefunderError

INSTALL = {
    "id": "ins_1",
    "type": "installation",
    "attributes": {"target": {"type": "syndicate", "id": "syn_1"}, "status": "active", "scopes": ["read:syndicates"]},
}


class Recorder:
    def __init__(self, respond: Any) -> None:
        self.requests: list[httpx.Request] = []
        self.respond = respond
        self.transport = httpx.MockTransport(self.handler)

    def handler(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        body = self.respond(request) if callable(self.respond) else self.respond
        return body if isinstance(body, httpx.Response) else httpx.Response(200, json=body)

    @property
    def seen(self) -> list[str]:
        return [f"{r.method} {r.url.path}" for r in self.requests]


def already_installed(request: httpx.Request) -> httpx.Response:
    if request.url.path == "/installations":
        return httpx.Response(
            409,
            json={
                "error": {
                    "type": "already_installed",
                    "message": "already",
                    "details": {"installation": "ins_existing"},
                    "request_id": "req_1",
                }
            },
        )
    if request.url.path == "/installations/ins_existing/tokens":
        return httpx.Response(
            201, json={"data": {**INSTALL, "id": "ins_existing"}, "token": {"access_token": "at_live_MINT"}}
        )
    raise AssertionError(f"unexpected {request.url.path}")


def test_eligible_targets_forwards_target_type_and_returns_rows() -> None:
    rec = Recorder(
        lambda r: (
            {"data": [{"type": "company", "id": "co_1", "name": "Acme", "installed": False}]}
            if r.url.params.get("target_type") == "company"
            else {"data": []}
        )
    )
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    rows = wf.installations.eligible_targets("company")
    assert rec.requests[0].url.path == "/installations/eligible"
    assert [r.id for r in rows] == ["co_1"]
    assert wf.installations.eligible_targets("syndicate") == []  # an investor's empty list is not an error
    assert wf.installations.eligible_targets() == []
    assert "target_type" not in rec.requests[2].url.params


def test_list_get_revoke_paths_and_envelopes() -> None:
    def respond(request: httpx.Request) -> Any:
        if request.method == "DELETE":
            return {"data": {**INSTALL, "attributes": {**INSTALL["attributes"], "status": "revoked"}}}
        if request.url.path == "/installations":
            return {"data": [INSTALL], "meta": {"count": 1}}
        return {"data": INSTALL}

    rec = Recorder(respond)
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    assert wf.installations.list().meta.count == 1
    assert wf.installations.get("ins_1").id == "ins_1"
    assert wf.installations.revoke("ins_1").attributes.status == "revoked"
    assert rec.seen == ["GET /installations", "GET /installations/ins_1", "DELETE /installations/ins_1"]


def test_create_posts_body_and_keeps_the_one_time_token_beside_data() -> None:
    rec = Recorder(httpx.Response(201, json={"data": INSTALL, "token": {"access_token": "at_live_INSTALL"}}))
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    created = wf.installations.create({"target_type": "syndicate", "target_id": "syn_1", "scopes": ["read:syndicates"]})
    assert rec.seen == ["POST /installations"]
    assert json.loads(rec.requests[0].content) == {
        "target_type": "syndicate",
        "target_id": "syn_1",
        "scopes": ["read:syndicates"],
    }
    assert created.data.id == "ins_1"
    assert created.token.access_token == "at_live_INSTALL"


def test_mint_token_sends_scopes_when_given_and_no_body_when_omitted() -> None:
    rec = Recorder(httpx.Response(201, json={"data": INSTALL, "token": {"access_token": "at_live_MINT"}}))
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    wf.installations.mint_token("ins_1", ["read:investments"])
    wf.installations.mint_token("ins_1")
    wf.installations.mint_token("ins_1", [])  # explicit [] is a real body: it grants nothing
    assert rec.seen == ["POST /installations/ins_1/tokens"] * 3
    assert json.loads(rec.requests[0].content) == {"scopes": ["read:investments"]}
    assert rec.requests[1].content == b""
    assert json.loads(rec.requests[2].content) == {"scopes": []}


def test_install_or_mint_token_falls_back_to_the_existing_install_with_the_same_scopes() -> None:
    rec = Recorder(already_installed)
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    result = wf.installations.install_or_mint_token(
        {"target_type": "syndicate", "target_id": "syn_1", "scopes": ["read:syndicates"]}
    )
    assert result.token.access_token == "at_live_MINT"
    assert rec.seen == ["POST /installations", "POST /installations/ins_existing/tokens"]
    assert json.loads(rec.requests[1].content) == {"scopes": ["read:syndicates"]}


def test_install_or_mint_token_fresh_install_makes_one_call() -> None:
    rec = Recorder(httpx.Response(201, json={"data": INSTALL, "token": {"access_token": "at_live_NEW"}}))
    wf = Wefunder(access_token="at_live_x", transport=rec.transport)
    result = wf.installations.install_or_mint_token({"target_type": "syndicate", "target_id": "syn_1"})
    assert result.token.access_token == "at_live_NEW"
    assert rec.seen == ["POST /installations"]


def test_install_or_mint_token_other_errors_still_raise() -> None:
    revoked = Recorder(
        httpx.Response(409, json={"error": {"type": "installation_revoked", "message": "revoked", "request_id": "r"}})
    )
    with pytest.raises(WefunderError) as info:
        Wefunder(access_token="at_live_x", transport=revoked.transport).installations.install_or_mint_token(
            {"target_type": "syndicate", "target_id": "syn_1"}
        )
    assert (info.value.status, info.value.type) == (409, "installation_revoked")

    no_details = Recorder(httpx.Response(409, json={"error": {"type": "already_installed", "message": "already"}}))
    with pytest.raises(WefunderError) as info:
        Wefunder(access_token="at_live_x", transport=no_details.transport).installations.install_or_mint_token(
            {"target_type": "syndicate", "target_id": "syn_1"}
        )
    assert info.value.type == "already_installed"
    assert no_details.seen == ["POST /installations"]


def test_async_namespace_mirrors_sync() -> None:
    async def run() -> None:
        rec = Recorder(already_installed)
        async with AsyncWefunder(access_token="at_live_x", transport=rec.transport) as wf:
            result = await wf.installations.install_or_mint_token(
                {"target_type": "syndicate", "target_id": "syn_1", "scopes": ["read:syndicates"]}
            )
            assert result.token.access_token == "at_live_MINT"
            assert json.loads(rec.requests[1].content) == {"scopes": ["read:syndicates"]}

        rec2 = Recorder(
            lambda r: {"data": [INSTALL], "meta": {"count": 1}} if r.url.path == "/installations" else {"data": []}
        )
        async with AsyncWefunder(access_token="at_live_x", transport=rec2.transport) as wf:
            assert (await wf.installations.list()).meta.count == 1
            assert await wf.installations.eligible_targets("syndicate") == []
        assert rec2.seen == ["GET /installations", "GET /installations/eligible"]

    asyncio.run(run())
