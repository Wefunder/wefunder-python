from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_webhook_endpoint_body import CreateWebhookEndpointBody
from ...models.error import Error
from ...models.webhook_endpoint_envelope import WebhookEndpointEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: CreateWebhookEndpointBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/webhook_endpoints",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | WebhookEndpointEnvelope | None:
    if response.status_code == 201:
        response_201 = WebhookEndpointEnvelope.from_dict(response.json())

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
) -> Response[Error | WebhookEndpointEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookEndpointBody,
) -> Response[Error | WebhookEndpointEnvelope]:
    """Create a webhook endpoint

     Registers an endpoint for your application. The response is the only time the
    signing `secret` is returned; store it to verify signatures. Requires an
    owner, admin, or developer role in the application's organization.

    On the sandbox API this returns `403 manage_endpoints_on_live_api`: create test
    endpoints through the live API with `mode: "test"`, and they are mirrored into sandbox.

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookEndpointEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookEndpointBody,
) -> Error | WebhookEndpointEnvelope | None:
    """Create a webhook endpoint

     Registers an endpoint for your application. The response is the only time the
    signing `secret` is returned; store it to verify signatures. Requires an
    owner, admin, or developer role in the application's organization.

    On the sandbox API this returns `403 manage_endpoints_on_live_api`: create test
    endpoints through the live API with `mode: "test"`, and they are mirrored into sandbox.

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookEndpointEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookEndpointBody,
) -> Response[Error | WebhookEndpointEnvelope]:
    """Create a webhook endpoint

     Registers an endpoint for your application. The response is the only time the
    signing `secret` is returned; store it to verify signatures. Requires an
    owner, admin, or developer role in the application's organization.

    On the sandbox API this returns `403 manage_endpoints_on_live_api`: create test
    endpoints through the live API with `mode: "test"`, and they are mirrored into sandbox.

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | WebhookEndpointEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateWebhookEndpointBody,
) -> Error | WebhookEndpointEnvelope | None:
    """Create a webhook endpoint

     Registers an endpoint for your application. The response is the only time the
    signing `secret` is returned; store it to verify signatures. Requires an
    owner, admin, or developer role in the application's organization.

    On the sandbox API this returns `403 manage_endpoints_on_live_api`: create test
    endpoints through the live API with `mode: "test"`, and they are mirrored into sandbox.

    Args:
        body (CreateWebhookEndpointBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | WebhookEndpointEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
