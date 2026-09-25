from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.webhook_subscription_with_secret_2_envelope import WebhookSubscriptionWithSecret2Envelope
from ...types import Response


def _get_kwargs(
    campaign_id: int,
    webhook_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/campaigns/{campaign_id}/attribution/webhooks/{webhook_id}/regenerate_secret".format(
            campaign_id=quote(str(campaign_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WebhookSubscriptionWithSecret2Envelope | None:
    if response.status_code == 200:
        response_200 = WebhookSubscriptionWithSecret2Envelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | WebhookSubscriptionWithSecret2Envelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: int,
    webhook_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error | WebhookSubscriptionWithSecret2Envelope]:
    """Regenerate webhook signing secret

     Generates a new HMAC signing secret for the webhook subscription.
    The old secret is immediately invalidated.

    **Important**: Store the new secret securely - it cannot be retrieved later.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscriptionWithSecret2Envelope]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        webhook_id=webhook_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: int,
    webhook_id: int,
    *,
    client: AuthenticatedClient,
) -> Error | WebhookSubscriptionWithSecret2Envelope | None:
    """Regenerate webhook signing secret

     Generates a new HMAC signing secret for the webhook subscription.
    The old secret is immediately invalidated.

    **Important**: Store the new secret securely - it cannot be retrieved later.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscriptionWithSecret2Envelope
    """

    return sync_detailed(
        campaign_id=campaign_id,
        webhook_id=webhook_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    campaign_id: int,
    webhook_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Error | WebhookSubscriptionWithSecret2Envelope]:
    """Regenerate webhook signing secret

     Generates a new HMAC signing secret for the webhook subscription.
    The old secret is immediately invalidated.

    **Important**: Store the new secret securely - it cannot be retrieved later.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscriptionWithSecret2Envelope]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        webhook_id=webhook_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: int,
    webhook_id: int,
    *,
    client: AuthenticatedClient,
) -> Error | WebhookSubscriptionWithSecret2Envelope | None:
    """Regenerate webhook signing secret

     Generates a new HMAC signing secret for the webhook subscription.
    The old secret is immediately invalidated.

    **Important**: Store the new secret securely - it cannot be retrieved later.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscriptionWithSecret2Envelope
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
