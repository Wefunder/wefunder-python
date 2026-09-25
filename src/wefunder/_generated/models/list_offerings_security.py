from enum import StrEnum


class ListOfferingsSecurity(StrEnum):
    CONVERTIBLE_NOTE = "convertible_note"
    DEBT = "debt"
    EQUITY = "equity"
    FUND = "fund"
    OTHER = "other"
    REVENUE_SHARE = "revenue_share"
    SAFE = "safe"

    def __str__(self) -> str:
        return str(self.value)
