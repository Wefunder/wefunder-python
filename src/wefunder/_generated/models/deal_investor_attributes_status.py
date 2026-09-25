from enum import StrEnum


class DealInvestorAttributesStatus(StrEnum):
    CONFIRMED = "confirmed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
