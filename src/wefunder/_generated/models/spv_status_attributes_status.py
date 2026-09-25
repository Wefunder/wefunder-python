from enum import StrEnum


class SpvStatusAttributesStatus(StrEnum):
    CANCELED = "canceled"
    CLOSED = "closed"
    CLOSING = "closing"
    DRAFT = "draft"
    OPEN = "open"

    def __str__(self) -> str:
        return str(self.value)
