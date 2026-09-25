from enum import StrEnum


class ListPortfolioPositionsStatus(StrEnum):
    ACTIVE = "active"
    EXITED = "exited"
    FAILED = "failed"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
