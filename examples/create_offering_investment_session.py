"""operationId: createOfferingInvestmentSession — put a known investor into checkout for one offering
(write:investment_sessions; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createOfferingInvestmentSession
    session = wf.investment_sessions.create(
        "ofr_2nVb8KxQ4tLm9RcW7pHs3FdY",
        {"email": "investor@example.com", "allocation_cents": 250000, "success_url": "https://yourapp.example/thanks"},
        idempotency_key="investor@example.com-ofr_2nVb8KxQ4tLm9RcW7pHs3FdY",
    )
    print(session.attributes.url)  # hand this to the investor
    # endregion
    return session
