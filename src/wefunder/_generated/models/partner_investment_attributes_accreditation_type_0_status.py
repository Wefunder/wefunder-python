from enum import StrEnum


class PartnerInvestmentAttributesAccreditationType0Status(StrEnum):
    EXPIRED = "expired"
    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
