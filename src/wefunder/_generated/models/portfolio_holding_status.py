from enum import StrEnum


class PortfolioHoldingStatus(StrEnum):
    ACTIVE = "active"
    EXITED = "exited"
    FAILED = "failed"

    def __str__(self) -> str:
        return str(self.value)
