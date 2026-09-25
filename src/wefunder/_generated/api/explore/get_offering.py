from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.offering_envelope import OfferingEnvelope
from ...types import Response


def _get_kwargs(
    external_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/offerings/{external_id}".format(
            external_id=quote(str(external_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | OfferingEnvelope | None:
    if response.status_code == 200:
        response_200 = OfferingEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())

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
) -> Response[Error | OfferingEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    external_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | OfferingEnvelope]:
    """Get a public offering

     Retrieves a single offering by its id (`ofr_...`).

    With `read:public`, a valid id for a non-public offering (e.g. a private Reg D 506(b)
    round) returns `404` — having an id does not make an offering publicly resolvable. With
    `read:explore` on a user access token, the offering resolves if *that user* may see it on
    wefunder.com (e.g. an accredited-only or invited round), and the response gains
    `publicly_visible` and `invested`.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OfferingEnvelope]
    """

    kwargs = _get_kwargs(
        external_id=external_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    external_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | OfferingEnvelope | None:
    """Get a public offering

     Retrieves a single offering by its id (`ofr_...`).

    With `read:public`, a valid id for a non-public offering (e.g. a private Reg D 506(b)
    round) returns `404` — having an id does not make an offering publicly resolvable. With
    `read:explore` on a user access token, the offering resolves if *that user* may see it on
    wefunder.com (e.g. an accredited-only or invited round), and the response gains
    `publicly_visible` and `invested`.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OfferingEnvelope
    """

    return sync_detailed(
        external_id=external_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    external_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | OfferingEnvelope]:
    """Get a public offering

     Retrieves a single offering by its id (`ofr_...`).

    With `read:public`, a valid id for a non-public offering (e.g. a private Reg D 506(b)
    round) returns `404` — having an id does not make an offering publicly resolvable. With
    `read:explore` on a user access token, the offering resolves if *that user* may see it on
    wefunder.com (e.g. an accredited-only or invited round), and the response gains
    `publicly_visible` and `invested`.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OfferingEnvelope]
    """

    kwargs = _get_kwargs(
        external_id=external_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    external_id: str,
    *,
    client: AuthenticatedClient,
) -> Error | OfferingEnvelope | None:
    """Get a public offering

     Retrieves a single offering by its id (`ofr_...`).

    With `read:public`, a valid id for a non-public offering (e.g. a private Reg D 506(b)
    round) returns `404` — having an id does not make an offering publicly resolvable. With
    `read:explore` on a user access token, the offering resolves if *that user* may see it on
    wefunder.com (e.g. an accredited-only or invited round), and the response gains
    `publicly_visible` and `invested`.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OfferingEnvelope
    """

    return (
        await asyncio_detailed(
            external_id=external_id,
            client=client,
        )
    ).parsed
