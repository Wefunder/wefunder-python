from enum import StrEnum


class CompanyQuestionAttributesMatch(StrEnum):
    ANSWER = "answer"
    QUESTION = "question"

    def __str__(self) -> str:
        return str(self.value)
