"""operationId: listInvestmentSessions — every investment session your app created (read:investment_sessions; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listInvestmentSessions
    for session in wf.investment_sessions.all(status="in_progress"):
        print(session.id, session.attributes.status)
    # endregion
    return None
