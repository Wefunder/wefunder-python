from enum import StrEnum


class ReferralCodeStatsCompanyLevel(StrEnum):
    ANONYMIZED = "anonymized"
    COUNTS = "counts"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
