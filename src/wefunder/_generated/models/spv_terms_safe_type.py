from enum import StrEnum


class SpvTermsSafeType(StrEnum):
    POST_MONEY = "post_money"
    PRE_MONEY = "pre_money"

    def __str__(self) -> str:
        return str(self.value)
