from enum import StrEnum


class MemberLinkType(StrEnum):
    MEMBER_LINK = "member_link"

    def __str__(self) -> str:
        return str(self.value)
