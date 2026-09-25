from enum import StrEnum


class CompanyDisclosuresType(StrEnum):
    COMPANY_DISCLOSURES = "company_disclosures"

    def __str__(self) -> str:
        return str(self.value)
