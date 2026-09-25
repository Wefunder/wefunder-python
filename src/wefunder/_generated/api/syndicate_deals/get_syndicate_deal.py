from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.syndicate_deal_detail_envelope import SyndicateDealDetailEnvelope
from typing import cast



def _get_kwargs(
    syndicate_id: str,
    fundraise_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/deals/{fundraise_id}".format(syndicate_id=quote(str(syndicate_id), safe=""),fundraise_id=quote(str(fundraise_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SyndicateDealDetailEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateDealDetailEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SyndicateDealDetailEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | SyndicateDealDetailEnvelope]:
    """ Get deal details

     Returns full details for a specific deal including investor breakdown.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDealDetailEnvelope]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | SyndicateDealDetailEnvelope | None:
    """ Get deal details

     Returns full details for a specific deal including investor breakdown.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDealDetailEnvelope
     """


    return sync_detailed(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,
client=client,

    ).parsed

async def asyncio_detailed(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | SyndicateDealDetailEnvelope]:
    """ Get deal details

     Returns full details for a specific deal including investor breakdown.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDealDetailEnvelope]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | SyndicateDealDetailEnvelope | None:
    """ Get deal details

     Returns full details for a specific deal including investor breakdown.

    Args:
        syndicate_id (str):
        fundraise_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDealDetailEnvelope
     """


    return (await asyncio_detailed(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,
client=client,

    )).parsed
