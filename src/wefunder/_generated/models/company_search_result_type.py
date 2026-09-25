from enum import StrEnum


class CompanySearchResultType(StrEnum):
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)
