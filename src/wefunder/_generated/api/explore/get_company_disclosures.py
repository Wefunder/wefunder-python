from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.company_disclosures_envelope import CompanyDisclosuresEnvelope
from ...models.error import Error
from ...models.get_company_disclosures_sections_item import GetCompanyDisclosuresSectionsItem
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    id: str,
    *,
    sections: list[GetCompanyDisclosuresSectionsItem] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_sections: list[str] | Unset = UNSET
    if not isinstance(sections, Unset):
        json_sections = []
        for sections_item_data in sections:
            sections_item = sections_item_data.value
            json_sections.append(sections_item)


    params["sections"] = json_sections


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/companies/{id}/disclosures".format(id=quote(str(id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CompanyDisclosuresEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanyDisclosuresEnvelope.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())



        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 429:
        response_429 = Error.from_dict(response.json())



        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CompanyDisclosuresEnvelope | Error]:
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
    sections: list[GetCompanyDisclosuresSectionsItem] | Unset = UNSET,

) -> Response[Any | CompanyDisclosuresEnvelope | Error]:
    """ Get a company's public Form C disclosures

     The Details tab of the company's Wefunder page as structured data — the company's own
    Form C disclosures, section for section: financial statements for the fiscal years on
    file, the page's ratios, the founder's current-position disclosure (cash on hand, monthly
    revenue / costs / burn), the financial-condition narrative, document links, risks, use of
    funds, directors and officers, 20%+ holders, capital structure, prior offerings, outstanding
    notes and debts, and related-party transactions.

    Same "who has a page" rule as `GET /companies/{id}`. The round read is the page's own: the
    display round for the viewer, swapped for its concurrent Reg CF sibling on a Reg D round,
    and only when it is a Reg CF / ECSP round with a Form C. A company with no such round has
    no details tab on the site and answers `404` with `error.type: no_disclosures` — distinct
    from an unknown or hidden company. A section the company hides on the site is `null`.

    Money is USD as decimal strings; ratios are percentages as decimal strings. Everything here
    is the issuer's own disclosure, served as filed, not a Wefunder assessment.

    Args:
        id (str):
        sections (list[GetCompanyDisclosuresSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyDisclosuresEnvelope | Error]
     """


    kwargs = _get_kwargs(
        id=id,
sections=sections,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    sections: list[GetCompanyDisclosuresSectionsItem] | Unset = UNSET,

) -> Any | CompanyDisclosuresEnvelope | Error | None:
    """ Get a company's public Form C disclosures

     The Details tab of the company's Wefunder page as structured data — the company's own
    Form C disclosures, section for section: financial statements for the fiscal years on
    file, the page's ratios, the founder's current-position disclosure (cash on hand, monthly
    revenue / costs / burn), the financial-condition narrative, document links, risks, use of
    funds, directors and officers, 20%+ holders, capital structure, prior offerings, outstanding
    notes and debts, and related-party transactions.

    Same "who has a page" rule as `GET /companies/{id}`. The round read is the page's own: the
    display round for the viewer, swapped for its concurrent Reg CF sibling on a Reg D round,
    and only when it is a Reg CF / ECSP round with a Form C. A company with no such round has
    no details tab on the site and answers `404` with `error.type: no_disclosures` — distinct
    from an unknown or hidden company. A section the company hides on the site is `null`.

    Money is USD as decimal strings; ratios are percentages as decimal strings. Everything here
    is the issuer's own disclosure, served as filed, not a Wefunder assessment.

    Args:
        id (str):
        sections (list[GetCompanyDisclosuresSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyDisclosuresEnvelope | Error
     """


    return sync_detailed(
        id=id,
client=client,
sections=sections,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    sections: list[GetCompanyDisclosuresSectionsItem] | Unset = UNSET,

) -> Response[Any | CompanyDisclosuresEnvelope | Error]:
    """ Get a company's public Form C disclosures

     The Details tab of the company's Wefunder page as structured data — the company's own
    Form C disclosures, section for section: financial statements for the fiscal years on
    file, the page's ratios, the founder's current-position disclosure (cash on hand, monthly
    revenue / costs / burn), the financial-condition narrative, document links, risks, use of
    funds, directors and officers, 20%+ holders, capital structure, prior offerings, outstanding
    notes and debts, and related-party transactions.

    Same "who has a page" rule as `GET /companies/{id}`. The round read is the page's own: the
    display round for the viewer, swapped for its concurrent Reg CF sibling on a Reg D round,
    and only when it is a Reg CF / ECSP round with a Form C. A company with no such round has
    no details tab on the site and answers `404` with `error.type: no_disclosures` — distinct
    from an unknown or hidden company. A section the company hides on the site is `null`.

    Money is USD as decimal strings; ratios are percentages as decimal strings. Everything here
    is the issuer's own disclosure, served as filed, not a Wefunder assessment.

    Args:
        id (str):
        sections (list[GetCompanyDisclosuresSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyDisclosuresEnvelope | Error]
     """


    kwargs = _get_kwargs(
        id=id,
sections=sections,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    sections: list[GetCompanyDisclosuresSectionsItem] | Unset = UNSET,

) -> Any | CompanyDisclosuresEnvelope | Error | None:
    """ Get a company's public Form C disclosures

     The Details tab of the company's Wefunder page as structured data — the company's own
    Form C disclosures, section for section: financial statements for the fiscal years on
    file, the page's ratios, the founder's current-position disclosure (cash on hand, monthly
    revenue / costs / burn), the financial-condition narrative, document links, risks, use of
    funds, directors and officers, 20%+ holders, capital structure, prior offerings, outstanding
    notes and debts, and related-party transactions.

    Same "who has a page" rule as `GET /companies/{id}`. The round read is the page's own: the
    display round for the viewer, swapped for its concurrent Reg CF sibling on a Reg D round,
    and only when it is a Reg CF / ECSP round with a Form C. A company with no such round has
    no details tab on the site and answers `404` with `error.type: no_disclosures` — distinct
    from an unknown or hidden company. A section the company hides on the site is `null`.

    Money is USD as decimal strings; ratios are percentages as decimal strings. Everything here
    is the issuer's own disclosure, served as filed, not a Wefunder assessment.

    Args:
        id (str):
        sections (list[GetCompanyDisclosuresSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyDisclosuresEnvelope | Error
     """


    return (await asyncio_detailed(
        id=id,
client=client,
sections=sections,

    )).parsed
