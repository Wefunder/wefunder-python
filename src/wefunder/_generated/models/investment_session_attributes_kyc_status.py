from enum import StrEnum


class InvestmentSessionAttributesKycStatus(StrEnum):
    FAILED = "failed"
    PASSED = "passed"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
