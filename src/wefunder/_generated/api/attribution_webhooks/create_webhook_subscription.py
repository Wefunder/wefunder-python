from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_subscription_body import CreateWebhookSubscriptionBody
from ...models.error import Error
from ...models.webhook_subscription_with_secret_envelope import WebhookSubscriptionWithSecretEnvelope
from ...types import Response


def _get_kwargs(
    campaign_id: int,
    *,
    body: CreateWebhookSubscriptionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/campaigns/{campaign_id}/attribution/webhooks".format(
            campaign_id=quote(str(campaign_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WebhookSubscriptionWithSecretEnvelope | None:
    if response.status_code == 201:
        response_201 = WebhookSubscriptionWithSecretEnvelope.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | WebhookSubscriptionWithSecretEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateWebhookSubscriptionBody,
) -> Response[Error | WebhookSubscriptionWithSecretEnvelope]:
    """Create webhook subscription

     Creates a new webhook subscription for this campaign. When attributed
    investments change state, we'll POST a JSON payload to your target URL.

    **Tier 1** endpoint requiring admin-approved access.

    ## Webhook Payload

    Payloads include anonymized data (tokens, amount tiers) matching the
    `/attribution/investments` endpoint.

    ## Security

    - `target_url` must use HTTPS
    - `target_url` cannot resolve to private/internal IPs (SSRF protection)
    - Payloads are signed with HMAC-SHA256 using the returned `secret`

    ## Verification

    Verify webhook signatures using the `X-Wefunder-Signature` header:
    ```
    timestamp = headers['X-Wefunder-Timestamp']
    signature = headers['X-Wefunder-Signature']
    expected = "sha256=" + HMAC-SHA256(secret, timestamp + "." + raw_body)
    ```

    Reject requests where:
    - Signature doesn't match
    - Timestamp is more than 5 minutes old (replay protection)

    Args:
        campaign_id (int):
        body (CreateWebhookSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscriptionWithSecretEnvelope]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateWebhookSubscriptionBody,
) -> Error | WebhookSubscriptionWithSecretEnvelope | None:
    """Create webhook subscription

     Creates a new webhook subscription for this campaign. When attributed
    investments change state, we'll POST a JSON payload to your target URL.

    **Tier 1** endpoint requiring admin-approved access.

    ## Webhook Payload

    Payloads include anonymized data (tokens, amount tiers) matching the
    `/attribution/investments` endpoint.

    ## Security

    - `target_url` must use HTTPS
    - `target_url` cannot resolve to private/internal IPs (SSRF protection)
    - Payloads are signed with HMAC-SHA256 using the returned `secret`

    ## Verification

    Verify webhook signatures using the `X-Wefunder-Signature` header:
    ```
    timestamp = headers['X-Wefunder-Timestamp']
    signature = headers['X-Wefunder-Signature']
    expected = "sha256=" + HMAC-SHA256(secret, timestamp + "." + raw_body)
    ```

    Reject requests where:
    - Signature doesn't match
    - Timestamp is more than 5 minutes old (replay protection)

    Args:
        campaign_id (int):
        body (CreateWebhookSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscriptionWithSecretEnvelope
    """

    return sync_detailed(
        campaign_id=campaign_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateWebhookSubscriptionBody,
) -> Response[Error | WebhookSubscriptionWithSecretEnvelope]:
    """Create webhook subscription

     Creates a new webhook subscription for this campaign. When attributed
    investments change state, we'll POST a JSON payload to your target URL.

    **Tier 1** endpoint requiring admin-approved access.

    ## Webhook Payload

    Payloads include anonymized data (tokens, amount tiers) matching the
    `/attribution/investments` endpoint.

    ## Security

    - `target_url` must use HTTPS
    - `target_url` cannot resolve to private/internal IPs (SSRF protection)
    - Payloads are signed with HMAC-SHA256 using the returned `secret`

    ## Verification

    Verify webhook signatures using the `X-Wefunder-Signature` header:
    ```
    timestamp = headers['X-Wefunder-Timestamp']
    signature = headers['X-Wefunder-Signature']
    expected = "sha256=" + HMAC-SHA256(secret, timestamp + "." + raw_body)
    ```

    Reject requests where:
    - Signature doesn't match
    - Timestamp is more than 5 minutes old (replay protection)

    Args:
        campaign_id (int):
        body (CreateWebhookSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscriptionWithSecretEnvelope]
    """

    kwargs = _get_kwargs(
        campaign_id=campaign_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    body: CreateWebhookSubscriptionBody,
) -> Error | WebhookSubscriptionWithSecretEnvelope | None:
    """Create webhook subscription

     Creates a new webhook subscription for this campaign. When attributed
    investments change state, we'll POST a JSON payload to your target URL.

    **Tier 1** endpoint requiring admin-approved access.

    ## Webhook Payload

    Payloads include anonymized data (tokens, amount tiers) matching the
    `/attribution/investments` endpoint.

    ## Security

    - `target_url` must use HTTPS
    - `target_url` cannot resolve to private/internal IPs (SSRF protection)
    - Payloads are signed with HMAC-SHA256 using the returned `secret`

    ## Verification

    Verify webhook signatures using the `X-Wefunder-Signature` header:
    ```
    timestamp = headers['X-Wefunder-Timestamp']
    signature = headers['X-Wefunder-Signature']
    expected = "sha256=" + HMAC-SHA256(secret, timestamp + "." + raw_body)
    ```

    Reject requests where:
    - Signature doesn't match
    - Timestamp is more than 5 minutes old (replay protection)

    Args:
        campaign_id (int):
        body (CreateWebhookSubscriptionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscriptionWithSecretEnvelope
    """

    return (
        await asyncio_detailed(
            campaign_id=campaign_id,
            client=client,
            body=body,
        )
    ).parsed
