"""operationId: updateReferralCode — relabel, retarget UTM, or deactivate a code (write:referral_codes; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region updateReferralCode
    code = wf.referral_codes.update("ref_7hQExampleCode00001", active=False)
    print(code.attributes.active)  # False — the link keeps resolving, nothing new is credited
    # endregion
    return code
