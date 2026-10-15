"""operationId: createOfferingMemberLink — mint a member's link to one deal page (write:invite_links)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createOfferingMemberLink
    # `reference` is your member id. Repeating it returns the live link instead of a second one;
    # the idempotency key makes a retried request safe as well.
    link = wf.member_links.create(
        "ofr_2nVb8KxQ4tLm9RcW7pHs3FdY",
        {"reference": "member_8812"},
        idempotency_key="member_8812-ofr_2nVb8KxQ4tLm9RcW7pHs3FdY",
    )
    print(link.attributes.url)  # send this to the member; it carries no email
    # endregion
    return link
