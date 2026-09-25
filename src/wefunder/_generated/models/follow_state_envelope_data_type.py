from enum import StrEnum

class FollowStateEnvelopeDataType(StrEnum):
    FOLLOW_STATE = "follow_state"

    def __str__(self) -> str:
        return str(self.value)
