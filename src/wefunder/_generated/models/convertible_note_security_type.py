from enum import StrEnum

class ConvertibleNoteSecurityType(StrEnum):
    CONVERTIBLE_NOTE = "convertible_note"

    def __str__(self) -> str:
        return str(self.value)
