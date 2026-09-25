from enum import StrEnum


class SpvSettingsAccreditationType(StrEnum):
    SELF_ATTESTATION = "self_attestation"
    VERIFIED = "verified"

    def __str__(self) -> str:
        return str(self.value)
