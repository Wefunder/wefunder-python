from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.deal_investor_list_envelope import DealInvestorListEnvelope
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    syndicate_id: str,
    fundraise_id: str,
    *,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/deals/{fundraise_id}/investors".format(syndicate_id=quote(str(syndicate_id), safe=""),fundraise_id=quote(str(fundraise_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DealInvestorListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = DealInvestorListEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DealInvestorListEnvelope | Error]:
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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,

) -> Response[DealInvestorListEnvelope | Error]:
    """ List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DealInvestorListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,
cursor=cursor,
limit=limit,

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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,

) -> DealInvestorListEnvelope | Error | None:
    """ List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DealInvestorListEnvelope | Error
     """


    return sync_detailed(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,
client=client,
cursor=cursor,
limit=limit,

    ).parsed

async def asyncio_detailed(
    syndicate_id: str,
    fundraise_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,

) -> Response[DealInvestorListEnvelope | Error]:
    """ List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DealInvestorListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,
cursor=cursor,
limit=limit,

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
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,

) -> DealInvestorListEnvelope | Error | None:
    """ List deal investors

     Returns syndicate members who invested in this deal. Results are scoped to
    syndicate member user IDs only and sorted by amount descending.

    The `user_email` field is **moderator-only** — it returns null for non-moderator
    callers (i.e., users who are not a manager/operator of the syndicate).

    All monetary values are strings representing cents to avoid floating-point precision issues.

    Args:
        syndicate_id (str):
        fundraise_id (str):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DealInvestorListEnvelope | Error
     """


    return (await asyncio_detailed(
        syndicate_id=syndicate_id,
fundraise_id=fundraise_id,
client=client,
cursor=cursor,
limit=limit,

    )).parsed
