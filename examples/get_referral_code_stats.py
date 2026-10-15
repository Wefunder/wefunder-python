"""operationId: getReferralCodeStats — what one code produced, per company (read:referral_codes; beta).
Each company's `level` decides the shape: `counts` carries weekly cohorts in `weeks`; `anonymized` and
`full` carry per-investment rows in `investments` instead (`full` includes investor names and emails
and needs a founder-tier installation grant on that company)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region getReferralCodeStats
    stats = wf.referral_codes.stats("ref_7hQExampleCode00001")
    for company in stats.data.attributes.companies:
        if company.level == "counts":
            print(company.company, len(company.weeks), "weekly cohort(s)")
        else:
            print(company.company, company.level, len(company.investments), "investment row(s)")
    # endregion
    return stats
