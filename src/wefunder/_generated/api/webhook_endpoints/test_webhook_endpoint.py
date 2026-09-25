from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error import Error
from ...models.test_webhook_endpoint_body import TestWebhookEndpointBody
from ...models.webhook_endpoint_test_result_envelope import WebhookEndpointTestResultEnvelope
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    external_id: str,
    *,
    body: TestWebhookEndpointBody | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook_endpoints/{external_id}/test".format(external_id=quote(str(external_id), safe=""),),
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Error | WebhookEndpointTestResultEnvelope | None:
    if response.status_code == 200:
        response_200 = WebhookEndpointTestResultEnvelope.from_dict(response.json())



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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())



        return response_422

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Error | WebhookEndpointTestResultEnvelope]:
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
    body: TestWebhookEndpointBody | Unset = UNSET,

) -> Response[Error | WebhookEndpointTestResultEnvelope]:
    """ Send a test event

     Sends a real, signed example event (fake values) using the production envelope,
    signature scheme, and transport, and reports the outcome inline. Does not affect
    delivery health. Rate-limited to 10 per minute per endpoint. Investor email appears
    in the example only if your application holds `read:investors:pii`, matching what
    real deliveries can carry.

    Args:
        external_id (str):
        body (TestWebhookEndpointBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookEndpointTestResultEnvelope]
     """


    kwargs = _get_kwargs(
        external_id=external_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: TestWebhookEndpointBody | Unset = UNSET,

) -> Error | WebhookEndpointTestResultEnvelope | None:
    """ Send a test event

     Sends a real, signed example event (fake values) using the production envelope,
    signature scheme, and transport, and reports the outcome inline. Does not affect
    delivery health. Rate-limited to 10 per minute per endpoint. Investor email appears
    in the example only if your application holds `read:investors:pii`, matching what
    real deliveries can carry.

    Args:
        external_id (str):
        body (TestWebhookEndpointBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookEndpointTestResultEnvelope
     """


    return sync_detailed(
        external_id=external_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: TestWebhookEndpointBody | Unset = UNSET,

) -> Response[Error | WebhookEndpointTestResultEnvelope]:
    """ Send a test event

     Sends a real, signed example event (fake values) using the production envelope,
    signature scheme, and transport, and reports the outcome inline. Does not affect
    delivery health. Rate-limited to 10 per minute per endpoint. Investor email appears
    in the example only if your application holds `read:investors:pii`, matching what
    real deliveries can carry.

    Args:
        external_id (str):
        body (TestWebhookEndpointBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookEndpointTestResultEnvelope]
     """


    kwargs = _get_kwargs(
        external_id=external_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    external_id: str,
    *,
    client: AuthenticatedClient,
    body: TestWebhookEndpointBody | Unset = UNSET,

) -> Error | WebhookEndpointTestResultEnvelope | None:
    """ Send a test event

     Sends a real, signed example event (fake values) using the production envelope,
    signature scheme, and transport, and reports the outcome inline. Does not affect
    delivery health. Rate-limited to 10 per minute per endpoint. Investor email appears
    in the example only if your application holds `read:investors:pii`, matching what
    real deliveries can carry.

    Args:
        external_id (str):
        body (TestWebhookEndpointBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookEndpointTestResultEnvelope
     """


    return (await asyncio_detailed(
        external_id=external_id,
client=client,
body=body,

    )).parsed
