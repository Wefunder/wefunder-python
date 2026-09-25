from enum import StrEnum


class InvestmentListEnvelopeMetaMode(StrEnum):
    BOOTSTRAP = "bootstrap"
    DELTA = "delta"

    def __str__(self) -> str:
        return str(self.value)
