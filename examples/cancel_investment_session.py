"""operationId: cancelInvestmentSession — cancel a session the recipient has not completed
(write:investment_sessions; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region cancelInvestmentSession
    session = wf.investment_sessions.cancel("is_7hQExampleSession001")
    print(session.attributes.status)  # "canceled"
    # endregion
    return session
