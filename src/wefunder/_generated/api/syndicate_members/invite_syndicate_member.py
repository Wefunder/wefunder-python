from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.invite_syndicate_member_body import InviteSyndicateMemberBody
from ...models.syndicate_member_envelope import SyndicateMemberEnvelope
from ...types import Response


def _get_kwargs(
    syndicate_id: str,
    *,
    body: InviteSyndicateMemberBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/syndicates/{syndicate_id}/members/invite".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SyndicateMemberEnvelope | None:
    if response.status_code == 201:
        response_201 = SyndicateMemberEnvelope.from_dict(response.json())

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
) -> Response[Error | SyndicateMemberEnvelope]:
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
    body: InviteSyndicateMemberBody,
) -> Response[Error | SyndicateMemberEnvelope]:
    """Invite member

     Send an invitation to join the syndicate by email.

    Args:
        syndicate_id (str):
        body (InviteSyndicateMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateMemberEnvelope]
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
    body: InviteSyndicateMemberBody,
) -> Error | SyndicateMemberEnvelope | None:
    """Invite member

     Send an invitation to join the syndicate by email.

    Args:
        syndicate_id (str):
        body (InviteSyndicateMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateMemberEnvelope
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
    body: InviteSyndicateMemberBody,
) -> Response[Error | SyndicateMemberEnvelope]:
    """Invite member

     Send an invitation to join the syndicate by email.

    Args:
        syndicate_id (str):
        body (InviteSyndicateMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateMemberEnvelope]
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
    body: InviteSyndicateMemberBody,
) -> Error | SyndicateMemberEnvelope | None:
    """Invite member

     Send an invitation to join the syndicate by email.

    Args:
        syndicate_id (str):
        body (InviteSyndicateMemberBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateMemberEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            body=body,
        )
    ).parsed
