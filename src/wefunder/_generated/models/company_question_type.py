from enum import StrEnum

class CompanyQuestionType(StrEnum):
    COMPANY_QUESTION = "company_question"

    def __str__(self) -> str:
        return str(self.value)
