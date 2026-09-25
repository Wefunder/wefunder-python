from enum import StrEnum

class AnonymizedAttributionStatusBucket(StrEnum):
    CANCELED = "canceled"
    CONFIRMED = "confirmed"
    DRAFT = "draft"
    IS_READY = "is_ready"
    NO_PAYMENT_YET = "no_payment_yet"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
