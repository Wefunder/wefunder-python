from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.attribution_stats_envelope import AttributionStatsEnvelope
from ...models.error import Error
from ...types import UNSET, Unset
from typing import cast
import datetime



def _get_kwargs(
    campaign_id: int,
    *,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

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


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/campaigns/{campaign_id}/attribution/stats".format(campaign_id=quote(str(campaign_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AttributionStatsEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = AttributionStatsEnvelope.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AttributionStatsEnvelope | Error]:
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
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,

) -> Response[AttributionStatsEnvelope | Error]:
    """ Get aggregate attribution statistics

     Returns aggregate attribution statistics for a campaign. This is a **Tier 0** endpoint
    available to all OAuth applications with the `read:attribution:aggregate` scope.

    Use this endpoint to:
    - Track overall marketing campaign performance
    - Measure conversion rates by UTM source/campaign
    - Monitor investment quality metrics
    - Build performance dashboards

    The response includes totals and breakdowns by UTM parameters. All counts exclude
    disputed attributions.

    **Privacy**: This endpoint returns aggregate data only. No individual investor
    information is exposed.

    Args:
        campaign_id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributionStatsEnvelope | Error]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,

) -> AttributionStatsEnvelope | Error | None:
    """ Get aggregate attribution statistics

     Returns aggregate attribution statistics for a campaign. This is a **Tier 0** endpoint
    available to all OAuth applications with the `read:attribution:aggregate` scope.

    Use this endpoint to:
    - Track overall marketing campaign performance
    - Measure conversion rates by UTM source/campaign
    - Monitor investment quality metrics
    - Build performance dashboards

    The response includes totals and breakdowns by UTM parameters. All counts exclude
    disputed attributions.

    **Privacy**: This endpoint returns aggregate data only. No individual investor
    information is exposed.

    Args:
        campaign_id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributionStatsEnvelope | Error
     """


    return sync_detailed(
        campaign_id=campaign_id,
client=client,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,

    ).parsed

async def asyncio_detailed(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,

) -> Response[AttributionStatsEnvelope | Error]:
    """ Get aggregate attribution statistics

     Returns aggregate attribution statistics for a campaign. This is a **Tier 0** endpoint
    available to all OAuth applications with the `read:attribution:aggregate` scope.

    Use this endpoint to:
    - Track overall marketing campaign performance
    - Measure conversion rates by UTM source/campaign
    - Monitor investment quality metrics
    - Build performance dashboards

    The response includes totals and breakdowns by UTM parameters. All counts exclude
    disputed attributions.

    **Privacy**: This endpoint returns aggregate data only. No individual investor
    information is exposed.

    Args:
        campaign_id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttributionStatsEnvelope | Error]
     """


    kwargs = _get_kwargs(
        campaign_id=campaign_id,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    campaign_id: int,
    *,
    client: AuthenticatedClient,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    utm_source: str | Unset = UNSET,
    utm_campaign: str | Unset = UNSET,

) -> AttributionStatsEnvelope | Error | None:
    """ Get aggregate attribution statistics

     Returns aggregate attribution statistics for a campaign. This is a **Tier 0** endpoint
    available to all OAuth applications with the `read:attribution:aggregate` scope.

    Use this endpoint to:
    - Track overall marketing campaign performance
    - Measure conversion rates by UTM source/campaign
    - Monitor investment quality metrics
    - Build performance dashboards

    The response includes totals and breakdowns by UTM parameters. All counts exclude
    disputed attributions.

    **Privacy**: This endpoint returns aggregate data only. No individual investor
    information is exposed.

    Args:
        campaign_id (int):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        utm_source (str | Unset):
        utm_campaign (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttributionStatsEnvelope | Error
     """


    return (await asyncio_detailed(
        campaign_id=campaign_id,
client=client,
start_date=start_date,
end_date=end_date,
utm_source=utm_source,
utm_campaign=utm_campaign,

    )).parsed
