from enum import StrEnum


class ListSyndicateMembersSort(StrEnum):
    ALPHABETICAL = "alphabetical"
    INVESTMENT_AMOUNT = "investment_amount"
    LAST_ACTIVITY = "last_activity"
    NEWEST = "newest"
    OLDEST = "oldest"

    def __str__(self) -> str:
        return str(self.value)
