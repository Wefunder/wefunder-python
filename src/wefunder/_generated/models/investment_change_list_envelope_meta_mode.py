from enum import StrEnum


class InvestmentChangeListEnvelopeMetaMode(StrEnum):
    BOOTSTRAP = "bootstrap"
    DELTA = "delta"

    def __str__(self) -> str:
        return str(self.value)
