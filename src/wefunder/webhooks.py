"""Webhook verification + parsing for Wefunder platform events.

The shipped scheme (docs.wefunder.com → Partner API → Webhooks → Verification) is a single
Stripe-style header::

    Wefunder-Signature: t=<unix seconds>,v1=<hex>[,v1=<hex>]
    v1 = HMAC-SHA256(secret, "<t>.<raw_body>")

During a secret rotation the header carries one ``v1`` per active secret (24h overlap); a
delivery is valid if ANY ``v1`` matches. Consumers enforce a replay tolerance on ``t``
(documented: 5 minutes). Every delivery body is the envelope
``{id: "evt_…", event, created_at, mode, data}`` — ``id`` is the dedup key.

The retired attribution surface signed differently (``X-Wefunder-Signature: sha256=<hex>``
+ ``X-Wefunder-Timestamp``). :func:`construct_event` still accepts that shape so an
attribution subscriber isn't stranded; everything new targets the platform-events scheme.
"""

from __future__ import annotations

import hashlib
import hmac
import inspect
import json
import time
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any, Literal

from ._generated.models.create_webhook_endpoint_body_events_item import CreateWebhookEndpointBodyEventsItem

#: Every event name in the catalog, derived from the spec so it can't drift from the API.
WEBHOOK_EVENT_NAMES: frozenset[str] = frozenset(e.value for e in CreateWebhookEndpointBodyEventsItem)

#: The platform-events signature header (case-insensitive).
SIGNATURE_HEADER = "wefunder-signature"
#: Documented consumer replay tolerance.
DEFAULT_TOLERANCE_SECONDS = 300

# Attribution-era headers; only relevant to legacy attribution subscriptions.
LEGACY_SIGNATURE_HEADER = "x-wefunder-signature"
LEGACY_TIMESTAMP_HEADER = "x-wefunder-timestamp"
LEGACY_EVENT_HEADER = "x-wefunder-event"
LEGACY_DELIVERY_ID_HEADER = "x-wefunder-delivery-id"

WebhookSignatureFailure = Literal[
    "missing_header", "malformed_header", "timestamp_out_of_tolerance", "signature_mismatch", "invalid_payload"
]
WebhookMode = Literal["live", "test"]
RawBody = str | bytes | bytearray
HeadersLike = Mapping[str, Any] | str
Now = Callable[[], float]  # unix seconds

_FAILURE_MESSAGES: dict[str, str] = {
    "missing_header": "Missing Wefunder-Signature header",
    "malformed_header": "Wefunder-Signature header is malformed (expected t=<unix>,v1=<hex>)",
    "timestamp_out_of_tolerance": "Webhook timestamp is outside the replay tolerance",
    "signature_mismatch": "Webhook signature verification failed",
    "invalid_payload": "Webhook body is not a JSON object",
}


class WebhookSignatureError(Exception):
    """Raised by :func:`construct_event`. Respond 400 and don't process."""

    def __init__(self, reason: WebhookSignatureFailure) -> None:
        super().__init__(_FAILURE_MESSAGES[reason])
        self.reason: WebhookSignatureFailure = reason


@dataclass(slots=True)
class WebhookEvent:
    """A verified, parsed delivery. ``data`` is the documented payload for ``event``;
    names newer than this SDK still arrive here (untyped) after verification."""

    #: Event id (``evt_…``) — the dedup key. Deliveries may repeat; ignore ids you've seen.
    id: str
    event: str
    created_at: str
    mode: WebhookMode
    data: Any
    #: The signed timestamp (``t``, unix seconds).
    timestamp: int

    @property
    def known(self) -> bool:
        """Whether ``event`` is in this SDK's catalog."""
        return self.event in WEBHOOK_EVENT_NAMES


@dataclass(frozen=True, slots=True)
class ParsedSignatureHeader:
    timestamp: int
    #: Every ``v1`` value (more than one during a secret rotation).
    signatures: tuple[str, ...]


# ---- primitives -------------------------------------------------------------------------


def _body_bytes(payload: RawBody) -> bytes:
    return payload.encode("utf-8") if isinstance(payload, str) else bytes(payload)


def compute_webhook_signature(secret: str, timestamp: int | str, payload: RawBody) -> str:
    """``HMAC-SHA256(secret, "<timestamp>.<raw body>")`` as lowercase hex."""
    mac = hmac.new(secret.encode("utf-8"), f"{timestamp}.".encode(), hashlib.sha256)
    mac.update(_body_bytes(payload))
    return mac.hexdigest()


def parse_signature_header(header: str) -> ParsedSignatureHeader | None:
    """Parse ``t=<unix>,v1=<hex>[,v1=<hex>]``. ``None`` when the shape is wrong. Unknown
    keys (a future ``v2``) are ignored on purpose — forward compatible."""
    timestamp: int | None = None
    signatures: list[str] = []
    for part in header.split(","):
        key, eq, value = part.partition("=")
        if not eq:
            continue
        key, value = key.strip(), value.strip()
        if key == "t":
            if not value.isdigit():
                return None
            timestamp = int(value)
        elif key == "v1" and value:
            signatures.append(value)
    if timestamp is None or not signatures:
        return None
    return ParsedSignatureHeader(timestamp=timestamp, signatures=tuple(signatures))


def sign_webhook(
    payload: RawBody,
    secret: str,
    *,
    timestamp: int | None = None,
    additional_secrets: list[str] | tuple[str, ...] = (),
) -> str:
    """Build a ``Wefunder-Signature`` header value for ``payload``. For your own tests (sign a
    fixture, POST it at your handler) — the API signs real deliveries. ``additional_secrets``
    adds one ``v1`` per secret, simulating a rotation window."""
    t = timestamp if timestamp is not None else int(time.time())
    entries = [f"v1={compute_webhook_signature(s, t, payload)}" for s in (secret, *additional_secrets)]
    return ",".join([f"t={t}", *entries])


# ---- verification -----------------------------------------------------------------------


def check_webhook_signature(
    payload: RawBody,
    header: str,
    secret: str,
    *,
    tolerance_seconds: float = DEFAULT_TOLERANCE_SECONDS,
    now: Now | None = None,
) -> WebhookSignatureFailure | None:
    """The reason a delivery is NOT valid, or ``None`` when it is. Constant-time compare
    against every ``v1``; enforces the timestamp tolerance (``0`` disables it)."""
    parsed = parse_signature_header(header)
    if parsed is None:
        return "malformed_header"
    if tolerance_seconds > 0 and abs((now or time.time)() - parsed.timestamp) > tolerance_seconds:
        return "timestamp_out_of_tolerance"
    expected = compute_webhook_signature(secret, parsed.timestamp, payload)
    return None if any(hmac.compare_digest(sig, expected) for sig in parsed.signatures) else "signature_mismatch"


def verify_legacy_webhook(
    payload: RawBody,
    signature: str,
    timestamp: str | int,
    secret: str,
    *,
    tolerance_seconds: float = DEFAULT_TOLERANCE_SECONDS,
    now: Now | None = None,
) -> bool:
    """Legacy attribution scheme: ``X-Wefunder-Signature: sha256=<hex>`` + ``X-Wefunder-Timestamp``."""
    try:
        ts = int(str(timestamp))
    except ValueError:
        return False
    if tolerance_seconds > 0 and abs((now or time.time)() - ts) > tolerance_seconds:
        return False
    expected = f"sha256={compute_webhook_signature(secret, timestamp, payload)}"
    return hmac.compare_digest(signature, expected)


def verify_webhook(
    payload: RawBody,
    secret: str,
    *,
    header: str | None = None,
    signature: str | None = None,
    timestamp: str | int | None = None,
    tolerance_seconds: float = DEFAULT_TOLERANCE_SECONDS,
    now: Now | None = None,
) -> bool:
    """``True`` iff the signature is valid and (when tolerance > 0) the timestamp is within
    tolerance. Never raises — respond 400 without a try/except. Pass ``header`` (the
    ``Wefunder-Signature`` value) or, for a legacy attribution subscription,
    ``signature`` + ``timestamp``."""
    if header is not None:
        return check_webhook_signature(payload, header, secret, tolerance_seconds=tolerance_seconds, now=now) is None
    if signature is None or timestamp is None:
        return False
    return verify_legacy_webhook(payload, signature, timestamp, secret, tolerance_seconds=tolerance_seconds, now=now)


# ---- construct_event: verify + parse ------------------------------------------------------


def _header_getter(headers: HeadersLike) -> Callable[[str], str | None]:
    if isinstance(headers, str):
        return lambda name: headers if name == SIGNATURE_HEADER else None
    lowered = {str(k).lower(): v for k, v in headers.items()}

    def get(name: str) -> str | None:
        value = lowered.get(name)
        if isinstance(value, (list, tuple)):
            value = value[0] if value else None
        return None if value is None else str(value)

    return get


def _parse_envelope(payload: RawBody) -> dict[str, Any]:
    try:
        parsed = json.loads(_body_bytes(payload).decode("utf-8"))
    except (ValueError, UnicodeDecodeError):
        raise WebhookSignatureError("invalid_payload") from None
    if not isinstance(parsed, dict):
        raise WebhookSignatureError("invalid_payload")
    return parsed


def _mode(value: Any) -> WebhookMode:
    return "test" if value == "test" else "live"


def construct_event(
    payload: RawBody,
    headers: HeadersLike,
    secret: str,
    *,
    tolerance_seconds: float = DEFAULT_TOLERANCE_SECONDS,
    now: Now | None = None,
) -> WebhookEvent:
    """Verify a delivery and parse its envelope in one step. Raises
    :class:`WebhookSignatureError` (with ``reason``) on any failure so handlers fail loudly.

    :param payload: the RAW request body (bytes or str) — never a re-serialised object
    :param headers: the request headers (any mapping; case-insensitive), or the
        ``Wefunder-Signature`` value itself
    :param secret: the endpoint's signing secret (shown once at create / rotate)
    """
    get = _header_getter(headers)
    header = get(SIGNATURE_HEADER)
    if not header:
        legacy_sig, legacy_ts = get(LEGACY_SIGNATURE_HEADER), get(LEGACY_TIMESTAMP_HEADER)
        if legacy_sig and legacy_ts:
            return _construct_legacy_event(payload, get, legacy_sig, legacy_ts, secret, tolerance_seconds, now)
        raise WebhookSignatureError("missing_header")
    failure = check_webhook_signature(payload, header, secret, tolerance_seconds=tolerance_seconds, now=now)
    if failure is not None:
        raise WebhookSignatureError(failure)
    parsed = parse_signature_header(header)
    assert parsed is not None
    env = _parse_envelope(payload)
    return WebhookEvent(
        id=str(env.get("id") or ""),
        event=str(env.get("event") or ""),
        created_at=str(env.get("created_at") or ""),
        mode=_mode(env.get("mode")),
        data=env.get("data"),
        timestamp=parsed.timestamp,
    )


def _construct_legacy_event(
    payload: RawBody,
    get: Callable[[str], str | None],
    signature: str,
    timestamp: str,
    secret: str,
    tolerance_seconds: float,
    now: Now | None,
) -> WebhookEvent:
    if not verify_legacy_webhook(payload, signature, timestamp, secret, tolerance_seconds=tolerance_seconds, now=now):
        raise WebhookSignatureError("signature_mismatch")
    env = _parse_envelope(payload)
    return WebhookEvent(
        id=str(env.get("id") or get(LEGACY_DELIVERY_ID_HEADER) or ""),
        event=str(env.get("event") or get(LEGACY_EVENT_HEADER) or ""),
        created_at=str(env.get("created_at") or ""),
        mode=_mode(env.get("mode")),
        data=env.get("data", env),
        timestamp=int(timestamp),
    )


# ---- dispatch -----------------------------------------------------------------------------

Handler = Callable[[WebhookEvent], Any]


def _pick_handler(event: WebhookEvent, handlers: Mapping[str, Handler]) -> Handler | None:
    # An event literally named "default" never selects the fallback as a *specific* handler.
    specific = handlers.get(event.event) if event.event != "default" else None
    return specific or handlers.get("default")


def dispatch_webhook(event: WebhookEvent, handlers: Mapping[str, Handler]) -> bool:
    """Call the handler registered for ``event.event``, falling back to ``"default"``.
    Returns ``True`` if a handler ran. Pairs with :func:`construct_event`."""
    handler = _pick_handler(event, handlers)
    if handler is None:
        return False
    handler(event)
    return True


async def async_dispatch_webhook(event: WebhookEvent, handlers: Mapping[str, Handler]) -> bool:
    """:func:`dispatch_webhook` for coroutine (or plain) handlers."""
    handler = _pick_handler(event, handlers)
    if handler is None:
        return False
    result = handler(event)
    if inspect.isawaitable(result):
        await result
    return True
