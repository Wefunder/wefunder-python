from enum import StrEnum


class SyndicateDealReadinessEnvelopeDataType(StrEnum):
    SYNDICATE_DEAL_READINESS = "syndicate_deal_readiness"

    def __str__(self) -> str:
        return str(self.value)
