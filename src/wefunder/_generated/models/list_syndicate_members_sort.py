from enum import StrEnum


class ListSyndicateMembersSort(StrEnum):
    ALPHABETICAL = "alphabetical"
    LAST_ACTIVITY = "last_activity"
    NEWEST = "newest"
    OLDEST = "oldest"
    RELEVANCE = "relevance"

    def __str__(self) -> str:
        return str(self.value)
