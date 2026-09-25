from enum import StrEnum

class ListInvestmentsStatus(StrEnum):
    ACTIVE = "active"
    CANCELED = "canceled"
    CONVERTED = "converted"
    EXECUTED = "executed"
    RESERVED = "reserved"

    def __str__(self) -> str:
        return str(self.value)
