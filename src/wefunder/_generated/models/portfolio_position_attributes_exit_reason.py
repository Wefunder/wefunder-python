from enum import StrEnum


class PortfolioPositionAttributesExitReason(StrEnum):
    ACQUISITION = "acquisition"
    BUYBACK = "buyback"
    FAILED = "failed"
    IPO = "ipo"
    WINDING_DOWN = "winding_down"

    def __str__(self) -> str:
        return str(self.value)
