from enum import StrEnum


class MemberLinkAttributesState(StrEnum):
    BOUND = "bound"
    CANCELED = "canceled"
    CREATED = "created"
    INVESTED = "invested"

    def __str__(self) -> str:
        return str(self.value)
