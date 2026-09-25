from enum import StrEnum

class AnonymizedAttributionAttributionTimeToInvestBucket(StrEnum):
    ASSISTED = "assisted"
    DELAYED = "delayed"
    DIRECT = "direct"

    def __str__(self) -> str:
        return str(self.value)
