from enum import StrEnum


class GetPortfolioStatus(StrEnum):
    ACTIVE = "active"
    EXITED = "exited"
    FAILED = "failed"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
