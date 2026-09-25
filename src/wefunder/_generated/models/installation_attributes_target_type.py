from enum import StrEnum

class InstallationAttributesTargetType(StrEnum):
    COMPANY = "company"
    SYNDICATE = "syndicate"

    def __str__(self) -> str:
        return str(self.value)
