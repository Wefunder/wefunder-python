from enum import StrEnum

class PastRoundSource(StrEnum):
    REPORTED = "reported"
    WEFUNDER = "wefunder"

    def __str__(self) -> str:
        return str(self.value)
