from enum import StrEnum


class CompanyQuestionAttributesMatchType2Type1(StrEnum):
    ANSWER = "answer"
    QUESTION = "question"

    def __str__(self) -> str:
        return str(self.value)
