from enum import StrEnum


class PartnerInvestmentAttributesAccreditationType0Type(StrEnum):
    SELF_ATTESTATION = "self_attestation"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
