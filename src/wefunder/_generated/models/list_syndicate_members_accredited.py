from enum import StrEnum


class ListSyndicateMembersAccredited(StrEnum):
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
