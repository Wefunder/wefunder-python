"""operationId: getOffering — one offering by its ofr_ id (read:public)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder, WefunderError


def example(wf: Wefunder, offering_id: str = "ofr_9m2ExampleRound00") -> Any:
    # region getOffering
    try:
        offering = wf.offerings.get(offering_id)
    except WefunderError as err:
        # 404 → err.type == "not_found"; err.request_id is what support asks for.
        print(err.status, err.type, err.request_id)
        raise
    print(offering.attributes.company_name, offering.attributes.status)
    # endregion
    return offering
