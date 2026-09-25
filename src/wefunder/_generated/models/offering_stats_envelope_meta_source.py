from enum import StrEnum

class OfferingStatsEnvelopeMetaSource(StrEnum):
    PUBLISHED = "published"

    def __str__(self) -> str:
        return str(self.value)
