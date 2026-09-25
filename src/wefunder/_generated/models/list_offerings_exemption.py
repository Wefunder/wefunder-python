from enum import StrEnum


class ListOfferingsExemption(StrEnum):
    REG_CF = "reg_cf"
    REG_D = "reg_d"

    def __str__(self) -> str:
        return str(self.value)
