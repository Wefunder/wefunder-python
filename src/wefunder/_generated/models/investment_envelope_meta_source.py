from enum import StrEnum

class InvestmentEnvelopeMetaSource(StrEnum):
    CURRENT = "current"

    def __str__(self) -> str:
        return str(self.value)
