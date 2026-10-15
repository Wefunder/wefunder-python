from enum import StrEnum


class CreateSyndicateJoinSessionBodyJoinSessionDisplay(StrEnum):
    POPUP = "popup"
    REDIRECT = "redirect"

    def __str__(self) -> str:
        return str(self.value)
