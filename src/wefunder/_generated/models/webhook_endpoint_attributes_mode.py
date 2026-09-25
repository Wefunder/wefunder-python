from enum import StrEnum

class WebhookEndpointAttributesMode(StrEnum):
    LIVE = "live"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
