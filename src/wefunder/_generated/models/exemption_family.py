from enum import StrEnum


class ExemptionFamily(StrEnum):
    ECSP = "ecsp"
    OTHER = "other"
    REG_A = "reg_a"
    REG_CF = "reg_cf"
    REG_D = "reg_d"
    REG_S = "reg_s"

    def __str__(self) -> str:
        return str(self.value)
