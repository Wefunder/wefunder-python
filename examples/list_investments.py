"""operationId: listInvestments — the Investment Delta API (read:investments)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listInvestments
    # First sync: no cursor. Persist meta.next_cursor after EVERY page — it is always
    # present, even on the last one — and pass it back next time for only what changed.
    page = wf.investments.list(company_id="co_abc123Example")
    for record in page.data:
        print(record.id, record.visible)
    checkpoint = page.meta.next_cursor

    # Or let the SDK walk every page (stops on has_more=false):
    changed = wf.investments.collect(company_id="co_abc123Example", updated_since="2026-09-01T00:00:00Z")
    # endregion
    return page, checkpoint, changed
