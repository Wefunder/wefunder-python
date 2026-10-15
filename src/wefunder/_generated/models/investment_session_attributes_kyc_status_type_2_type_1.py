from enum import StrEnum


class InvestmentSessionAttributesKycStatusType2Type1(StrEnum):
    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
