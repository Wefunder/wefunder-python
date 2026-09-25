from enum import StrEnum


class CreatePartnerInviteBodyDirection(StrEnum):
    FOUNDER_TO_PARTNER = "founder_to_partner"
    PARTNER_TO_FOUNDER = "partner_to_founder"

    def __str__(self) -> str:
        return str(self.value)
