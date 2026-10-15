"""operationId: getInvestmentSession — one investment session by id (read:investment_sessions; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getInvestmentSession
    session = wf.investment_sessions.get("is_7hQExampleSession001")
    print(session.attributes.status)
    # endregion
    return session
