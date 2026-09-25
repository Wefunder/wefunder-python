from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_installation_body import CreateInstallationBody
from ...models.error import Error
from ...models.installation_token_envelope import InstallationTokenEnvelope
from typing import cast



def _get_kwargs(
    *,
    body: CreateInstallationBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/installations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | Error | InstallationTokenEnvelope | None:
    if response.status_code == 201:
        response_201 = InstallationTokenEnvelope.from_dict(response.json())



        return response_201

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())



        return response_403

    if response.status_code == 404:
        response_404 = Error.from_dict(response.json())



        return response_404

    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409

    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | Error | InstallationTokenEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInstallationBody,

) -> Response[Any | Error | InstallationTokenEnvelope]:
    """ Install your app on a company or syndicate

     Installs the calling application on a company or syndicate the token's user can edit (or, for a
    syndicate, manages), and mints the **company-owned token** the install stands for. The token
    appears in this response only. Requires a token authorized by a user.

    The install is granted at the caller's tier (founder, admin or editor for a company). An
    editor-tier install carries read scopes only; write scopes in `scopes` are dropped. Installing
    on a company outside your own organization requires the app to be approved.

    Args:
        body (CreateInstallationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | InstallationTokenEnvelope]
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
    body: CreateInstallationBody,

) -> Any | Error | InstallationTokenEnvelope | None:
    """ Install your app on a company or syndicate

     Installs the calling application on a company or syndicate the token's user can edit (or, for a
    syndicate, manages), and mints the **company-owned token** the install stands for. The token
    appears in this response only. Requires a token authorized by a user.

    The install is granted at the caller's tier (founder, admin or editor for a company). An
    editor-tier install carries read scopes only; write scopes in `scopes` are dropped. Installing
    on a company outside your own organization requires the app to be approved.

    Args:
        body (CreateInstallationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | InstallationTokenEnvelope
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateInstallationBody,

) -> Response[Any | Error | InstallationTokenEnvelope]:
    """ Install your app on a company or syndicate

     Installs the calling application on a company or syndicate the token's user can edit (or, for a
    syndicate, manages), and mints the **company-owned token** the install stands for. The token
    appears in this response only. Requires a token authorized by a user.

    The install is granted at the caller's tier (founder, admin or editor for a company). An
    editor-tier install carries read scopes only; write scopes in `scopes` are dropped. Installing
    on a company outside your own organization requires the app to be approved.

    Args:
        body (CreateInstallationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | Error | InstallationTokenEnvelope]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateInstallationBody,

) -> Any | Error | InstallationTokenEnvelope | None:
    """ Install your app on a company or syndicate

     Installs the calling application on a company or syndicate the token's user can edit (or, for a
    syndicate, manages), and mints the **company-owned token** the install stands for. The token
    appears in this response only. Requires a token authorized by a user.

    The install is granted at the caller's tier (founder, admin or editor for a company). An
    editor-tier install carries read scopes only; write scopes in `scopes` are dropped. Installing
    on a company outside your own organization requires the app to be approved.

    Args:
        body (CreateInstallationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | Error | InstallationTokenEnvelope
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
