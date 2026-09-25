from enum import StrEnum


class CompanyUpdateAttributesVisibilityType3Type1(StrEnum):
    COMMUNITY = "community"
    FOUNDERS = "founders"
    INVESTORS = "investors"
    PRIVATE = "private"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
