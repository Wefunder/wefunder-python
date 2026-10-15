from enum import StrEnum


class OfferingListEnvelopeMetaStatus(StrEnum):
    ALL = "all"
    CLOSED = "closed"
    LIVE = "live"

    def __str__(self) -> str:
        return str(self.value)
