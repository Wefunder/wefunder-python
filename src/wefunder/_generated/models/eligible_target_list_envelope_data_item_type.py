from enum import StrEnum


class EligibleTargetListEnvelopeDataItemType(StrEnum):
    COMPANY = "company"
    SYNDICATE = "syndicate"

    def __str__(self) -> str:
        return str(self.value)
