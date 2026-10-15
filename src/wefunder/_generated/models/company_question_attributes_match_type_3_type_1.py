from enum import StrEnum


class CompanyQuestionAttributesMatchType3Type1(StrEnum):
    ANSWER = "answer"
    QUESTION = "question"

    def __str__(self) -> str:
        return str(self.value)
