from enum import StrEnum


class FollowedCompanyType(StrEnum):
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)
