"""operationId: listReferralCodes — your app's referral codes (read:referral_codes; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region listReferralCodes
    for code in wf.referral_codes.all(active=True):
        print(code.id, code.attributes.label)
    # endregion
    return None
