from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_portfolio_status import GetPortfolioStatus
from ...models.portfolio_summary_envelope import PortfolioSummaryEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: GetPortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["company"] = company

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/portfolio",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | PortfolioSummaryEnvelope | None:
    if response.status_code == 200:
        response_200 = PortfolioSummaryEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | PortfolioSummaryEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: GetPortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Response[Error | PortfolioSummaryEnvelope]:
    """Get portfolio summary

     Returns totals across the authenticated investor's portfolio: cost basis,
    current value, realized and unrealized gains, and per-status position counts.
    Accepts the same `status` and `company` filters as `GET /portfolio/positions`
    to total a slice of the portfolio, such as only exited positions.

    Requires a user-authorized token. App-only (client credentials) tokens
    receive 403.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        status (GetPortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PortfolioSummaryEnvelope]
    """

    kwargs = _get_kwargs(
        status=status,
        company=company,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: GetPortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Error | PortfolioSummaryEnvelope | None:
    """Get portfolio summary

     Returns totals across the authenticated investor's portfolio: cost basis,
    current value, realized and unrealized gains, and per-status position counts.
    Accepts the same `status` and `company` filters as `GET /portfolio/positions`
    to total a slice of the portfolio, such as only exited positions.

    Requires a user-authorized token. App-only (client credentials) tokens
    receive 403.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        status (GetPortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PortfolioSummaryEnvelope
    """

    return sync_detailed(
        client=client,
        status=status,
        company=company,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: GetPortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Response[Error | PortfolioSummaryEnvelope]:
    """Get portfolio summary

     Returns totals across the authenticated investor's portfolio: cost basis,
    current value, realized and unrealized gains, and per-status position counts.
    Accepts the same `status` and `company` filters as `GET /portfolio/positions`
    to total a slice of the portfolio, such as only exited positions.

    Requires a user-authorized token. App-only (client credentials) tokens
    receive 403.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        status (GetPortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | PortfolioSummaryEnvelope]
    """

    kwargs = _get_kwargs(
        status=status,
        company=company,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: GetPortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Error | PortfolioSummaryEnvelope | None:
    """Get portfolio summary

     Returns totals across the authenticated investor's portfolio: cost basis,
    current value, realized and unrealized gains, and per-status position counts.
    Accepts the same `status` and `company` filters as `GET /portfolio/positions`
    to total a slice of the portfolio, such as only exited positions.

    Requires a user-authorized token. App-only (client credentials) tokens
    receive 403.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        status (GetPortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | PortfolioSummaryEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            company=company,
        )
    ).parsed
