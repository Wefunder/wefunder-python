"""operationId: getReferralCode — one referral code by id (read:referral_codes; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getReferralCode
    code = wf.referral_codes.get("ref_7hQExampleCode00001")
    print(code.attributes.label, code.attributes.active)
    # endregion
    return code
