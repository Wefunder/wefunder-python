from enum import StrEnum


class CreateSyndicateJoinSessionBodyJoinSessionMode(StrEnum):
    HOSTED = "hosted"

    def __str__(self) -> str:
        return str(self.value)
