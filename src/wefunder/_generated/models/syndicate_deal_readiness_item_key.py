from enum import StrEnum


class SyndicateDealReadinessItemKey(StrEnum):
    ADVISOR = "advisor"
    ALLOCATION = "allocation"
    CARRY_AGREEMENTS = "carry_agreements"
    CONFLICT_DISCLOSURES = "conflict_disclosures"
    MASTER_LLC = "master_llc"
    SERIES = "series"
    SIGN_AND_OPEN = "sign_and_open"
    TARGET_COMPANY = "target_company"
    TERMS = "terms"

    def __str__(self) -> str:
        return str(self.value)
