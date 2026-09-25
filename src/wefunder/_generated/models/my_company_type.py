from enum import StrEnum


class MyCompanyType(StrEnum):
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)
