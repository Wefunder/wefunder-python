"""operationId: listCompanyInvestmentChanges — the company-scoped Investment Delta feed
(read:investments or read:companies; the user must be able to edit the company)."""

from __future__ import annotations

from wefunder import Wefunder
from wefunder._generated.api.investment_delta import list_company_investment_changes


def example(wf: Wefunder, company_id: str = "co_abc123Example") -> str | None:
    # region listCompanyInvestmentChanges
    # Walk every change for one company. Persist meta.next_cursor after each page — it is
    # always present, even on the last page — and pass it back next sync for only what changed.
    cursor: str | None = None
    while True:
        page = wf.call(list_company_investment_changes, company_id=company_id, cursor=cursor, per_page=50)
        for record in page.data:
            print(record.id, record.visible)
        cursor = page.meta.next_cursor
        if not page.meta.has_more:
            break
    # endregion
    return cursor
