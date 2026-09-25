from enum import StrEnum

class WebhookEndpointTestResultEnvelopeDataErrorType1(StrEnum):
    BLOCKED_URL = "blocked_url"
    CONNECTION_FAILED = "connection_failed"
    TIMEOUT = "timeout"
    TLS_ERROR = "tls_error"

    def __str__(self) -> str:
        return str(self.value)
