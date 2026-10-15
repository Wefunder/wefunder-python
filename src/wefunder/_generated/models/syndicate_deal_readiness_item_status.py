from enum import StrEnum


class SyndicateDealReadinessItemStatus(StrEnum):
    BLOCKED = "blocked"
    COMPLETE = "complete"
    MISSING = "missing"
    NEEDS_HUMAN = "needs_human"
    NEEDS_STAFF = "needs_staff"

    def __str__(self) -> str:
        return str(self.value)
