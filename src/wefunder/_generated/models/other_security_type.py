from enum import StrEnum

class OtherSecurityType(StrEnum):
    OTHER = "other"

    def __str__(self) -> str:
        return str(self.value)
