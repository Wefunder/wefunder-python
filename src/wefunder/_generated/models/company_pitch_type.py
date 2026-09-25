from enum import StrEnum


class CompanyPitchType(StrEnum):
    COMPANY_PITCH = "company_pitch"

    def __str__(self) -> str:
        return str(self.value)
