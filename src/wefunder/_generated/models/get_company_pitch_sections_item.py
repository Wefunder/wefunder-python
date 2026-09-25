from enum import StrEnum


class GetCompanyPitchSectionsItem(StrEnum):
    PERKS = "perks"
    STORY = "story"

    def __str__(self) -> str:
        return str(self.value)
