from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.get_syndicate_portfolio_status import GetSyndicatePortfolioStatus
from ...models.syndicate_portfolio_summary_envelope import SyndicatePortfolioSummaryEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    syndicate_id: str,
    *,
    status: GetSyndicatePortfolioStatus | Unset = UNSET,
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
        "url": "/syndicates/{syndicate_id}/portfolio".format(
            syndicate_id=quote(str(syndicate_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | SyndicatePortfolioSummaryEnvelope | None:
    if response.status_code == 200:
        response_200 = SyndicatePortfolioSummaryEnvelope.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | SyndicatePortfolioSummaryEnvelope]:
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
    status: GetSyndicatePortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Response[Error | SyndicatePortfolioSummaryEnvelope]:
    """Get syndicate portfolio summary

     Returns totals across the syndicate's portfolio: cost basis, current value,
    gains, per-status deal counts, and the number of distinct investors.
    Accepts the same `status` and `company` filters as the positions endpoint
    to total a slice of the portfolio, such as only exited deals.

    The summary covers the syndicate's funded deals, summed across everyone
    holding their securities (not just current members), as aggregate figures
    only. Member-level data is available on the members endpoints.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        syndicate_id (str):
        status (GetSyndicatePortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicatePortfolioSummaryEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        status=status,
        company=company,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    status: GetSyndicatePortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Error | SyndicatePortfolioSummaryEnvelope | None:
    """Get syndicate portfolio summary

     Returns totals across the syndicate's portfolio: cost basis, current value,
    gains, per-status deal counts, and the number of distinct investors.
    Accepts the same `status` and `company` filters as the positions endpoint
    to total a slice of the portfolio, such as only exited deals.

    The summary covers the syndicate's funded deals, summed across everyone
    holding their securities (not just current members), as aggregate figures
    only. Member-level data is available on the members endpoints.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        syndicate_id (str):
        status (GetSyndicatePortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicatePortfolioSummaryEnvelope
    """

    return sync_detailed(
        syndicate_id=syndicate_id,
        client=client,
        status=status,
        company=company,
    ).parsed


async def asyncio_detailed(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    status: GetSyndicatePortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Response[Error | SyndicatePortfolioSummaryEnvelope]:
    """Get syndicate portfolio summary

     Returns totals across the syndicate's portfolio: cost basis, current value,
    gains, per-status deal counts, and the number of distinct investors.
    Accepts the same `status` and `company` filters as the positions endpoint
    to total a slice of the portfolio, such as only exited deals.

    The summary covers the syndicate's funded deals, summed across everyone
    holding their securities (not just current members), as aggregate figures
    only. Member-level data is available on the members endpoints.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        syndicate_id (str):
        status (GetSyndicatePortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | SyndicatePortfolioSummaryEnvelope]
    """

    kwargs = _get_kwargs(
        syndicate_id=syndicate_id,
        status=status,
        company=company,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    syndicate_id: str,
    *,
    client: AuthenticatedClient,
    status: GetSyndicatePortfolioStatus | Unset = UNSET,
    company: str | Unset = UNSET,
) -> Error | SyndicatePortfolioSummaryEnvelope | None:
    """Get syndicate portfolio summary

     Returns totals across the syndicate's portfolio: cost basis, current value,
    gains, per-status deal counts, and the number of distinct investors.
    Accepts the same `status` and `company` filters as the positions endpoint
    to total a slice of the portfolio, such as only exited deals.

    The summary covers the syndicate's funded deals, summed across everyone
    holding their securities (not just current members), as aggregate figures
    only. Member-level data is available on the members endpoints.

    Portfolio values are recalculated periodically rather than on each request,
    so recent investments and valuation changes can take a few minutes to appear.
    `as_of` is the timestamp of the oldest calculation included in the response.

    Monetary values are **integer cents**; per-share prices and return multiples
    are **decimal strings**.

    Args:
        syndicate_id (str):
        status (GetSyndicatePortfolioStatus | Unset):
        company (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | SyndicatePortfolioSummaryEnvelope
    """

    return (
        await asyncio_detailed(
            syndicate_id=syndicate_id,
            client=client,
            status=status,
            company=company,
        )
    ).parsed
