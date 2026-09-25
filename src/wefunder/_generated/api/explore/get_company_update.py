from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_update_envelope import CompanyUpdateEnvelope
from ...models.error import Error
from ...types import Response


def _get_kwargs(
    id: str,
    update_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{id}/updates/{update_id}".format(
            id=quote(str(id), safe=""),
            update_id=quote(str(update_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompanyUpdateEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanyUpdateEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

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
) -> Response[Any | CompanyUpdateEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    update_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CompanyUpdateEnvelope | Error]:
    """Get one company post in full

     One post with its full plain-text content, by the id the list returned. Same visibility as the list;
    a post the tab would not show this viewer is a 404.

    Args:
        id (str):
        update_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyUpdateEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        update_id=update_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    update_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CompanyUpdateEnvelope | Error | None:
    """Get one company post in full

     One post with its full plain-text content, by the id the list returned. Same visibility as the list;
    a post the tab would not show this viewer is a 404.

    Args:
        id (str):
        update_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyUpdateEnvelope | Error
    """

    return sync_detailed(
        id=id,
        update_id=update_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    update_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | CompanyUpdateEnvelope | Error]:
    """Get one company post in full

     One post with its full plain-text content, by the id the list returned. Same visibility as the list;
    a post the tab would not show this viewer is a 404.

    Args:
        id (str):
        update_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyUpdateEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        update_id=update_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    update_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | CompanyUpdateEnvelope | Error | None:
    """Get one company post in full

     One post with its full plain-text content, by the id the list returned. Same visibility as the list;
    a post the tab would not show this viewer is a 404.

    Args:
        id (str):
        update_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyUpdateEnvelope | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            update_id=update_id,
            client=client,
        )
    ).parsed
