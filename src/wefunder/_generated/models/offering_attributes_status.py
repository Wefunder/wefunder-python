from enum import StrEnum


class OfferingAttributesStatus(StrEnum):
    CANCELED = "canceled"
    CLOSED = "closed"
    OPEN = "open"
    UPCOMING = "upcoming"

    def __str__(self) -> str:
        return str(self.value)
