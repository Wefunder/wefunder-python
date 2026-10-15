"""operationId: listSyndicateJoinSessions — your syndicate's join sessions (read:syndicates; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listSyndicateJoinSessions
    for session in wf.join_sessions.all("syn_aB3xQ9k2vF8mNp1zT5wY7Qc4"):
        print(session["id"], session["attributes"]["status"], session["attributes"]["email"])
    # endregion
    return None
