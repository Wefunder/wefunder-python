from enum import StrEnum


class CreateWebhookSubscriptionBodyEventsItem(StrEnum):
    INVESTMENT_APPLIED = "investment.applied"
    INVESTMENT_CANCELED = "investment.canceled"
    INVESTMENT_CONFIRMED = "investment.confirmed"

    def __str__(self) -> str:
        return str(self.value)
