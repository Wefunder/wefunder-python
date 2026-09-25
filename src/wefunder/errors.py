"""Typed errors mapped from the real Wefunder error envelope.

Confirmed against ``api/v2/base_controller.rb#render_error``::

    {"error": {"type", "message", "details"?, "request_id", "remediation"?}}

``request_id`` and ``remediation`` are NESTED under ``error`` (not top-level). The
``X-Wf-Request-Id`` response header is set on every authenticated response — even when the
body is not JSON (an HTML 502 from the edge) — so it is preferred over the body's id.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

import httpx

#: Response header carrying the partner-facing request id (Stripe-style ``req_…``).
REQUEST_ID_HEADER = "X-Wf-Request-Id"
#: ``type`` reported when the body is not the documented envelope.
FALLBACK_ERROR_TYPE = "api_error"


class WefunderError(Exception):
    """An API call failed. ``status``/``type`` tell you what; ``request_id`` is for support."""

    #: Documentation pointer surfaced to developers in tracebacks and logs.
    documentation_url = "https://docs.wefunder.com/api-reference"

    def __init__(
        self,
        *,
        status: int,
        type: str,
        message: str,
        request_id: str | None = None,
        details: Any = None,
        remediation: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.type = type
        self.message = message
        self.request_id = request_id
        self.details = details
        self.remediation = remediation

    def __str__(self) -> str:
        parts = [f"{self.status} {self.type}: {self.message}"]
        if self.request_id:
            parts.append(f"(request_id={self.request_id})")
        if self.remediation:
            parts.append(f"— {self.remediation}")
        return " ".join(parts)


class WefunderAuthError(WefunderError):
    """Raised when a token must be recovered but no refresh token / re-mint capability exists."""

    def __init__(self, message: str) -> None:
        super().__init__(status=401, type="unauthorized", message=message)


def request_id_from(headers: Mapping[str, str] | httpx.Headers, body_request_id: str | None) -> str | None:
    """Prefer the ``X-Wf-Request-Id`` header; fall back to a body-derived id."""
    hdrs = headers if isinstance(headers, httpx.Headers) else httpx.Headers(dict(headers))
    return hdrs.get(REQUEST_ID_HEADER) or body_request_id


def error_from_response(
    status: int,
    headers: Mapping[str, str] | httpx.Headers,
    content: bytes | str | None,
    *,
    reason_phrase: str | None = None,
) -> WefunderError:
    """Build a :class:`WefunderError` from a failed response's parts.

    Reads the typed envelope from the body and degrades gracefully when the body is not
    the documented shape (non-JSON, empty, or a bare object).
    """
    body: Any = None
    if content:
        try:
            body = json.loads(content)
        except ValueError:
            body = None
    err = body.get("error") if isinstance(body, Mapping) else None
    if not isinstance(err, Mapping):
        err = {}
    top_level_request_id = body.get("request_id") if isinstance(body, Mapping) else None
    message = err.get("message")
    if not isinstance(message, str):
        message = reason_phrase or "Request failed"
    etype = err.get("type")
    return WefunderError(
        status=status,
        type=etype if isinstance(etype, str) else FALLBACK_ERROR_TYPE,
        message=message,
        request_id=request_id_from(headers, err.get("request_id") or top_level_request_id),
        details=err.get("details"),
        remediation=err.get("remediation") if isinstance(err.get("remediation"), str) else None,
    )


def error_from_httpx(response: httpx.Response) -> WefunderError:
    """:func:`error_from_response` for an ``httpx.Response`` (body must already be read)."""
    return error_from_response(
        response.status_code, response.headers, response.content, reason_phrase=response.reason_phrase or None
    )
