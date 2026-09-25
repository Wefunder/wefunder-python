from enum import StrEnum


class SpvAttributesStatus(StrEnum):
    CANCELED = "canceled"
    CLOSED = "closed"
    CLOSING = "closing"
    DISSOLVED = "dissolved"
    DRAFT = "draft"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
