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
        "method": "put",
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
    """Follow a company

     Follow the company for the authenticated user — exactly what pressing Follow on its
    Wefunder page does, side effects included (the company counts the user as a follower and
    may be notified; the user receives the company's updates). Idempotent: following an
    already-followed company returns `changed: false`. `404` for a company the site would not
    show this user. Requires `write:follows`, which the user grants explicitly; it is never
    implied by `read:mcp`.

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
    """Follow a company

     Follow the company for the authenticated user — exactly what pressing Follow on its
    Wefunder page does, side effects included (the company counts the user as a follower and
    may be notified; the user receives the company's updates). Idempotent: following an
    already-followed company returns `changed: false`. `404` for a company the site would not
    show this user. Requires `write:follows`, which the user grants explicitly; it is never
    implied by `read:mcp`.

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
    """Follow a company

     Follow the company for the authenticated user — exactly what pressing Follow on its
    Wefunder page does, side effects included (the company counts the user as a follower and
    may be notified; the user receives the company's updates). Idempotent: following an
    already-followed company returns `changed: false`. `404` for a company the site would not
    show this user. Requires `write:follows`, which the user grants explicitly; it is never
    implied by `read:mcp`.

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
    """Follow a company

     Follow the company for the authenticated user — exactly what pressing Follow on its
    Wefunder page does, side effects included (the company counts the user as a follower and
    may be notified; the user receives the company's updates). Idempotent: following an
    already-followed company returns `changed: false`. `404` for a company the site would not
    show this user. Requires `write:follows`, which the user grants explicitly; it is never
    implied by `read:mcp`.

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
