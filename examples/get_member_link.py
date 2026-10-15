"""operationId: getMemberLink — what the member did with their link (read:invite_links)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getMemberLink
    link = wf.member_links.get("il_8kQm2xVb7nRt4WcY9pLe3HdA")
    print(link.attributes.state, link.attributes.wefunder_user_id, link.attributes.investment_id)
    # endregion
    return link
