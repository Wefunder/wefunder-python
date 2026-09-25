from enum import StrEnum


class PortfolioPositionType(StrEnum):
    PORTFOLIO_POSITION = "portfolio_position"
    SYNDICATE_PORTFOLIO_POSITION = "syndicate_portfolio_position"

    def __str__(self) -> str:
        return str(self.value)
