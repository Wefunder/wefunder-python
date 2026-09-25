from enum import StrEnum


class SpvTermsStructure(StrEnum):
    CONVERTIBLE_NOTE = "convertible_note"
    EQUITY = "equity"
    SAFE = "safe"

    def __str__(self) -> str:
        return str(self.value)
