from enum import StrEnum


class ListCompanyQuestionsSort(StrEnum):
    RECENT = "recent"
    RELEVANCE = "relevance"
    UNANSWERED = "unanswered"
    UPVOTED = "upvoted"

    def __str__(self) -> str:
        return str(self.value)
