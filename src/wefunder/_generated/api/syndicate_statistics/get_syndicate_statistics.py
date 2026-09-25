from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.syndicate_statistics_envelope import SyndicateStatisticsEnvelope
from typing import cast



def _get_kwargs(
    syndicate_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/statistics".format(syndicate_id=quote(str(syndicate_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | SyndicateStatisticsEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateStatisticsEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | SyndicateStatisticsEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | SyndicateStatisticsEnvelope]:
    """ Get syndicate statistics

     Returns aggregate metrics for a syndicate including member counts, deal counts,
    total raised, and recent activity.

    `total_raised` and `total_investors` are computed from directory-selected deals
    (one per company). `total_deals` and `live_deals` use all linked deals.

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateStatisticsEnvelope]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | SyndicateStatisticsEnvelope | None:
    """ Get syndicate statistics

     Returns aggregate metrics for a syndicate including member counts, deal counts,
    total raised, and recent activity.

    `total_raised` and `total_investors` are computed from directory-selected deals
    (one per company). `total_deals` and `live_deals` use all linked deals.

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateStatisticsEnvelope
     """


    return sync_detailed(
        syndicate_id=syndicate_id,
client=client,

    ).parsed

async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Error | SyndicateStatisticsEnvelope]:
    """ Get syndicate statistics

     Returns aggregate metrics for a syndicate including member counts, deal counts,
    total raised, and recent activity.

    `total_raised` and `total_investors` are computed from directory-selected deals
    (one per company). `total_deals` and `live_deals` use all linked deals.

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateStatisticsEnvelope]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,

) -> Error | SyndicateStatisticsEnvelope | None:
    """ Get syndicate statistics

     Returns aggregate metrics for a syndicate including member counts, deal counts,
    total raised, and recent activity.

    `total_raised` and `total_investors` are computed from directory-selected deals
    (one per company). `total_deals` and `live_deals` use all linked deals.

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateStatisticsEnvelope
     """


    return (await asyncio_detailed(
        syndicate_id=syndicate_id,
client=client,

    )).parsed
