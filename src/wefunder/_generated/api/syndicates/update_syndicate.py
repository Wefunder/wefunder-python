from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.syndicate_detail_envelope import SyndicateDetailEnvelope
from ...models.update_syndicate_body import UpdateSyndicateBody
from ...types import Response


def _get_kwargs(
    syndicate_id: str,
    *,
    body: UpdateSyndicateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/syndicates/{syndicate_id}".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SyndicateDetailEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicateDetailEnvelope.from_dict(response.json())

        return response_200

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
) -> Response[Error | SyndicateDetailEnvelope]:
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
    body: UpdateSyndicateBody,
) -> Response[Error | SyndicateDetailEnvelope]:
    """Update syndicate settings

     Update syndicate configuration. Currently supports name, description, and tagline.
    Requires `write:syndicates` scope and at least operator permission.

    Args:
        syndicate_id (str):
        body (UpdateSyndicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDetailEnvelope]
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
    body: UpdateSyndicateBody,
) -> Error | SyndicateDetailEnvelope | None:
    """Update syndicate settings

     Update syndicate configuration. Currently supports name, description, and tagline.
    Requires `write:syndicates` scope and at least operator permission.

    Args:
        syndicate_id (str):
        body (UpdateSyndicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDetailEnvelope
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
    body: UpdateSyndicateBody,
) -> Response[Error | SyndicateDetailEnvelope]:
    """Update syndicate settings

     Update syndicate configuration. Currently supports name, description, and tagline.
    Requires `write:syndicates` scope and at least operator permission.

    Args:
        syndicate_id (str):
        body (UpdateSyndicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicateDetailEnvelope]
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
    body: UpdateSyndicateBody,
) -> Error | SyndicateDetailEnvelope | None:
    """Update syndicate settings

     Update syndicate configuration. Currently supports name, description, and tagline.
    Requires `write:syndicates` scope and at least operator permission.

    Args:
        syndicate_id (str):
        body (UpdateSyndicateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicateDetailEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            body=body,
        )
    ).parsed
