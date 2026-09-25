from enum import StrEnum

class ListOfferingsSort(StrEnum):
    CLOSING_SOON = "closing_soon"
    MOST_INVESTORS = "most_investors"
    MOST_RAISED = "most_raised"
    NEWEST = "newest"

    def __str__(self) -> str:
        return str(self.value)
