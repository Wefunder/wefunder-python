from enum import StrEnum


class RevenueShareSecurityTermsRevenueBasisType1(StrEnum):
    GROSS = "gross"
    NET = "net"

    def __str__(self) -> str:
        return str(self.value)
