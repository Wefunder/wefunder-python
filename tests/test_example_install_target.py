"""The install-target guide must survive the API's "already installed" answer: create_installation
returns 409 already_installed (details.installation = the existing id) and the example has to mint a
token for THAT install and continue — not surface the 409. (Review finding on PR #1.)"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import httpx
import pytest

from wefunder import Wefunder, WefunderError

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "examples"))
from install_target import example  # noqa: E402


class Api:
    def __init__(self, create_response: httpx.Response) -> None:
        self.create_response = create_response
        self.bodies: list[str] = []
        self.seen: list[str] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.seen.append(f"{request.method} {request.url.path} {request.headers.get('authorization')}")
        self.bodies.append(request.content.decode())
        path = request.url.path
        if path == "/installations/eligible":
            return httpx.Response(
                200, json={"data": [{"type": "syndicate", "id": "syn_1", "name": "Ex", "installed": True}]}
            )
        if path == "/installations" and request.method == "POST":
            return self.create_response
        if path == "/installations/ins_existing/tokens":
            return httpx.Response(
                201, json={"data": {"id": "ins_existing"}, "token": {"access_token": "at_live_INSTALL"}}
            )
        if path == "/syndicates/syn_1/deals":
            return httpx.Response(200, json={"data": [{"id": "deal_1"}], "meta": {}})
        raise AssertionError(f"unexpected {request.method} {path}")


def test_already_installed_mints_for_the_existing_install_and_continues(monkeypatch: pytest.MonkeyPatch) -> None:
    api = Api(
        httpx.Response(
            409,
            json={
                "error": {
                    "type": "already_installed",
                    "message": "This app is already installed here",
                    "details": {"installation": "ins_existing"},
                    "request_id": "req_1",
                }
            },
        )
    )
    # The example builds a SECOND client for the installation token with Wefunder(access_token=…),
    # which would use a real HTTP transport — route that through the same fake.
    monkeypatch.setattr("wefunder.client.httpx.HTTPTransport", lambda: httpx.MockTransport(api))
    wf = Wefunder(access_token="at_live_USER", transport=httpx.MockTransport(api))

    deals = example(wf, "syn_1")

    assert [d.id for d in deals.data] == ["deal_1"]
    assert api.seen == [
        "GET /installations/eligible Bearer at_live_USER",
        "POST /installations Bearer at_live_USER",
        "POST /installations/ins_existing/tokens Bearer at_live_USER",
        "GET /syndicates/syn_1/deals Bearer at_live_INSTALL",  # the deals call runs AS the installation
    ]
    # The mint for the existing install asks for the SAME read-only scope as the install itself.
    assert json.loads(api.bodies[2]) == {"scopes": ["read:syndicates"]}


def test_other_409_still_raises() -> None:
    api = Api(
        httpx.Response(409, json={"error": {"type": "installation_revoked", "message": "revoked", "request_id": "r"}})
    )
    wf = Wefunder(access_token="at_live_USER", transport=httpx.MockTransport(api))
    with pytest.raises(WefunderError) as info:
        example(wf, "syn_1")
    assert (info.value.status, info.value.type) == (409, "installation_revoked")
