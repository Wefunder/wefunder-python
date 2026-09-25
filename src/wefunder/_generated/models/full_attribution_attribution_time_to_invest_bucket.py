from enum import StrEnum


class FullAttributionAttributionTimeToInvestBucket(StrEnum):
    ASSISTED = "assisted"
    DELAYED = "delayed"
    DIRECT = "direct"

    def __str__(self) -> str:
        return str(self.value)
