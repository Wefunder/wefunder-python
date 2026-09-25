from enum import StrEnum

class SyndicateMemberAttributesSyndicatePermission(StrEnum):
    FULL_ACCESS = "full_access"
    OPERATOR = "operator"

    def __str__(self) -> str:
        return str(self.value)
