from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.member_link_envelope import MemberLinkEnvelope
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/member_links/{id}/cancel".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | MemberLinkEnvelope | None:
    if response.status_code == 200:
        response_200 = MemberLinkEnvelope.from_dict(response.json())

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
) -> Response[Error | MemberLinkEnvelope]:
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
) -> Response[Error | MemberLinkEnvelope]:
    """Cancel a member link

     Retracts the invitation. Idempotent. The link grants nothing new afterwards:
    a checkout started after the cancel, including the same member's next
    investment, is priced at standard terms. Investments already made through the
    link keep the terms they were made at. A link nobody invested through is
    also released from the account you pre-bound it to. Revoking your install
    cancels every member link it minted that no investment went through (same
    release); links an investment went through stand.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MemberLinkEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Error | MemberLinkEnvelope | None:
    """Cancel a member link

     Retracts the invitation. Idempotent. The link grants nothing new afterwards:
    a checkout started after the cancel, including the same member's next
    investment, is priced at standard terms. Investments already made through the
    link keep the terms they were made at. A link nobody invested through is
    also released from the account you pre-bound it to. Revoking your install
    cancels every member link it minted that no investment went through (same
    release); links an investment went through stand.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MemberLinkEnvelope
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | MemberLinkEnvelope]:
    """Cancel a member link

     Retracts the invitation. Idempotent. The link grants nothing new afterwards:
    a checkout started after the cancel, including the same member's next
    investment, is priced at standard terms. Investments already made through the
    link keep the terms they were made at. A link nobody invested through is
    also released from the account you pre-bound it to. Revoking your install
    cancels every member link it minted that no investment went through (same
    release); links an investment went through stand.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | MemberLinkEnvelope]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Error | MemberLinkEnvelope | None:
    """Cancel a member link

     Retracts the invitation. Idempotent. The link grants nothing new afterwards:
    a checkout started after the cancel, including the same member's next
    investment, is priced at standard terms. Investments already made through the
    link keep the terms they were made at. A link nobody invested through is
    also released from the account you pre-bound it to. Revoking your install
    cancels every member link it minted that no investment went through (same
    release); links an investment went through stand.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | MemberLinkEnvelope
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
