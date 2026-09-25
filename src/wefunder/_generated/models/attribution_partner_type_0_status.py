from enum import StrEnum

class AttributionPartnerType0Status(StrEnum):
    APPROVED = "approved"
    PENDING = "pending"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
