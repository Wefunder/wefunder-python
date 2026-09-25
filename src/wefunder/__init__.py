"""Official Python SDK for the Wefunder API (beta).

from wefunder import Wefunder

wf = Wefunder.from_client_credentials(client_id=..., client_secret=..., scopes=["read:public"])
for offering in wf.offerings.all(sort="newest"):
    print(offering.id)
"""

from ._retry import RetryOptions
from ._version import __version__
from .client import (
    API_VERSION_HEADER,
    DEFAULT_API_BASE_URL,
    DEFAULT_API_VERSION,
    AsyncWefunder,
    Mode,
    Wefunder,
    mode_for_token,
)
from .errors import REQUEST_ID_HEADER, WefunderAuthError, WefunderError
from .oauth import (
    DEFAULT_AUTHORIZE_BASE_URL,
    DEFAULT_TOKEN_BASE_URL,
    SANDBOX_AUTHORIZE_BASE_URL,
    OAuthTokenError,
    Pkce,
    TokenSet,
    async_client_credentials_grant,
    async_exchange_code,
    async_refresh_token,
    client_credentials_grant,
    create_authorization_url,
    exchange_code,
    generate_pkce,
    pkce_challenge,
    refresh_token,
)
from .pagination import acollect, apaginate, collect, paginate
from .token_manager import AsyncTokenManager, TokenManager, TokenStore
from .webhooks import (
    DEFAULT_TOLERANCE_SECONDS,
    SIGNATURE_HEADER,
    WEBHOOK_EVENT_NAMES,
    WebhookEvent,
    WebhookSignatureError,
    async_dispatch_webhook,
    check_webhook_signature,
    compute_webhook_signature,
    construct_event,
    dispatch_webhook,
    parse_signature_header,
    sign_webhook,
    verify_webhook,
)

__all__ = [
    "API_VERSION_HEADER",
    "DEFAULT_API_BASE_URL",
    "DEFAULT_API_VERSION",
    "DEFAULT_AUTHORIZE_BASE_URL",
    "DEFAULT_TOKEN_BASE_URL",
    "DEFAULT_TOLERANCE_SECONDS",
    "REQUEST_ID_HEADER",
    "SANDBOX_AUTHORIZE_BASE_URL",
    "SIGNATURE_HEADER",
    "WEBHOOK_EVENT_NAMES",
    "AsyncTokenManager",
    "AsyncWefunder",
    "Mode",
    "OAuthTokenError",
    "Pkce",
    "RetryOptions",
    "TokenManager",
    "TokenSet",
    "TokenStore",
    "WebhookEvent",
    "WebhookSignatureError",
    "Wefunder",
    "WefunderAuthError",
    "WefunderError",
    "__version__",
    "acollect",
    "apaginate",
    "async_client_credentials_grant",
    "async_dispatch_webhook",
    "async_exchange_code",
    "async_refresh_token",
    "check_webhook_signature",
    "client_credentials_grant",
    "collect",
    "compute_webhook_signature",
    "construct_event",
    "create_authorization_url",
    "dispatch_webhook",
    "exchange_code",
    "generate_pkce",
    "mode_for_token",
    "paginate",
    "parse_signature_header",
    "pkce_challenge",
    "refresh_token",
    "sign_webhook",
    "verify_webhook",
]
