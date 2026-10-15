"""operationId: listOfferingMemberLinks — your app's member links on one offering (read:invite_links)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listOfferingMemberLinks
    for link in wf.member_links.all("ofr_2nVb8KxQ4tLm9RcW7pHs3FdY"):
        print(link.id, link.attributes.reference, link.attributes.state)
    # endregion
    return None
