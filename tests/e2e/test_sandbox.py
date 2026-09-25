"""Live sandbox E2E — needs WEFUNDER_CLIENT_ID / WEFUNDER_CLIENT_SECRET (a pk_test_ app).
Excluded from the default `pytest` run (pyproject addopts); run with `pytest tests/e2e`.
Asserts contract shape and paginator invariants, not data (a fresh realm may have no offerings)."""

from __future__ import annotations

import os

import pytest

from wefunder import Wefunder, WefunderError

CLIENT_ID = os.environ.get("WEFUNDER_CLIENT_ID")
CLIENT_SECRET = os.environ.get("WEFUNDER_CLIENT_SECRET")

pytestmark = pytest.mark.skipif(not (CLIENT_ID and CLIENT_SECRET), reason="sandbox credentials not set")


@pytest.fixture(scope="module")
def wf() -> Wefunder:
    assert CLIENT_ID and CLIENT_SECRET
    return Wefunder.from_client_credentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, scopes=["read:public"])


def test_mints_a_test_mode_token_at_the_gateway(wf: Wefunder) -> None:
    assert wf.mode == "test"
    assert wf.tokens.access_token.startswith("at_test_")


def test_offerings_list_has_the_envelope_shape(wf: Wefunder) -> None:
    page = wf.offerings.list()
    assert isinstance(page.data, list)
    assert page.meta is not None


def test_paginator_terminates_without_duplicates(wf: Wefunder) -> None:
    ids = [o.id for o in wf.offerings.all()]
    assert len(ids) == len(set(ids))


def test_scope_error_is_typed_and_carries_a_request_id(wf: Wefunder) -> None:
    with pytest.raises(WefunderError) as info:
        wf.users.me()  # needs read:profile; a cc token holds only read:public
    assert info.value.status == 403
    assert info.value.request_id


def test_unknown_offering_is_a_typed_error(wf: Wefunder) -> None:
    with pytest.raises(WefunderError) as info:
        wf.offerings.get("ofr_doesnotexist000000")
    assert info.value.status in (404, 400)
    assert info.value.request_id
