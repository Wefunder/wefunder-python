"""operationId: cancelMemberLink — stop an unused link from opening the deal page (write:invite_links)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region cancelMemberLink
    link = wf.member_links.cancel("il_8kQm2xVb7nRt4WcY9pLe3HdA")
    print(link.attributes.state)  # "canceled"
    # endregion
    return link
