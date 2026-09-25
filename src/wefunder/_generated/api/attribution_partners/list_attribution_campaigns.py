from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.attribution_campaign_summary_list_envelope import AttributionCampaignSummaryListEnvelope
from ...models.error import Error
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/attribution/campaigns",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttributionCampaignSummaryListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = AttributionCampaignSummaryListEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AttributionCampaignSummaryListEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[AttributionCampaignSummaryListEnvelope | Error]:
    """ List campaigns accessible to the current user

     Returns all campaigns the authenticated user can access for attribution data.
    For founders, this includes their own campaigns.
    For marketing partners, this includes campaigns they've been granted access to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributionCampaignSummaryListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> AttributionCampaignSummaryListEnvelope | Error | None:
    """ List campaigns accessible to the current user

     Returns all campaigns the authenticated user can access for attribution data.
    For founders, this includes their own campaigns.
    For marketing partners, this includes campaigns they've been granted access to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributionCampaignSummaryListEnvelope | Error
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[AttributionCampaignSummaryListEnvelope | Error]:
    """ List campaigns accessible to the current user

     Returns all campaigns the authenticated user can access for attribution data.
    For founders, this includes their own campaigns.
    For marketing partners, this includes campaigns they've been granted access to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributionCampaignSummaryListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> AttributionCampaignSummaryListEnvelope | Error | None:
    """ List campaigns accessible to the current user

     Returns all campaigns the authenticated user can access for attribution data.
    For founders, this includes their own campaigns.
    For marketing partners, this includes campaigns they've been granted access to.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributionCampaignSummaryListEnvelope | Error
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
