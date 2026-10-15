"""operationId: getSyndicateJoinSession — the state of one join session (read:syndicates; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getSyndicateJoinSession
    session = wf.join_sessions.get("syn_aB3xQ9k2vF8mNp1zT5wY7Qc4", "js_7hQExampleSession001")
    print(session["attributes"]["status"], session["attributes"]["ineligible_reason"])
    # endregion
    return session
