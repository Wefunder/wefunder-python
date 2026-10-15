from enum import StrEnum


class InviteLinkAttributesStatusType2Type1(StrEnum):
    INVESTED = "invested"
    OPENED = "opened"
    PENDING = "pending"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
