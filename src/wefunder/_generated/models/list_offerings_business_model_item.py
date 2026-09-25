from enum import StrEnum


class ListOfferingsBusinessModelItem(StrEnum):
    B2B = "b2b"
    B2C = "b2c"
    ECOMMERCE = "ecommerce"
    MARKETPLACE = "marketplace"
    RETAIL = "retail"
    SAAS = "saas"
    SERVICE = "service"
    SUBSCRIPTION = "subscription"

    def __str__(self) -> str:
        return str(self.value)
