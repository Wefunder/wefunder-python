from enum import StrEnum


class InvestmentSessionAttributesKycStatusType1(StrEnum):
    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
