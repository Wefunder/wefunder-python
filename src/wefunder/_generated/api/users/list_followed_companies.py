from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.followed_company_list_envelope import FollowedCompanyListEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["per_page"] = per_page


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/users/me/follows",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | FollowedCompanyListEnvelope | None:
    if response.status_code == 200:
        response_200 = FollowedCompanyListEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | FollowedCompanyListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,

) -> Response[Error | FollowedCompanyListEnvelope]:
    """ List the companies you follow

     The authenticated user's watchlist — the companies they follow on wefunder.com (the same
    rows the site's Follow button writes), newest first. Each entry is in the search-result
    shape (`co_` id, name, tagline, URL, logo, `raising`, `profile_available`) plus
    `followed_at`. The list owner sees every company they follow.

    Args:
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FollowedCompanyListEnvelope]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
per_page=per_page,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,

) -> Error | FollowedCompanyListEnvelope | None:
    """ List the companies you follow

     The authenticated user's watchlist — the companies they follow on wefunder.com (the same
    rows the site's Follow button writes), newest first. Each entry is in the search-result
    shape (`co_` id, name, tagline, URL, logo, `raising`, `profile_available`) plus
    `followed_at`. The list owner sees every company they follow.

    Args:
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FollowedCompanyListEnvelope
     """


    return sync_detailed(
        client=client,
cursor=cursor,
per_page=per_page,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,

) -> Response[Error | FollowedCompanyListEnvelope]:
    """ List the companies you follow

     The authenticated user's watchlist — the companies they follow on wefunder.com (the same
    rows the site's Follow button writes), newest first. Each entry is in the search-result
    shape (`co_` id, name, tagline, URL, logo, `raising`, `profile_available`) plus
    `followed_at`. The list owner sees every company they follow.

    Args:
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | FollowedCompanyListEnvelope]
     """


    kwargs = _get_kwargs(
        cursor=cursor,
per_page=per_page,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,

) -> Error | FollowedCompanyListEnvelope | None:
    """ List the companies you follow

     The authenticated user's watchlist — the companies they follow on wefunder.com (the same
    rows the site's Follow button writes), newest first. Each entry is in the search-result
    shape (`co_` id, name, tagline, URL, logo, `raising`, `profile_available`) plus
    `followed_at`. The list owner sees every company they follow.

    Args:
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | FollowedCompanyListEnvelope
     """


    return (await asyncio_detailed(
        client=client,
cursor=cursor,
per_page=per_page,

    )).parsed
