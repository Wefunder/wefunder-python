from enum import StrEnum

class CreateWebhookEndpointBodyMode(StrEnum):
    LIVE = "live"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
