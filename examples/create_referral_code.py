"""operationId: createReferralCode — mint a code with your app's server key (write:referral_codes; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createReferralCode
    code = wf.referral_codes.create(
        {
            "label": "October newsletter",
            "company_id": "co_7hQExampleCompany0001",  # omit to credit any company
            "utm": {"source": "newsletter", "campaign": "october"},
        }
    )
    print(code.id, code.attributes.link_parameter)  # e.g. "wfr=ref_…" — append to any wefunder.com link
    # endregion
    return code
