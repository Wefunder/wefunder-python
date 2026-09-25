from enum import StrEnum

class AnonymizedAttributionAmountTier(StrEnum):
    LARGE = "large"
    MEDIUM = "medium"
    SMALL = "small"

    def __str__(self) -> str:
        return str(self.value)
