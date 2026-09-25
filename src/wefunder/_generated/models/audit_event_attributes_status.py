from enum import StrEnum

class AuditEventAttributesStatus(StrEnum):
    DENIED = "denied"
    FAILURE = "failure"
    SUCCESS = "success"

    def __str__(self) -> str:
        return str(self.value)
