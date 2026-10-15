from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_syndicate_join_sessions_response_200 import ListSyndicateJoinSessionsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    syndicate_id: str,
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
        "url": "/syndicates/{syndicate_id}/join_sessions".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ListSyndicateJoinSessionsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListSyndicateJoinSessionsResponse200.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ListSyndicateJoinSessionsResponse200]:
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
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | ListSyndicateJoinSessionsResponse200]:
    """List join sessions

     List the join sessions your app's installation minted on this syndicate.
    Sessions are install-scoped: you only see the ones your own install created.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListSyndicateJoinSessionsResponse200]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | ListSyndicateJoinSessionsResponse200 | None:
    """List join sessions

     List the join sessions your app's installation minted on this syndicate.
    Sessions are install-scoped: you only see the ones your own install created.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListSyndicateJoinSessionsResponse200
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        client=client,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | ListSyndicateJoinSessionsResponse200]:
    """List join sessions

     List the join sessions your app's installation minted on this syndicate.
    Sessions are install-scoped: you only see the ones your own install created.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ListSyndicateJoinSessionsResponse200]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | ListSyndicateJoinSessionsResponse200 | None:
    """List join sessions

     List the join sessions your app's installation minted on this syndicate.
    Sessions are install-scoped: you only see the ones your own install created.

    Args:
        syndicate_id (str):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ListSyndicateJoinSessionsResponse200
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
