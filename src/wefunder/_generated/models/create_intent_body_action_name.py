from enum import StrEnum


class CreateIntentBodyActionName(StrEnum):
    COMMENTS_CREATE = "comments.create"
    SYNDICATES_CLOSE_DEAL = "syndicates.close_deal"
    SYNDICATES_DELETE_DRAFT = "syndicates.delete_draft"
    SYNDICATES_FINALIZE_DEAL = "syndicates.finalize_deal"
    SYNDICATES_PUBLISH = "syndicates.publish"
    SYNDICATES_REMOVE_MEMBER = "syndicates.remove_member"

    def __str__(self) -> str:
        return str(self.value)
