from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.webhook_test_result_envelope import WebhookTestResultEnvelope
from ...types import Response


def _get_kwargs(
    campaign_id: int,
    webhook_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/campaigns/{campaign_id}/attribution/webhooks/{webhook_id}/test".format(
            campaign_id=quote(str(campaign_id), safe=""),
            webhook_id=quote(str(webhook_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WebhookTestResultEnvelope | None:
    if response.status_code == 200:
        response_200 = WebhookTestResultEnvelope.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | WebhookTestResultEnvelope]:
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
) -> Response[Error | WebhookTestResultEnvelope]:
    """Send test webhook

     Sends a test webhook to verify your endpoint is working correctly.
    The test payload includes a `"event": "test"` field to distinguish
    it from real events.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookTestResultEnvelope]
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
) -> Error | WebhookTestResultEnvelope | None:
    """Send test webhook

     Sends a test webhook to verify your endpoint is working correctly.
    The test payload includes a `"event": "test"` field to distinguish
    it from real events.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookTestResultEnvelope
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
) -> Response[Error | WebhookTestResultEnvelope]:
    """Send test webhook

     Sends a test webhook to verify your endpoint is working correctly.
    The test payload includes a `"event": "test"` field to distinguish
    it from real events.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookTestResultEnvelope]
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
) -> Error | WebhookTestResultEnvelope | None:
    """Send test webhook

     Sends a test webhook to verify your endpoint is working correctly.
    The test payload includes a `"event": "test"` field to distinguish
    it from real events.

    Args:
        campaign_id (int):
        webhook_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookTestResultEnvelope
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            webhook_id=webhook_id,
            client=client,
        )
    ).parsed
