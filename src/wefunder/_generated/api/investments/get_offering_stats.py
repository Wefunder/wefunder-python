from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.offering_stats_envelope import OfferingStatsEnvelope
from typing import cast



def _get_kwargs(
    offering_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/offerings/{offering_id}/stats".format(offering_id=quote(str(offering_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | OfferingStatsEnvelope | None:
    if response.status_code == 200:
        response_200 = OfferingStatsEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | OfferingStatsEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    offering_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error | OfferingStatsEnvelope]:
    """ Investment totals for an offering

     Count and committed amount of the founder-visible published records for one offering,
    by status, from the same rows `GET /investments?offering_id=…` lists, so the two
    reconcile. These are **not** the public campaign figures (the progress bar has its own
    rules and sources); they are the sum of the records you can list. Requires the token's
    user to edit the offering's company.

    Args:
        offering_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | OfferingStatsEnvelope]
     """


    kwargs = _get_kwargs(
        offering_id=offering_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    offering_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | OfferingStatsEnvelope | None:
    """ Investment totals for an offering

     Count and committed amount of the founder-visible published records for one offering,
    by status, from the same rows `GET /investments?offering_id=…` lists, so the two
    reconcile. These are **not** the public campaign figures (the progress bar has its own
    rules and sources); they are the sum of the records you can list. Requires the token's
    user to edit the offering's company.

    Args:
        offering_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | OfferingStatsEnvelope
     """


    return sync_detailed(
        offering_id=offering_id,
client=client,

    ).parsed

async def asyncio_detailed(
    offering_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | Error | OfferingStatsEnvelope]:
    """ Investment totals for an offering

     Count and committed amount of the founder-visible published records for one offering,
    by status, from the same rows `GET /investments?offering_id=…` lists, so the two
    reconcile. These are **not** the public campaign figures (the progress bar has its own
    rules and sources); they are the sum of the records you can list. Requires the token's
    user to edit the offering's company.

    Args:
        offering_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | OfferingStatsEnvelope]
     """


    kwargs = _get_kwargs(
        offering_id=offering_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    offering_id: str,
    *,
    client: AuthenticatedClient,

) -> Any | Error | OfferingStatsEnvelope | None:
    """ Investment totals for an offering

     Count and committed amount of the founder-visible published records for one offering,
    by status, from the same rows `GET /investments?offering_id=…` lists, so the two
    reconcile. These are **not** the public campaign figures (the progress bar has its own
    rules and sources); they are the sum of the records you can list. Requires the token's
    user to edit the offering's company.

    Args:
        offering_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | OfferingStatsEnvelope
     """


    return (await asyncio_detailed(
        offering_id=offering_id,
client=client,

    )).parsed
