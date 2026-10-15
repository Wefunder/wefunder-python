from enum import StrEnum


class SyndicateDealReadinessEnvelopeDataAttributesStatus(StrEnum):
    CANCELED = "canceled"
    CLOSED = "closed"
    OPEN = "open"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
