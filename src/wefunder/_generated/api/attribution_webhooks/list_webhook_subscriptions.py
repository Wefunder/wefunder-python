from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.webhook_subscription_list_envelope import WebhookSubscriptionListEnvelope
from typing import cast



def _get_kwargs(
    campaign_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/campaigns/{campaign_id}/attribution/webhooks".format(campaign_id=quote(str(campaign_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | WebhookSubscriptionListEnvelope | None:
    if response.status_code == 200:
        response_200 = WebhookSubscriptionListEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | WebhookSubscriptionListEnvelope]:
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

) -> Response[Error | WebhookSubscriptionListEnvelope]:
    """ List attribution webhook subscriptions

     Returns all active webhook subscriptions for this campaign belonging to
    your OAuth application.

    **Tier 1** endpoint requiring admin-approved access with the
    `read:attribution:anonymized` scope.

    Args:
        campaign_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscriptionListEnvelope]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: int,
    *,
    client: AuthenticatedClient,

) -> Error | WebhookSubscriptionListEnvelope | None:
    """ List attribution webhook subscriptions

     Returns all active webhook subscriptions for this campaign belonging to
    your OAuth application.

    **Tier 1** endpoint requiring admin-approved access with the
    `read:attribution:anonymized` scope.

    Args:
        campaign_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscriptionListEnvelope
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,

    ).parsed

async def asyncio_detailed(
    campaign_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[Error | WebhookSubscriptionListEnvelope]:
    """ List attribution webhook subscriptions

     Returns all active webhook subscriptions for this campaign belonging to
    your OAuth application.

    **Tier 1** endpoint requiring admin-approved access with the
    `read:attribution:anonymized` scope.

    Args:
        campaign_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookSubscriptionListEnvelope]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: int,
    *,
    client: AuthenticatedClient,

) -> Error | WebhookSubscriptionListEnvelope | None:
    """ List attribution webhook subscriptions

     Returns all active webhook subscriptions for this campaign belonging to
    your OAuth application.

    **Tier 1** endpoint requiring admin-approved access with the
    `read:attribution:anonymized` scope.

    Args:
        campaign_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookSubscriptionListEnvelope
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,

    )).parsed
