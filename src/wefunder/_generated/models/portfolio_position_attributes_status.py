from enum import StrEnum

class PortfolioPositionAttributesStatus(StrEnum):
    ACTIVE = "active"
    EXITED = "exited"
    FAILED = "failed"
    SOLD = "sold"

    def __str__(self) -> str:
        return str(self.value)
