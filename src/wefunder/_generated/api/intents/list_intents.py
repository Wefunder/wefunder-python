from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.intent_list_envelope import IntentListEnvelope
from ...models.list_intents_status import ListIntentsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListIntentsStatus | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["resource_type"] = resource_type

    params["resource_id"] = resource_id

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/intents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | IntentListEnvelope | None:
    if response.status_code == 200:
        response_200 = IntentListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | IntentListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: ListIntentsStatus | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[Error | IntentListEnvelope]:
    """List intents

     List intents created by the current token, optionally filtered by status or resource.

    Args:
        status (ListIntentsStatus | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IntentListEnvelope]
    """

    kwargs = _get_kwargs(
        status=status,
        resource_type=resource_type,
        resource_id=resource_id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: ListIntentsStatus | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> Error | IntentListEnvelope | None:
    """List intents

     List intents created by the current token, optionally filtered by status or resource.

    Args:
        status (ListIntentsStatus | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IntentListEnvelope
    """

    return sync_detailed(
        client=client,
        status=status,
        resource_type=resource_type,
        resource_id=resource_id,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: ListIntentsStatus | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> Response[Error | IntentListEnvelope]:
    """List intents

     List intents created by the current token, optionally filtered by status or resource.

    Args:
        status (ListIntentsStatus | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | IntentListEnvelope]
    """

    kwargs = _get_kwargs(
        status=status,
        resource_type=resource_type,
        resource_id=resource_id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: ListIntentsStatus | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    cursor: str | Unset = UNSET,
    limit: int | Unset = 25,
) -> Error | IntentListEnvelope | None:
    """List intents

     List intents created by the current token, optionally filtered by status or resource.

    Args:
        status (ListIntentsStatus | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        cursor (str | Unset):
        limit (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | IntentListEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            resource_type=resource_type,
            resource_id=resource_id,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
