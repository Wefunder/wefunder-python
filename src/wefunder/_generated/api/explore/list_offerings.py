import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error import Error
from ...models.list_offerings_business_model_item import ListOfferingsBusinessModelItem
from ...models.list_offerings_exemption import ListOfferingsExemption
from ...models.list_offerings_industry_item import ListOfferingsIndustryItem
from ...models.list_offerings_security import ListOfferingsSecurity
from ...models.list_offerings_sort import ListOfferingsSort
from ...models.list_offerings_status import ListOfferingsStatus
from ...models.offering_list_envelope import OfferingListEnvelope
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListOfferingsStatus | Unset = ListOfferingsStatus.LIVE,
    sort: ListOfferingsSort | Unset = ListOfferingsSort.MOST_RAISED,
    exemption: ListOfferingsExemption | Unset = UNSET,
    security: ListOfferingsSecurity | Unset = UNSET,
    testing_the_waters: bool | Unset = UNSET,
    max_min_investment: float | Unset = UNSET,
    closing_before: datetime.date | Unset = UNSET,
    min_amount_raised: float | Unset = UNSET,
    industry: list[ListOfferingsIndustryItem] | Unset = UNSET,
    business_model: list[ListOfferingsBusinessModelItem] | Unset = UNSET,
    followed: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    params["per_page"] = per_page

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    json_exemption: str | Unset = UNSET
    if not isinstance(exemption, Unset):
        json_exemption = exemption.value

    params["exemption"] = json_exemption

    json_security: str | Unset = UNSET
    if not isinstance(security, Unset):
        json_security = security.value

    params["security"] = json_security

    params["testing_the_waters"] = testing_the_waters

    params["max_min_investment"] = max_min_investment

    json_closing_before: str | Unset = UNSET
    if not isinstance(closing_before, Unset):
        json_closing_before = closing_before.isoformat()
    params["closing_before"] = json_closing_before

    params["min_amount_raised"] = min_amount_raised

    json_industry: list[str] | Unset = UNSET
    if not isinstance(industry, Unset):
        json_industry = []
        for industry_item_data in industry:
            industry_item = industry_item_data.value
            json_industry.append(industry_item)

    params["industry"] = json_industry

    json_business_model: list[str] | Unset = UNSET
    if not isinstance(business_model, Unset):
        json_business_model = []
        for business_model_item_data in business_model:
            business_model_item = business_model_item_data.value
            json_business_model.append(business_model_item)

    params["business_model"] = json_business_model

    params["followed"] = followed

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/explore",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | OfferingListEnvelope | None:
    if response.status_code == 200:
        response_200 = OfferingListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | OfferingListEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListOfferingsStatus | Unset = ListOfferingsStatus.LIVE,
    sort: ListOfferingsSort | Unset = ListOfferingsSort.MOST_RAISED,
    exemption: ListOfferingsExemption | Unset = UNSET,
    security: ListOfferingsSecurity | Unset = UNSET,
    testing_the_waters: bool | Unset = UNSET,
    max_min_investment: float | Unset = UNSET,
    closing_before: datetime.date | Unset = UNSET,
    min_amount_raised: float | Unset = UNSET,
    industry: list[ListOfferingsIndustryItem] | Unset = UNSET,
    business_model: list[ListOfferingsBusinessModelItem] | Unset = UNSET,
    followed: bool | Unset = UNSET,
) -> Response[Error | OfferingListEnvelope]:
    """List public offerings

     Returns the offerings shown on wefunder.com/explore — the curated set of companies that
    meet Wefunder's discoverability bar (a soft-confirmed traction threshold plus approval),
    **one offering per company**. An "offering" is a fundraise, addressed by its id
    (`ofr_...`).

    **Public view (`read:public`).** Reachable with either a server-side (client_credentials)
    token or a user access token. Private rounds (e.g. Reg D 506(b)) are never listed, and
    low-traction or unapproved companies are excluded — exactly as they are on the website
    for a logged-out visitor.

    **Logged-in view (`read:explore`).** A user access token carrying `read:explore` gets
    what *that user* sees on wefunder.com/explore: the public offerings plus any the user
    qualifies for (accredited-only / Vault deals, invited private rounds), each checked
    against the same visibility policy the website applies. The response is a strict
    superset of the public one — same fields and ids — with two extra attributes,
    `publicly_visible` and `invested`, and `meta.personalized: true`. A server-side key can
    never hold `read:explore`; a token with `read:explore` but no resolvable user gets the
    public view.

    Order with `sort` (default: most raised); paginate with `cursor` and `per_page`.
    `meta.total_count` is the number of offerings across all pages, after filters.

    **Closed rounds (`status`).** By default the list is live rounds. `status=closed` lists
    rounds that finished raising instead, newest `closed_at` first. It is not limited to one
    per company or to the curated explore set: it covers every finished round that
    `GET /offerings/{id}` serves to a logged-out visitor, for companies listed in Wefunder's
    public directory. `status=all` returns the live list first, then the closed list. With
    `status=closed` or `status=all`, `exemption` is the only filter accepted, and `sort`
    orders only the live part. Closed rounds follow the public view even for a
    `read:explore` token.

    **Filters** are objective, per-offering terms — exemption family, security type,
    TTW vs. live, minimum investment ceiling, close date, amount raised floor. The response
    echoes the applied set in `meta.filters`. An out-of-vocabulary value is a `400` naming
    the accepted values. There are deliberately no relevance, quality, or ranking criteria.

    Use this endpoint to:
    - Discover and monitor active deals
    - Build deal aggregators and public listings
    - Bulk-list closed rounds (`status=closed`)

    Args:
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListOfferingsStatus | Unset):  Default: ListOfferingsStatus.LIVE.
        sort (ListOfferingsSort | Unset):  Default: ListOfferingsSort.MOST_RAISED.
        exemption (ListOfferingsExemption | Unset):
        security (ListOfferingsSecurity | Unset):
        testing_the_waters (bool | Unset):
        max_min_investment (float | Unset):
        closing_before (datetime.date | Unset):
        min_amount_raised (float | Unset):
        industry (list[ListOfferingsIndustryItem] | Unset):
        business_model (list[ListOfferingsBusinessModelItem] | Unset):
        followed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OfferingListEnvelope]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        per_page=per_page,
        status=status,
        sort=sort,
        exemption=exemption,
        security=security,
        testing_the_waters=testing_the_waters,
        max_min_investment=max_min_investment,
        closing_before=closing_before,
        min_amount_raised=min_amount_raised,
        industry=industry,
        business_model=business_model,
        followed=followed,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListOfferingsStatus | Unset = ListOfferingsStatus.LIVE,
    sort: ListOfferingsSort | Unset = ListOfferingsSort.MOST_RAISED,
    exemption: ListOfferingsExemption | Unset = UNSET,
    security: ListOfferingsSecurity | Unset = UNSET,
    testing_the_waters: bool | Unset = UNSET,
    max_min_investment: float | Unset = UNSET,
    closing_before: datetime.date | Unset = UNSET,
    min_amount_raised: float | Unset = UNSET,
    industry: list[ListOfferingsIndustryItem] | Unset = UNSET,
    business_model: list[ListOfferingsBusinessModelItem] | Unset = UNSET,
    followed: bool | Unset = UNSET,
) -> Error | OfferingListEnvelope | None:
    """List public offerings

     Returns the offerings shown on wefunder.com/explore — the curated set of companies that
    meet Wefunder's discoverability bar (a soft-confirmed traction threshold plus approval),
    **one offering per company**. An "offering" is a fundraise, addressed by its id
    (`ofr_...`).

    **Public view (`read:public`).** Reachable with either a server-side (client_credentials)
    token or a user access token. Private rounds (e.g. Reg D 506(b)) are never listed, and
    low-traction or unapproved companies are excluded — exactly as they are on the website
    for a logged-out visitor.

    **Logged-in view (`read:explore`).** A user access token carrying `read:explore` gets
    what *that user* sees on wefunder.com/explore: the public offerings plus any the user
    qualifies for (accredited-only / Vault deals, invited private rounds), each checked
    against the same visibility policy the website applies. The response is a strict
    superset of the public one — same fields and ids — with two extra attributes,
    `publicly_visible` and `invested`, and `meta.personalized: true`. A server-side key can
    never hold `read:explore`; a token with `read:explore` but no resolvable user gets the
    public view.

    Order with `sort` (default: most raised); paginate with `cursor` and `per_page`.
    `meta.total_count` is the number of offerings across all pages, after filters.

    **Closed rounds (`status`).** By default the list is live rounds. `status=closed` lists
    rounds that finished raising instead, newest `closed_at` first. It is not limited to one
    per company or to the curated explore set: it covers every finished round that
    `GET /offerings/{id}` serves to a logged-out visitor, for companies listed in Wefunder's
    public directory. `status=all` returns the live list first, then the closed list. With
    `status=closed` or `status=all`, `exemption` is the only filter accepted, and `sort`
    orders only the live part. Closed rounds follow the public view even for a
    `read:explore` token.

    **Filters** are objective, per-offering terms — exemption family, security type,
    TTW vs. live, minimum investment ceiling, close date, amount raised floor. The response
    echoes the applied set in `meta.filters`. An out-of-vocabulary value is a `400` naming
    the accepted values. There are deliberately no relevance, quality, or ranking criteria.

    Use this endpoint to:
    - Discover and monitor active deals
    - Build deal aggregators and public listings
    - Bulk-list closed rounds (`status=closed`)

    Args:
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListOfferingsStatus | Unset):  Default: ListOfferingsStatus.LIVE.
        sort (ListOfferingsSort | Unset):  Default: ListOfferingsSort.MOST_RAISED.
        exemption (ListOfferingsExemption | Unset):
        security (ListOfferingsSecurity | Unset):
        testing_the_waters (bool | Unset):
        max_min_investment (float | Unset):
        closing_before (datetime.date | Unset):
        min_amount_raised (float | Unset):
        industry (list[ListOfferingsIndustryItem] | Unset):
        business_model (list[ListOfferingsBusinessModelItem] | Unset):
        followed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OfferingListEnvelope
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        per_page=per_page,
        status=status,
        sort=sort,
        exemption=exemption,
        security=security,
        testing_the_waters=testing_the_waters,
        max_min_investment=max_min_investment,
        closing_before=closing_before,
        min_amount_raised=min_amount_raised,
        industry=industry,
        business_model=business_model,
        followed=followed,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListOfferingsStatus | Unset = ListOfferingsStatus.LIVE,
    sort: ListOfferingsSort | Unset = ListOfferingsSort.MOST_RAISED,
    exemption: ListOfferingsExemption | Unset = UNSET,
    security: ListOfferingsSecurity | Unset = UNSET,
    testing_the_waters: bool | Unset = UNSET,
    max_min_investment: float | Unset = UNSET,
    closing_before: datetime.date | Unset = UNSET,
    min_amount_raised: float | Unset = UNSET,
    industry: list[ListOfferingsIndustryItem] | Unset = UNSET,
    business_model: list[ListOfferingsBusinessModelItem] | Unset = UNSET,
    followed: bool | Unset = UNSET,
) -> Response[Error | OfferingListEnvelope]:
    """List public offerings

     Returns the offerings shown on wefunder.com/explore — the curated set of companies that
    meet Wefunder's discoverability bar (a soft-confirmed traction threshold plus approval),
    **one offering per company**. An "offering" is a fundraise, addressed by its id
    (`ofr_...`).

    **Public view (`read:public`).** Reachable with either a server-side (client_credentials)
    token or a user access token. Private rounds (e.g. Reg D 506(b)) are never listed, and
    low-traction or unapproved companies are excluded — exactly as they are on the website
    for a logged-out visitor.

    **Logged-in view (`read:explore`).** A user access token carrying `read:explore` gets
    what *that user* sees on wefunder.com/explore: the public offerings plus any the user
    qualifies for (accredited-only / Vault deals, invited private rounds), each checked
    against the same visibility policy the website applies. The response is a strict
    superset of the public one — same fields and ids — with two extra attributes,
    `publicly_visible` and `invested`, and `meta.personalized: true`. A server-side key can
    never hold `read:explore`; a token with `read:explore` but no resolvable user gets the
    public view.

    Order with `sort` (default: most raised); paginate with `cursor` and `per_page`.
    `meta.total_count` is the number of offerings across all pages, after filters.

    **Closed rounds (`status`).** By default the list is live rounds. `status=closed` lists
    rounds that finished raising instead, newest `closed_at` first. It is not limited to one
    per company or to the curated explore set: it covers every finished round that
    `GET /offerings/{id}` serves to a logged-out visitor, for companies listed in Wefunder's
    public directory. `status=all` returns the live list first, then the closed list. With
    `status=closed` or `status=all`, `exemption` is the only filter accepted, and `sort`
    orders only the live part. Closed rounds follow the public view even for a
    `read:explore` token.

    **Filters** are objective, per-offering terms — exemption family, security type,
    TTW vs. live, minimum investment ceiling, close date, amount raised floor. The response
    echoes the applied set in `meta.filters`. An out-of-vocabulary value is a `400` naming
    the accepted values. There are deliberately no relevance, quality, or ranking criteria.

    Use this endpoint to:
    - Discover and monitor active deals
    - Build deal aggregators and public listings
    - Bulk-list closed rounds (`status=closed`)

    Args:
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListOfferingsStatus | Unset):  Default: ListOfferingsStatus.LIVE.
        sort (ListOfferingsSort | Unset):  Default: ListOfferingsSort.MOST_RAISED.
        exemption (ListOfferingsExemption | Unset):
        security (ListOfferingsSecurity | Unset):
        testing_the_waters (bool | Unset):
        max_min_investment (float | Unset):
        closing_before (datetime.date | Unset):
        min_amount_raised (float | Unset):
        industry (list[ListOfferingsIndustryItem] | Unset):
        business_model (list[ListOfferingsBusinessModelItem] | Unset):
        followed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | OfferingListEnvelope]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        per_page=per_page,
        status=status,
        sort=sort,
        exemption=exemption,
        security=security,
        testing_the_waters=testing_the_waters,
        max_min_investment=max_min_investment,
        closing_before=closing_before,
        min_amount_raised=min_amount_raised,
        industry=industry,
        business_model=business_model,
        followed=followed,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    per_page: int | Unset = 25,
    status: ListOfferingsStatus | Unset = ListOfferingsStatus.LIVE,
    sort: ListOfferingsSort | Unset = ListOfferingsSort.MOST_RAISED,
    exemption: ListOfferingsExemption | Unset = UNSET,
    security: ListOfferingsSecurity | Unset = UNSET,
    testing_the_waters: bool | Unset = UNSET,
    max_min_investment: float | Unset = UNSET,
    closing_before: datetime.date | Unset = UNSET,
    min_amount_raised: float | Unset = UNSET,
    industry: list[ListOfferingsIndustryItem] | Unset = UNSET,
    business_model: list[ListOfferingsBusinessModelItem] | Unset = UNSET,
    followed: bool | Unset = UNSET,
) -> Error | OfferingListEnvelope | None:
    """List public offerings

     Returns the offerings shown on wefunder.com/explore — the curated set of companies that
    meet Wefunder's discoverability bar (a soft-confirmed traction threshold plus approval),
    **one offering per company**. An "offering" is a fundraise, addressed by its id
    (`ofr_...`).

    **Public view (`read:public`).** Reachable with either a server-side (client_credentials)
    token or a user access token. Private rounds (e.g. Reg D 506(b)) are never listed, and
    low-traction or unapproved companies are excluded — exactly as they are on the website
    for a logged-out visitor.

    **Logged-in view (`read:explore`).** A user access token carrying `read:explore` gets
    what *that user* sees on wefunder.com/explore: the public offerings plus any the user
    qualifies for (accredited-only / Vault deals, invited private rounds), each checked
    against the same visibility policy the website applies. The response is a strict
    superset of the public one — same fields and ids — with two extra attributes,
    `publicly_visible` and `invested`, and `meta.personalized: true`. A server-side key can
    never hold `read:explore`; a token with `read:explore` but no resolvable user gets the
    public view.

    Order with `sort` (default: most raised); paginate with `cursor` and `per_page`.
    `meta.total_count` is the number of offerings across all pages, after filters.

    **Closed rounds (`status`).** By default the list is live rounds. `status=closed` lists
    rounds that finished raising instead, newest `closed_at` first. It is not limited to one
    per company or to the curated explore set: it covers every finished round that
    `GET /offerings/{id}` serves to a logged-out visitor, for companies listed in Wefunder's
    public directory. `status=all` returns the live list first, then the closed list. With
    `status=closed` or `status=all`, `exemption` is the only filter accepted, and `sort`
    orders only the live part. Closed rounds follow the public view even for a
    `read:explore` token.

    **Filters** are objective, per-offering terms — exemption family, security type,
    TTW vs. live, minimum investment ceiling, close date, amount raised floor. The response
    echoes the applied set in `meta.filters`. An out-of-vocabulary value is a `400` naming
    the accepted values. There are deliberately no relevance, quality, or ranking criteria.

    Use this endpoint to:
    - Discover and monitor active deals
    - Build deal aggregators and public listings
    - Bulk-list closed rounds (`status=closed`)

    Args:
        cursor (int | Unset):
        per_page (int | Unset):  Default: 25.
        status (ListOfferingsStatus | Unset):  Default: ListOfferingsStatus.LIVE.
        sort (ListOfferingsSort | Unset):  Default: ListOfferingsSort.MOST_RAISED.
        exemption (ListOfferingsExemption | Unset):
        security (ListOfferingsSecurity | Unset):
        testing_the_waters (bool | Unset):
        max_min_investment (float | Unset):
        closing_before (datetime.date | Unset):
        min_amount_raised (float | Unset):
        industry (list[ListOfferingsIndustryItem] | Unset):
        business_model (list[ListOfferingsBusinessModelItem] | Unset):
        followed (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | OfferingListEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            per_page=per_page,
            status=status,
            sort=sort,
            exemption=exemption,
            security=security,
            testing_the_waters=testing_the_waters,
            max_min_investment=max_min_investment,
            closing_before=closing_before,
            min_amount_raised=min_amount_raised,
            industry=industry,
            business_model=business_model,
            followed=followed,
        )
    ).parsed
