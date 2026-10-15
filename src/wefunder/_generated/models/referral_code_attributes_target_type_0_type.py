from enum import StrEnum


class ReferralCodeAttributesTargetType0Type(StrEnum):
    COMPANY = "company"
    OFFERING = "offering"

    def __str__(self) -> str:
        return str(self.value)
