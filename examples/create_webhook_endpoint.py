"""operationId: createWebhookEndpoint — register a signed delivery target (write:webhooks, live API)."""

from __future__ import annotations

from typing import Any

from wefunder import Wefunder


def example(wf: Wefunder) -> Any:
    # region createWebhookEndpoint
    endpoint = wf.webhook_endpoints.create(
        url="https://yourapp.com/webhooks/wefunder",  # public HTTPS; localhost / private IPs are rejected
        events=["offering.opened", "investment.executed"],
        mode="live",  # "test" endpoints receive sandbox events
    )
    # The signing secret is returned ONLY here and on rotate — store it now.
    save_secret(endpoint.attributes.secret)
    # endregion
    return endpoint


def save_secret(secret: str) -> None:  # harness stand-in for your secrets store
    del secret
