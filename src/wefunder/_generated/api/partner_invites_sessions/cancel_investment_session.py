from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.investment_session_envelope import InvestmentSessionEnvelope
from ...models.validation_error import ValidationError
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/investment_sessions/{id}".format(
            id=quote(str(id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InvestmentSessionEnvelope | ValidationError | None:
    if response.status_code == 200:
        response_200 = InvestmentSessionEnvelope.from_dict(response.json())

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
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InvestmentSessionEnvelope | ValidationError]:
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
) -> Response[Error | InvestmentSessionEnvelope | ValidationError]:
    """Cancel an investment session

     Alias of `/partner/investment_sessions` (#23636).

    Cancels a session so its link stops working. Valid while the session is
    `pending`, `in_progress`, or `abandoned`; repeating the call on an
    already-canceled session returns the same 200. A `completed` or `expired`
    session cannot be canceled (422 `session_not_cancelable`).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvestmentSessionEnvelope | ValidationError]
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
) -> Error | InvestmentSessionEnvelope | ValidationError | None:
    """Cancel an investment session

     Alias of `/partner/investment_sessions` (#23636).

    Cancels a session so its link stops working. Valid while the session is
    `pending`, `in_progress`, or `abandoned`; repeating the call on an
    already-canceled session returns the same 200. A `completed` or `expired`
    session cannot be canceled (422 `session_not_cancelable`).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvestmentSessionEnvelope | ValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Error | InvestmentSessionEnvelope | ValidationError]:
    """Cancel an investment session

     Alias of `/partner/investment_sessions` (#23636).

    Cancels a session so its link stops working. Valid while the session is
    `pending`, `in_progress`, or `abandoned`; repeating the call on an
    already-canceled session returns the same 200. A `completed` or `expired`
    session cannot be canceled (422 `session_not_cancelable`).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvestmentSessionEnvelope | ValidationError]
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
) -> Error | InvestmentSessionEnvelope | ValidationError | None:
    """Cancel an investment session

     Alias of `/partner/investment_sessions` (#23636).

    Cancels a session so its link stops working. Valid while the session is
    `pending`, `in_progress`, or `abandoned`; repeating the call on an
    already-canceled session returns the same 200. A `completed` or `expired`
    session cannot be canceled (422 `session_not_cancelable`).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvestmentSessionEnvelope | ValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
