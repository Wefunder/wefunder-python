from enum import StrEnum


class EquitySecurityType(StrEnum):
    EQUITY = "equity"

    def __str__(self) -> str:
        return str(self.value)
