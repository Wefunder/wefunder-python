from enum import StrEnum

class CommentProposalEnvelopeProposalTargetType(StrEnum):
    COMMENT = "comment"
    COMPANY = "company"

    def __str__(self) -> str:
        return str(self.value)
