from enum import StrEnum

class CompanyPitchAttributesAuthoredBy(StrEnum):
    COMPANY = "company"
    WEFUNDER = "wefunder"

    def __str__(self) -> str:
        return str(self.value)
