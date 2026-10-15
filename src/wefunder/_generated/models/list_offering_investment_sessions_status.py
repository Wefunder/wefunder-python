from enum import StrEnum


class ListOfferingInvestmentSessionsStatus(StrEnum):
    ABANDONED = "abandoned"
    CANCELED = "canceled"
    COMPLETED = "completed"
    EXPIRED = "expired"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
