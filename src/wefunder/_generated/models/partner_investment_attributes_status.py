from enum import StrEnum

class PartnerInvestmentAttributesStatus(StrEnum):
    AWAITING_PAYMENT = "awaiting_payment"
    CANCELED = "canceled"
    CONFIRMED = "confirmed"
    PENDING = "pending"
    PENDING_ACCREDITATION = "pending_accreditation"

    def __str__(self) -> str:
        return str(self.value)
