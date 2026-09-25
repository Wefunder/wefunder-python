from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.attributed_investment_list_envelope import AttributedInvestmentListEnvelope
from ...models.error import Error
from ...models.list_attributed_investments_detail_level import ListAttributedInvestmentsDetailLevel
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    campaign_id: int,
    *,
    cursor: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    detail_level: ListAttributedInvestmentsDetailLevel | Unset = ListAttributedInvestmentsDetailLevel.ANONYMIZED,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["cursor"] = cursor

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["utm_source"] = utm_source

    params["utm_campaign"] = utm_campaign

    json_detail_level: str | Unset = UNSET
    if not isinstance(detail_level, Unset):
        json_detail_level = detail_level.value

    params["detail_level"] = json_detail_level


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/campaigns/{campaign_id}/attribution/investments".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttributedInvestmentListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = AttributedInvestmentListEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AttributedInvestmentListEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    detail_level: ListAttributedInvestmentsDetailLevel | Unset = ListAttributedInvestmentsDetailLevel.ANONYMIZED,

) -> Response[AttributedInvestmentListEnvelope | Error]:
    """ List attributed investments

     Returns a list of attributed investments. The detail level depends on your access:

    **Tier 1 (Marketing Partners)** - Anonymized data:
    - Investor identity represented by opaque tokens (not real IDs)
    - Tokens are campaign-scoped (different token per campaign for same investor)
    - Investment amounts shown as tiers (small/medium/large), not exact values
    - No PII (email, name, address) is returned

    **Tier 2 (Founders/Employees)** - Full data with `detail_level=full`:
    - Real investment IDs (linkable to Wefunder admin)
    - Investor name, email, and username
    - Exact dollar amounts

    **Access**: Requires Tier 1+ access approval from Wefunder admin.

    Args:
        campaign_id (int):
        cursor (int | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):
        detail_level (ListAttributedInvestmentsDetailLevel | Unset):  Default:
            ListAttributedInvestmentsDetailLevel.ANONYMIZED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributedInvestmentListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
cursor=cursor,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,
detail_level=detail_level,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    detail_level: ListAttributedInvestmentsDetailLevel | Unset = ListAttributedInvestmentsDetailLevel.ANONYMIZED,

) -> AttributedInvestmentListEnvelope | Error | None:
    """ List attributed investments

     Returns a list of attributed investments. The detail level depends on your access:

    **Tier 1 (Marketing Partners)** - Anonymized data:
    - Investor identity represented by opaque tokens (not real IDs)
    - Tokens are campaign-scoped (different token per campaign for same investor)
    - Investment amounts shown as tiers (small/medium/large), not exact values
    - No PII (email, name, address) is returned

    **Tier 2 (Founders/Employees)** - Full data with `detail_level=full`:
    - Real investment IDs (linkable to Wefunder admin)
    - Investor name, email, and username
    - Exact dollar amounts

    **Access**: Requires Tier 1+ access approval from Wefunder admin.

    Args:
        campaign_id (int):
        cursor (int | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):
        detail_level (ListAttributedInvestmentsDetailLevel | Unset):  Default:
            ListAttributedInvestmentsDetailLevel.ANONYMIZED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributedInvestmentListEnvelope | Error
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
cursor=cursor,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,
detail_level=detail_level,

    ).parsed

async def asyncio_detailed(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    detail_level: ListAttributedInvestmentsDetailLevel | Unset = ListAttributedInvestmentsDetailLevel.ANONYMIZED,

) -> Response[AttributedInvestmentListEnvelope | Error]:
    """ List attributed investments

     Returns a list of attributed investments. The detail level depends on your access:

    **Tier 1 (Marketing Partners)** - Anonymized data:
    - Investor identity represented by opaque tokens (not real IDs)
    - Tokens are campaign-scoped (different token per campaign for same investor)
    - Investment amounts shown as tiers (small/medium/large), not exact values
    - No PII (email, name, address) is returned

    **Tier 2 (Founders/Employees)** - Full data with `detail_level=full`:
    - Real investment IDs (linkable to Wefunder admin)
    - Investor name, email, and username
    - Exact dollar amounts

    **Access**: Requires Tier 1+ access approval from Wefunder admin.

    Args:
        campaign_id (int):
        cursor (int | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):
        detail_level (ListAttributedInvestmentsDetailLevel | Unset):  Default:
            ListAttributedInvestmentsDetailLevel.ANONYMIZED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributedInvestmentListEnvelope | Error]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
cursor=cursor,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,
detail_level=detail_level,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    cursor: int | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,
    detail_level: ListAttributedInvestmentsDetailLevel | Unset = ListAttributedInvestmentsDetailLevel.ANONYMIZED,

) -> AttributedInvestmentListEnvelope | Error | None:
    """ List attributed investments

     Returns a list of attributed investments. The detail level depends on your access:

    **Tier 1 (Marketing Partners)** - Anonymized data:
    - Investor identity represented by opaque tokens (not real IDs)
    - Tokens are campaign-scoped (different token per campaign for same investor)
    - Investment amounts shown as tiers (small/medium/large), not exact values
    - No PII (email, name, address) is returned

    **Tier 2 (Founders/Employees)** - Full data with `detail_level=full`:
    - Real investment IDs (linkable to Wefunder admin)
    - Investor name, email, and username
    - Exact dollar amounts

    **Access**: Requires Tier 1+ access approval from Wefunder admin.

    Args:
        campaign_id (int):
        cursor (int | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):
        detail_level (ListAttributedInvestmentsDetailLevel | Unset):  Default:
            ListAttributedInvestmentsDetailLevel.ANONYMIZED.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributedInvestmentListEnvelope | Error
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
cursor=cursor,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,
detail_level=detail_level,

    )).parsed
