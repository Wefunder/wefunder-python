"""operationId: listOfferings — the public discovery feed (read:public)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listOfferings
    # Browse live offerings, sorted. The cursor is opaque and handled for you.
    page = wf.offerings.list(sort="most_raised")
    for offering in page.data:
        print(offering.id, offering.attributes.company_name)

    # Or stream every offering lazily, one page fetched at a time:
    for offering in wf.offerings.all(sort="newest"):
        print(offering.id)
    # endregion
    return page
