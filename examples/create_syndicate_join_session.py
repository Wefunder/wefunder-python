"""operationId: createSyndicateJoinSession — mint a hosted join session for one person
(write:syndicate_members; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createSyndicateJoinSession
    session = wf.join_sessions.create(
        "syn_aB3xQ9k2vF8mNp1zT5wY7Qc4",
        {
            "email": "member@example.com",
            "name": "Ada Example",
            "require_approval": True,
            "success_url": "https://yourapp.example/joined",
        },
    )
    print(session["attributes"]["url"])  # send the person here; the outcome arrives as join_session.* webhooks
    # endregion
    return session
