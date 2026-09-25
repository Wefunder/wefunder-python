from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.delete_webhook_endpoint_response_200 import DeleteWebhookEndpointResponse200
from ...models.error import Error
from typing import cast



def _get_kwargs(
    external_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/webhook_endpoints/{external_id}".format(external_id=quote(str(external_id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeleteWebhookEndpointResponse200 | Error | None:
    if response.status_code == 200:
        response_200 = DeleteWebhookEndpointResponse200.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeleteWebhookEndpointResponse200 | Error]:
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

) -> Response[DeleteWebhookEndpointResponse200 | Error]:
    """ Remove a webhook endpoint

     Stops deliveries immediately. The endpoint is retained as removed and cannot be restored.
    Returns `403 manage_endpoints_on_live_api` on the sandbox API; use the live API.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookEndpointResponse200 | Error]
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

) -> DeleteWebhookEndpointResponse200 | Error | None:
    """ Remove a webhook endpoint

     Stops deliveries immediately. The endpoint is retained as removed and cannot be restored.
    Returns `403 manage_endpoints_on_live_api` on the sandbox API; use the live API.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookEndpointResponse200 | Error
     """


    return sync_detailed(
        external_id=external_id,
client=client,

    ).parsed

async def asyncio_detailed(
    external_id: str,
    *,
    client: AuthenticatedClient,

) -> Response[DeleteWebhookEndpointResponse200 | Error]:
    """ Remove a webhook endpoint

     Stops deliveries immediately. The endpoint is retained as removed and cannot be restored.
    Returns `403 manage_endpoints_on_live_api` on the sandbox API; use the live API.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteWebhookEndpointResponse200 | Error]
     """


    kwargs = _get_kwargs(
        external_id=external_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    external_id: str,
    *,
    client: AuthenticatedClient,

) -> DeleteWebhookEndpointResponse200 | Error | None:
    """ Remove a webhook endpoint

     Stops deliveries immediately. The endpoint is retained as removed and cannot be restored.
    Returns `403 manage_endpoints_on_live_api` on the sandbox API; use the live API.

    Args:
        external_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteWebhookEndpointResponse200 | Error
     """


    return (await asyncio_detailed(
        external_id=external_id,
client=client,

    )).parsed
