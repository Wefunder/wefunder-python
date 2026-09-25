from enum import StrEnum

class FundSecurityType(StrEnum):
    FUND = "fund"

    def __str__(self) -> str:
        return str(self.value)
