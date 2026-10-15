"""operationId: getReferralCodeStats — weekly cohorts per company for one code (read:referral_codes; beta)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getReferralCodeStats
    stats = wf.referral_codes.stats("ref_7hQExampleCode00001")
    for company in stats.data.attributes.companies:
        print(company.company, company.level, len(company.weeks), "weekly cohort(s)")
    # endregion
    return stats
