from enum import StrEnum

class AnonymizedAttributionAttributionQualityScore(StrEnum):
    HIGH = "high"
    LOW = "low"
    MEDIUM = "medium"
    SUSPICIOUS = "suspicious"

    def __str__(self) -> str:
        return str(self.value)
