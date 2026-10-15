from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_syndicate_join_session_body import CreateSyndicateJoinSessionBody
from ...models.create_syndicate_join_session_response_201 import CreateSyndicateJoinSessionResponse201
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    syndicate_id: str,
    *,
    body: CreateSyndicateJoinSessionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/syndicates/{syndicate_id}/join_sessions".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreateSyndicateJoinSessionResponse201 | Error | None:
    if response.status_code == 201:
        response_201 = CreateSyndicateJoinSessionResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreateSyndicateJoinSessionResponse201 | Error]:
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
    body: CreateSyndicateJoinSessionBody,
) -> Response[CreateSyndicateJoinSessionResponse201 | Error]:
    """Create a join session

     Mint a hosted join session that turns an invitee into a member of a
    syndicate you manage. The session is bound to one email; the recipient
    completes the join on `wefunder.com/join/session/{id}`, and you learn the
    outcome by polling this session or via `join_session.*` webhooks.

    Requires `write:syndicate_members` (included in `write:syndicates`),
    operator permission, and an active installation of your app on the
    syndicate. Phase 1 supports `mode: hosted` only.

    Args:
        syndicate_id (str):
        body (CreateSyndicateJoinSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSyndicateJoinSessionResponse201 | Error]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateSyndicateJoinSessionBody,
) -> CreateSyndicateJoinSessionResponse201 | Error | None:
    """Create a join session

     Mint a hosted join session that turns an invitee into a member of a
    syndicate you manage. The session is bound to one email; the recipient
    completes the join on `wefunder.com/join/session/{id}`, and you learn the
    outcome by polling this session or via `join_session.*` webhooks.

    Requires `write:syndicate_members` (included in `write:syndicates`),
    operator permission, and an active installation of your app on the
    syndicate. Phase 1 supports `mode: hosted` only.

    Args:
        syndicate_id (str):
        body (CreateSyndicateJoinSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSyndicateJoinSessionResponse201 | Error
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateSyndicateJoinSessionBody,
) -> Response[CreateSyndicateJoinSessionResponse201 | Error]:
    """Create a join session

     Mint a hosted join session that turns an invitee into a member of a
    syndicate you manage. The session is bound to one email; the recipient
    completes the join on `wefunder.com/join/session/{id}`, and you learn the
    outcome by polling this session or via `join_session.*` webhooks.

    Requires `write:syndicate_members` (included in `write:syndicates`),
    operator permission, and an active installation of your app on the
    syndicate. Phase 1 supports `mode: hosted` only.

    Args:
        syndicate_id (str):
        body (CreateSyndicateJoinSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateSyndicateJoinSessionResponse201 | Error]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateSyndicateJoinSessionBody,
) -> CreateSyndicateJoinSessionResponse201 | Error | None:
    """Create a join session

     Mint a hosted join session that turns an invitee into a member of a
    syndicate you manage. The session is bound to one email; the recipient
    completes the join on `wefunder.com/join/session/{id}`, and you learn the
    outcome by polling this session or via `join_session.*` webhooks.

    Requires `write:syndicate_members` (included in `write:syndicates`),
    operator permission, and an active installation of your app on the
    syndicate. Phase 1 supports `mode: hosted` only.

    Args:
        syndicate_id (str):
        body (CreateSyndicateJoinSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateSyndicateJoinSessionResponse201 | Error
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            body=body,
        )
    ).parsed
