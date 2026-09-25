from enum import StrEnum

class DebtSecurityType(StrEnum):
    DEBT = "debt"

    def __str__(self) -> str:
        return str(self.value)
