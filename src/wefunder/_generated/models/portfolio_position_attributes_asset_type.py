from enum import StrEnum

class PortfolioPositionAttributesAssetType(StrEnum):
    COMPANY = "company"
    FUND = "fund"

    def __str__(self) -> str:
        return str(self.value)
