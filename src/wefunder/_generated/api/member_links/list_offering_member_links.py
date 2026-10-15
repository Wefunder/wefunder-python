from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.member_link_list_envelope import MemberLinkListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    cursor: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/offerings/{id}/member_links".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MemberLinkListEnvelope | None:
    if response.status_code == 200:
        response_200 = MemberLinkListEnvelope.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | MemberLinkListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
) -> Response[Error | MemberLinkListEnvelope]:
    """List member links

     The member links **your install** minted on this offering, newest first.
    Another app installed on the same offering never sees them, and they never
    appear in `/invite_links`. Requires a syndicate- or company-owned token of an
    app installed on the offering's syndicate or company.

    Args:
        id (str):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MemberLinkListEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
) -> Error | MemberLinkListEnvelope | None:
    """List member links

     The member links **your install** minted on this offering, newest first.
    Another app installed on the same offering never sees them, and they never
    appear in `/invite_links`. Requires a syndicate- or company-owned token of an
    app installed on the offering's syndicate or company.

    Args:
        id (str):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MemberLinkListEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
) -> Response[Error | MemberLinkListEnvelope]:
    """List member links

     The member links **your install** minted on this offering, newest first.
    Another app installed on the same offering never sees them, and they never
    appear in `/invite_links`. Requires a syndicate- or company-owned token of an
    app installed on the offering's syndicate or company.

    Args:
        id (str):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MemberLinkListEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
) -> Error | MemberLinkListEnvelope | None:
    """List member links

     The member links **your install** minted on this offering, newest first.
    Another app installed on the same offering never sees them, and they never
    appear in `/invite_links`. Requires a syndicate- or company-owned token of an
    app installed on the offering's syndicate or company.

    Args:
        id (str):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MemberLinkListEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            cursor=cursor,
        )
    ).parsed
