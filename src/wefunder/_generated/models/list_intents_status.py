from enum import StrEnum


class ListIntentsStatus(StrEnum):
    APPROVED = "approved"
    EXECUTED = "executed"
    EXPIRED = "expired"
    FAILED = "failed"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
