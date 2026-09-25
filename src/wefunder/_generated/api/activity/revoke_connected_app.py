from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connected_app_revocation_envelope import ConnectedAppRevocationEnvelope
from ...models.error import Error
from typing import cast



def _get_kwargs(
    app_id: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/connected-apps/{app_id}".format(app_id=quote(str(app_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectedAppRevocationEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = ConnectedAppRevocationEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ConnectedAppRevocationEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    app_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[ConnectedAppRevocationEnvelope | Error]:
    """ Revoke connected app

     Revoke all tokens for this app. Any pending intents from this app are automatically expired.

    Args:
        app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppRevocationEnvelope | Error]
     """


    kwargs = _get_kwargs(
        app_id=app_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    app_id: int,
    *,
    client: AuthenticatedClient,

) -> ConnectedAppRevocationEnvelope | Error | None:
    """ Revoke connected app

     Revoke all tokens for this app. Any pending intents from this app are automatically expired.

    Args:
        app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppRevocationEnvelope | Error
     """


    return sync_detailed(
        app_id=app_id,
client=client,

    ).parsed

async def asyncio_detailed(
    app_id: int,
    *,
    client: AuthenticatedClient,

) -> Response[ConnectedAppRevocationEnvelope | Error]:
    """ Revoke connected app

     Revoke all tokens for this app. Any pending intents from this app are automatically expired.

    Args:
        app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectedAppRevocationEnvelope | Error]
     """


    kwargs = _get_kwargs(
        app_id=app_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    app_id: int,
    *,
    client: AuthenticatedClient,

) -> ConnectedAppRevocationEnvelope | Error | None:
    """ Revoke connected app

     Revoke all tokens for this app. Any pending intents from this app are automatically expired.

    Args:
        app_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectedAppRevocationEnvelope | Error
     """


    return (await asyncio_detailed(
        app_id=app_id,
client=client,

    )).parsed
