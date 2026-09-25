from enum import StrEnum


class AttributedInvestmentListEnvelopeMetaDetailLevel(StrEnum):
    ANONYMIZED = "anonymized"
    FULL = "full"

    def __str__(self) -> str:
        return str(self.value)
