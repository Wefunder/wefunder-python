from enum import StrEnum


class ListAttributedInvestmentsDetailLevel(StrEnum):
    ANONYMIZED = "anonymized"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
