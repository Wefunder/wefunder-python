from enum import StrEnum


class InstallationAttributesStatus(StrEnum):
    ACTIVE = "active"
    REVOKED = "revoked"

    def __str__(self) -> str:
        return str(self.value)
