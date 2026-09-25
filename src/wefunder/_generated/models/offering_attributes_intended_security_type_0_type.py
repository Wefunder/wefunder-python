from enum import StrEnum

class OfferingAttributesIntendedSecurityType0Type(StrEnum):
    CONVERTIBLE_NOTE = "convertible_note"
    DEBT = "debt"
    EQUITY = "equity"
    FUND = "fund"
    REVENUE_SHARE = "revenue_share"
    SAFE = "safe"

    def __str__(self) -> str:
        return str(self.value)
