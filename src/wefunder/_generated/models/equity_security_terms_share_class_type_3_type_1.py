from enum import StrEnum


class EquitySecurityTermsShareClassType3Type1(StrEnum):
    COMMON = "common"
    PREFERRED = "preferred"

    def __str__(self) -> str:
        return str(self.value)
