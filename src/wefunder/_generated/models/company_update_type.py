from enum import StrEnum


class CompanyUpdateType(StrEnum):
    COMPANY_UPDATE = "company_update"

    def __str__(self) -> str:
        return str(self.value)
