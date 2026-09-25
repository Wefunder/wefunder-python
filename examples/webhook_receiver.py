"""Verify + handle a delivery. Framework-agnostic: pass the RAW body bytes and the headers."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from wefunder import WebhookEvent, WebhookSignatureError, construct_event, dispatch_webhook


def handle_delivery(raw_body: bytes, headers: Mapping[str, str], secret: str) -> tuple[int, str]:
    # region guides/webhook-receiver
    try:
        event = construct_event(raw_body, headers, secret)
    except WebhookSignatureError as err:
        return 400, err.reason  # not authentic — don't process

    # Acknowledge first, then do the work. Deliveries are at-least-once and unordered:
    # deduplicate on event.id and, where a payload has occurred_at, keep the latest state.
    def record_funding(e: WebhookEvent) -> None:
        print("funded", e.data["id"], e.data["amounts"]["committed"])

    dispatch_webhook(
        event,
        {
            "investment.executed": record_funding,
            "offering.opened": lambda e: print("opened", e.data["company"]["name"]),
            "default": lambda e: print("unhandled", e.event),
        },
    )
    # endregion
    return 200, "ok"


def example(_wf: Any = None) -> None:  # hidden harness entry so the file type-checks in the gate
    return None
