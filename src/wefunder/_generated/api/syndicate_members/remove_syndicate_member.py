from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    syndicate_id: str,
    member_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/syndicates/{syndicate_id}/members/{member_id}".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
            member_id=quote(str(member_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | None:
    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Remove member (requires intent)

     Removing a member is irreversible and requires human approval through the Intent system.
    This endpoint always returns 422 with a `use_intents` error directing you to
    `POST /intents` with action `syndicates.remove_member`.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        member_id=member_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | None:
    """Remove member (requires intent)

     Removing a member is irreversible and requires human approval through the Intent system.
    This endpoint always returns 422 with a `use_intents` error directing you to
    `POST /intents` with action `syndicates.remove_member`.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        member_id=member_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error]:
    """Remove member (requires intent)

     Removing a member is irreversible and requires human approval through the Intent system.
    This endpoint always returns 422 with a `use_intents` error directing you to
    `POST /intents` with action `syndicates.remove_member`.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        member_id=member_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    member_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | None:
    """Remove member (requires intent)

     Removing a member is irreversible and requires human approval through the Intent system.
    This endpoint always returns 422 with a `use_intents` error directing you to
    `POST /intents` with action `syndicates.remove_member`.

    Args:
        syndicate_id (str):
        member_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            member_id=member_id,
            client=client,
        )
    ).parsed
