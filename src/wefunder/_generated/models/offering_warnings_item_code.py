from enum import StrEnum

class OfferingWarningsItemCode(StrEnum):
    CONCURRENT_ROUNDS = "concurrent_rounds"
    PRIOR_ROUNDS = "prior_rounds"

    def __str__(self) -> str:
        return str(self.value)
