from enum import StrEnum

class IntentAttributesStatus(StrEnum):
    APPROVED = "approved"
    EXECUTED = "executed"
    EXECUTING = "executing"
    EXPIRED = "expired"
    FAILED = "failed"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
