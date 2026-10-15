from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.investment_session_list_envelope import InvestmentSessionListEnvelope
from ...models.list_offering_investment_sessions_status import ListOfferingInvestmentSessionsStatus
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    status: ListOfferingInvestmentSessionsStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["per_page"] = per_page

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/offerings/{id}/investment_sessions".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InvestmentSessionListEnvelope | ValidationError | None:
    if response.status_code == 200:
        response_200 = InvestmentSessionListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = ValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | InvestmentSessionListEnvelope | ValidationError]:
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
    status: ListOfferingInvestmentSessionsStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
) -> Response[Error | InvestmentSessionListEnvelope | ValidationError]:
    """List investment sessions

     Lists the investment sessions your app created on this offering, newest first;
    filter by `status`. A session belongs to the application that created it: no other
    app sees it, even one of your organization. A syndicate- or company-owned token sees
    only its own syndicate's or company's sessions. An offering with none of your app's
    sessions lists nothing, so the id reveals nothing about the offering.

    Args:
        id (str):
        status (ListOfferingInvestmentSessionsStatus | Unset):
        per_page (int | Unset):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvestmentSessionListEnvelope | ValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        per_page=per_page,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    status: ListOfferingInvestmentSessionsStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
) -> Error | InvestmentSessionListEnvelope | ValidationError | None:
    """List investment sessions

     Lists the investment sessions your app created on this offering, newest first;
    filter by `status`. A session belongs to the application that created it: no other
    app sees it, even one of your organization. A syndicate- or company-owned token sees
    only its own syndicate's or company's sessions. An offering with none of your app's
    sessions lists nothing, so the id reveals nothing about the offering.

    Args:
        id (str):
        status (ListOfferingInvestmentSessionsStatus | Unset):
        per_page (int | Unset):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvestmentSessionListEnvelope | ValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
        status=status,
        per_page=per_page,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    status: ListOfferingInvestmentSessionsStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
) -> Response[Error | InvestmentSessionListEnvelope | ValidationError]:
    """List investment sessions

     Lists the investment sessions your app created on this offering, newest first;
    filter by `status`. A session belongs to the application that created it: no other
    app sees it, even one of your organization. A syndicate- or company-owned token sees
    only its own syndicate's or company's sessions. An offering with none of your app's
    sessions lists nothing, so the id reveals nothing about the offering.

    Args:
        id (str):
        status (ListOfferingInvestmentSessionsStatus | Unset):
        per_page (int | Unset):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvestmentSessionListEnvelope | ValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        status=status,
        per_page=per_page,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    status: ListOfferingInvestmentSessionsStatus | Unset = UNSET,
    per_page: int | Unset = UNSET,
    cursor: int | Unset = UNSET,
) -> Error | InvestmentSessionListEnvelope | ValidationError | None:
    """List investment sessions

     Lists the investment sessions your app created on this offering, newest first;
    filter by `status`. A session belongs to the application that created it: no other
    app sees it, even one of your organization. A syndicate- or company-owned token sees
    only its own syndicate's or company's sessions. An offering with none of your app's
    sessions lists nothing, so the id reveals nothing about the offering.

    Args:
        id (str):
        status (ListOfferingInvestmentSessionsStatus | Unset):
        per_page (int | Unset):
        cursor (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvestmentSessionListEnvelope | ValidationError
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            status=status,
            per_page=per_page,
            cursor=cursor,
        )
    ).parsed
