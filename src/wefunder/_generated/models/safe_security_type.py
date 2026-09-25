from enum import StrEnum


class SafeSecurityType(StrEnum):
    SAFE = "safe"

    def __str__(self) -> str:
        return str(self.value)
