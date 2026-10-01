from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_syndicate_members_accredited import ListSyndicateMembersAccredited
from ...models.list_syndicate_members_has_invested import ListSyndicateMembersHasInvested
from ...models.list_syndicate_members_permission import ListSyndicateMembersPermission
from ...models.list_syndicate_members_sort import ListSyndicateMembersSort
from ...models.syndicate_member_list_envelope import SyndicateMemberListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    syndicate_id: str,
    *,
    role: str | Unset = UNSET,
    permission: ListSyndicateMembersPermission | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: ListSyndicateMembersSort | Unset = UNSET,
    has_invested: ListSyndicateMembersHasInvested | Unset = UNSET,
    accredited: ListSyndicateMembersAccredited | Unset = UNSET,
    tag: str | Unset = UNSET,
    location: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["role"] = role

    json_permission: str | Unset = UNSET
    if not isinstance(permission, Unset):
        json_permission = permission.value

    params["permission"] = json_permission

    params["search"] = search

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_has_invested: str | Unset = UNSET
    if not isinstance(has_invested, Unset):
        json_has_invested = has_invested.value

    params["has_invested"] = json_has_invested

    json_accredited: str | Unset = UNSET
    if not isinstance(accredited, Unset):
        json_accredited = accredited.value

    params["accredited"] = json_accredited

    params["tag"] = tag

    params["location"] = location

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/syndicates/{syndicate_id}/members".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SyndicateMemberListEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateMemberListEnvelope.from_dict(response.json())

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
) -> Response[Error | SyndicateMemberListEnvelope]:
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
    role: str | Unset = UNSET,
    permission: ListSyndicateMembersPermission | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: ListSyndicateMembersSort | Unset = UNSET,
    has_invested: ListSyndicateMembersHasInvested | Unset = UNSET,
    accredited: ListSyndicateMembersAccredited | Unset = UNSET,
    tag: str | Unset = UNSET,
    location: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | SyndicateMemberListEnvelope]:
    """List members

     Returns the member directory for a syndicate with role, status, tags, sidebar notes,
    and investment history summaries. Supports filtering, sorting, search, and pagination.

    Args:
        syndicate_id (str):
        role (str | Unset):
        permission (ListSyndicateMembersPermission | Unset):
        search (str | Unset):
        sort (ListSyndicateMembersSort | Unset):
        has_invested (ListSyndicateMembersHasInvested | Unset):
        accredited (ListSyndicateMembersAccredited | Unset):
        tag (str | Unset):
        location (str | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateMemberListEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        role=role,
        permission=permission,
        search=search,
        sort=sort,
        has_invested=has_invested,
        accredited=accredited,
        tag=tag,
        location=location,
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
    role: str | Unset = UNSET,
    permission: ListSyndicateMembersPermission | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: ListSyndicateMembersSort | Unset = UNSET,
    has_invested: ListSyndicateMembersHasInvested | Unset = UNSET,
    accredited: ListSyndicateMembersAccredited | Unset = UNSET,
    tag: str | Unset = UNSET,
    location: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | SyndicateMemberListEnvelope | None:
    """List members

     Returns the member directory for a syndicate with role, status, tags, sidebar notes,
    and investment history summaries. Supports filtering, sorting, search, and pagination.

    Args:
        syndicate_id (str):
        role (str | Unset):
        permission (ListSyndicateMembersPermission | Unset):
        search (str | Unset):
        sort (ListSyndicateMembersSort | Unset):
        has_invested (ListSyndicateMembersHasInvested | Unset):
        accredited (ListSyndicateMembersAccredited | Unset):
        tag (str | Unset):
        location (str | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateMemberListEnvelope
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        client=client,
        role=role,
        permission=permission,
        search=search,
        sort=sort,
        has_invested=has_invested,
        accredited=accredited,
        tag=tag,
        location=location,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    role: str | Unset = UNSET,
    permission: ListSyndicateMembersPermission | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: ListSyndicateMembersSort | Unset = UNSET,
    has_invested: ListSyndicateMembersHasInvested | Unset = UNSET,
    accredited: ListSyndicateMembersAccredited | Unset = UNSET,
    tag: str | Unset = UNSET,
    location: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[Error | SyndicateMemberListEnvelope]:
    """List members

     Returns the member directory for a syndicate with role, status, tags, sidebar notes,
    and investment history summaries. Supports filtering, sorting, search, and pagination.

    Args:
        syndicate_id (str):
        role (str | Unset):
        permission (ListSyndicateMembersPermission | Unset):
        search (str | Unset):
        sort (ListSyndicateMembersSort | Unset):
        has_invested (ListSyndicateMembersHasInvested | Unset):
        accredited (ListSyndicateMembersAccredited | Unset):
        tag (str | Unset):
        location (str | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateMemberListEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        role=role,
        permission=permission,
        search=search,
        sort=sort,
        has_invested=has_invested,
        accredited=accredited,
        tag=tag,
        location=location,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    role: str | Unset = UNSET,
    permission: ListSyndicateMembersPermission | Unset = UNSET,
    search: str | Unset = UNSET,
    sort: ListSyndicateMembersSort | Unset = UNSET,
    has_invested: ListSyndicateMembersHasInvested | Unset = UNSET,
    accredited: ListSyndicateMembersAccredited | Unset = UNSET,
    tag: str | Unset = UNSET,
    location: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Error | SyndicateMemberListEnvelope | None:
    """List members

     Returns the member directory for a syndicate with role, status, tags, sidebar notes,
    and investment history summaries. Supports filtering, sorting, search, and pagination.

    Args:
        syndicate_id (str):
        role (str | Unset):
        permission (ListSyndicateMembersPermission | Unset):
        search (str | Unset):
        sort (ListSyndicateMembersSort | Unset):
        has_invested (ListSyndicateMembersHasInvested | Unset):
        accredited (ListSyndicateMembersAccredited | Unset):
        tag (str | Unset):
        location (str | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateMemberListEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            role=role,
            permission=permission,
            search=search,
            sort=sort,
            has_invested=has_invested,
            accredited=accredited,
            tag=tag,
            location=location,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
