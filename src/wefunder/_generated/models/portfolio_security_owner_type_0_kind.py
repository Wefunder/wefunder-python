from enum import StrEnum

class PortfolioSecurityOwnerType0Kind(StrEnum):
    ENTITY = "entity"
    INDIVIDUAL = "individual"

    def __str__(self) -> str:
        return str(self.value)
