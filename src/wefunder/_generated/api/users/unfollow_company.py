from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.follow_state_envelope import FollowStateEnvelope
from ...types import Response


def _get_kwargs(
    company_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/users/me/follows/{company_id}".format(
            company_id=quote(str(company_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | Error | FollowStateEnvelope | None:
    if response.status_code == 200:
        response_200 = FollowStateEnvelope.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | Error | FollowStateEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error | FollowStateEnvelope]:
    """Unfollow a company

     Unfollow the company for the authenticated user. Idempotent (`changed` is false when they were not
    following it). No visibility gate: a follow you hold is always undoable, even for a company since
    hidden. Requires `write:follows`.

    Args:
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | FollowStateEnvelope]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    company_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Error | FollowStateEnvelope | None:
    """Unfollow a company

     Unfollow the company for the authenticated user. Idempotent (`changed` is false when they were not
    following it). No visibility gate: a follow you hold is always undoable, even for a company since
    hidden. Requires `write:follows`.

    Args:
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | FollowStateEnvelope
    """

    return sync_detailed(
        company_id=company_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    company_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | Error | FollowStateEnvelope]:
    """Unfollow a company

     Unfollow the company for the authenticated user. Idempotent (`changed` is false when they were not
    following it). No visibility gate: a follow you hold is always undoable, even for a company since
    hidden. Requires `write:follows`.

    Args:
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | FollowStateEnvelope]
    """

    kwargs = _get_kwargs(
        company_id=company_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    company_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | Error | FollowStateEnvelope | None:
    """Unfollow a company

     Unfollow the company for the authenticated user. Idempotent (`changed` is false when they were not
    following it). No visibility gate: a follow you hold is always undoable, even for a company since
    hidden. Requires `write:follows`.

    Args:
        company_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | FollowStateEnvelope
    """

    return (
        await asyncio_detailed(
            company_id=company_id,
            client=client,
        )
    ).parsed
