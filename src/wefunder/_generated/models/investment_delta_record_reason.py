from enum import StrEnum

class InvestmentDeltaRecordReason(StrEnum):
    CHANGED = "changed"
    INVESTOR_DEACTIVATED = "investor_deactivated"
    REPROJECTED = "reprojected"

    def __str__(self) -> str:
        return str(self.value)
