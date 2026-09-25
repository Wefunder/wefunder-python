from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.company_pitch_envelope import CompanyPitchEnvelope
from ...models.error import Error
from ...models.get_company_pitch_sections_item import GetCompanyPitchSectionsItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    sections: list[GetCompanyPitchSectionsItem] | Unset = UNSET,
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
        "url": "/companies/{id}/pitch".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CompanyPitchEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = CompanyPitchEnvelope.from_dict(response.json())

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


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CompanyPitchEnvelope | Error]:
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
    sections: list[GetCompanyPitchSectionsItem] | Unset = UNSET,
) -> Response[Any | CompanyPitchEnvelope | Error]:
    """Get a company's pitch

     The Overview tab's pitch as structured data: the story as ordered blocks (`heading`,
    `paragraph`, `list`, `image`, `video`, `footnote`), plus the perk tiers of the round the page
    shows the viewer. Images and embedded videos keep their place in the document with an absolute
    URL, because founders publish perk tiers, stretch goals, timelines, and charts as pictures
    (typically with no alt text) and a plain-text rendering would drop them.

    What is parsed is what the page renders: the story passes through the site's own sanitizer
    first, so an embed the page refuses (a host off its allowlist, a `javascript:` URL) is never
    served here either. Same "who has a page" rule and round chooser as `GET /companies/{id}`.
    A site-public company with no round the viewer may see still has a pitch (`perks: null`).
    `perks.described_in_pitch` is a heuristic: true when the structured perk list is a placeholder
    ("See investor overview page", or one identical sentence on every tier) and the real tiers are
    in the story's images.

    `authored_by` says who wrote the story: `company` (the issuer's own words and imagery, not a
    Wefunder assessment) or `wefunder` (a Wefunder-prepared deal memo the company did not
    participate in; `disclaimer` carries the page's notice). A pitch can run to ~70 KB; use
    `sections` to ask for less.

    Args:
        id (str):
        sections (list[GetCompanyPitchSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyPitchEnvelope | Error]
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
    sections: list[GetCompanyPitchSectionsItem] | Unset = UNSET,
) -> Any | CompanyPitchEnvelope | Error | None:
    """Get a company's pitch

     The Overview tab's pitch as structured data: the story as ordered blocks (`heading`,
    `paragraph`, `list`, `image`, `video`, `footnote`), plus the perk tiers of the round the page
    shows the viewer. Images and embedded videos keep their place in the document with an absolute
    URL, because founders publish perk tiers, stretch goals, timelines, and charts as pictures
    (typically with no alt text) and a plain-text rendering would drop them.

    What is parsed is what the page renders: the story passes through the site's own sanitizer
    first, so an embed the page refuses (a host off its allowlist, a `javascript:` URL) is never
    served here either. Same "who has a page" rule and round chooser as `GET /companies/{id}`.
    A site-public company with no round the viewer may see still has a pitch (`perks: null`).
    `perks.described_in_pitch` is a heuristic: true when the structured perk list is a placeholder
    ("See investor overview page", or one identical sentence on every tier) and the real tiers are
    in the story's images.

    `authored_by` says who wrote the story: `company` (the issuer's own words and imagery, not a
    Wefunder assessment) or `wefunder` (a Wefunder-prepared deal memo the company did not
    participate in; `disclaimer` carries the page's notice). A pitch can run to ~70 KB; use
    `sections` to ask for less.

    Args:
        id (str):
        sections (list[GetCompanyPitchSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyPitchEnvelope | Error
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
    sections: list[GetCompanyPitchSectionsItem] | Unset = UNSET,
) -> Response[Any | CompanyPitchEnvelope | Error]:
    """Get a company's pitch

     The Overview tab's pitch as structured data: the story as ordered blocks (`heading`,
    `paragraph`, `list`, `image`, `video`, `footnote`), plus the perk tiers of the round the page
    shows the viewer. Images and embedded videos keep their place in the document with an absolute
    URL, because founders publish perk tiers, stretch goals, timelines, and charts as pictures
    (typically with no alt text) and a plain-text rendering would drop them.

    What is parsed is what the page renders: the story passes through the site's own sanitizer
    first, so an embed the page refuses (a host off its allowlist, a `javascript:` URL) is never
    served here either. Same "who has a page" rule and round chooser as `GET /companies/{id}`.
    A site-public company with no round the viewer may see still has a pitch (`perks: null`).
    `perks.described_in_pitch` is a heuristic: true when the structured perk list is a placeholder
    ("See investor overview page", or one identical sentence on every tier) and the real tiers are
    in the story's images.

    `authored_by` says who wrote the story: `company` (the issuer's own words and imagery, not a
    Wefunder assessment) or `wefunder` (a Wefunder-prepared deal memo the company did not
    participate in; `disclaimer` carries the page's notice). A pitch can run to ~70 KB; use
    `sections` to ask for less.

    Args:
        id (str):
        sections (list[GetCompanyPitchSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CompanyPitchEnvelope | Error]
    """

    kwargs = _get_kwargs(
        id=id,
        sections=sections,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    sections: list[GetCompanyPitchSectionsItem] | Unset = UNSET,
) -> Any | CompanyPitchEnvelope | Error | None:
    """Get a company's pitch

     The Overview tab's pitch as structured data: the story as ordered blocks (`heading`,
    `paragraph`, `list`, `image`, `video`, `footnote`), plus the perk tiers of the round the page
    shows the viewer. Images and embedded videos keep their place in the document with an absolute
    URL, because founders publish perk tiers, stretch goals, timelines, and charts as pictures
    (typically with no alt text) and a plain-text rendering would drop them.

    What is parsed is what the page renders: the story passes through the site's own sanitizer
    first, so an embed the page refuses (a host off its allowlist, a `javascript:` URL) is never
    served here either. Same "who has a page" rule and round chooser as `GET /companies/{id}`.
    A site-public company with no round the viewer may see still has a pitch (`perks: null`).
    `perks.described_in_pitch` is a heuristic: true when the structured perk list is a placeholder
    ("See investor overview page", or one identical sentence on every tier) and the real tiers are
    in the story's images.

    `authored_by` says who wrote the story: `company` (the issuer's own words and imagery, not a
    Wefunder assessment) or `wefunder` (a Wefunder-prepared deal memo the company did not
    participate in; `disclaimer` carries the page's notice). A pitch can run to ~70 KB; use
    `sections` to ask for less.

    Args:
        id (str):
        sections (list[GetCompanyPitchSectionsItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CompanyPitchEnvelope | Error
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            sections=sections,
        )
    ).parsed
