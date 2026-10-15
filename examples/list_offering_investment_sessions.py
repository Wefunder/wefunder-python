"""operationId: listOfferingInvestmentSessions — one offering's investment sessions (read:investment_sessions; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listOfferingInvestmentSessions
    page = wf.investment_sessions.list_for_offering("ofr_2nVb8KxQ4tLm9RcW7pHs3FdY", status="completed")
    for session in page.data:
        print(session.id, session.attributes.status)
    # endregion
    return page
