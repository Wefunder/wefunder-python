from enum import StrEnum


class InvestmentDeltaRecordReasonType1(StrEnum):
    CHANGED = "changed"
    INVESTOR_DEACTIVATED = "investor_deactivated"
    RECOMPUTED = "recomputed"
    REPROJECTED = "reprojected"

    def __str__(self) -> str:
        return str(self.value)
