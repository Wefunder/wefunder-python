from enum import StrEnum

class RevenueShareSecurityType(StrEnum):
    REVENUE_SHARE = "revenue_share"

    def __str__(self) -> str:
        return str(self.value)
