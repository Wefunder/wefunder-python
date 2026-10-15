from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_referral_code_body import CreateReferralCodeBody
from ...models.error import Error
from ...models.referral_code_envelope import ReferralCodeEnvelope
from ...types import Response


def _get_kwargs(
    *,
    body: CreateReferralCodeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/referral_codes",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | ReferralCodeEnvelope | None:
    if response.status_code == 201:
        response_201 = ReferralCodeEnvelope.from_dict(response.json())

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

    if response.status_code == 422:
        response_422 = Error.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error | ReferralCodeEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateReferralCodeBody,
) -> Response[Error | ReferralCodeEnvelope]:
    """Create a referral code

     Mints a referral code for your application. No relationship with the company is needed.
    Put it on any wefunder.com link as `?wfr=<id>`.

    Before its first code, your organization must accept the referral attribution terms once:
    Wefunder does not pay partners per referral, and a partner may not be compensated per
    referral unless it is a registered broker-dealer. Until an owner or admin accepts them in
    the developer portal, this returns `422 attribution_terms_required` with
    `details.acceptance_url`.

    An application may have at most 500 active codes (`422 quota_exceeded`); deactivate codes
    you no longer use. UTM presets fill blank `utm_*` fields on visits that carry the code. A
    `source` or `campaign` starting with `wf_` is reserved for Wefunder's own channels and
    returns `422 reserved_utm_prefix`. Idempotency keys are not supported here: a retried
    request may create a second code, which you can deactivate.

    Args:
        body (CreateReferralCodeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReferralCodeEnvelope]
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
    body: CreateReferralCodeBody,
) -> Error | ReferralCodeEnvelope | None:
    """Create a referral code

     Mints a referral code for your application. No relationship with the company is needed.
    Put it on any wefunder.com link as `?wfr=<id>`.

    Before its first code, your organization must accept the referral attribution terms once:
    Wefunder does not pay partners per referral, and a partner may not be compensated per
    referral unless it is a registered broker-dealer. Until an owner or admin accepts them in
    the developer portal, this returns `422 attribution_terms_required` with
    `details.acceptance_url`.

    An application may have at most 500 active codes (`422 quota_exceeded`); deactivate codes
    you no longer use. UTM presets fill blank `utm_*` fields on visits that carry the code. A
    `source` or `campaign` starting with `wf_` is reserved for Wefunder's own channels and
    returns `422 reserved_utm_prefix`. Idempotency keys are not supported here: a retried
    request may create a second code, which you can deactivate.

    Args:
        body (CreateReferralCodeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReferralCodeEnvelope
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateReferralCodeBody,
) -> Response[Error | ReferralCodeEnvelope]:
    """Create a referral code

     Mints a referral code for your application. No relationship with the company is needed.
    Put it on any wefunder.com link as `?wfr=<id>`.

    Before its first code, your organization must accept the referral attribution terms once:
    Wefunder does not pay partners per referral, and a partner may not be compensated per
    referral unless it is a registered broker-dealer. Until an owner or admin accepts them in
    the developer portal, this returns `422 attribution_terms_required` with
    `details.acceptance_url`.

    An application may have at most 500 active codes (`422 quota_exceeded`); deactivate codes
    you no longer use. UTM presets fill blank `utm_*` fields on visits that carry the code. A
    `source` or `campaign` starting with `wf_` is reserved for Wefunder's own channels and
    returns `422 reserved_utm_prefix`. Idempotency keys are not supported here: a retried
    request may create a second code, which you can deactivate.

    Args:
        body (CreateReferralCodeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | ReferralCodeEnvelope]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateReferralCodeBody,
) -> Error | ReferralCodeEnvelope | None:
    """Create a referral code

     Mints a referral code for your application. No relationship with the company is needed.
    Put it on any wefunder.com link as `?wfr=<id>`.

    Before its first code, your organization must accept the referral attribution terms once:
    Wefunder does not pay partners per referral, and a partner may not be compensated per
    referral unless it is a registered broker-dealer. Until an owner or admin accepts them in
    the developer portal, this returns `422 attribution_terms_required` with
    `details.acceptance_url`.

    An application may have at most 500 active codes (`422 quota_exceeded`); deactivate codes
    you no longer use. UTM presets fill blank `utm_*` fields on visits that carry the code. A
    `source` or `campaign` starting with `wf_` is reserved for Wefunder's own channels and
    returns `422 reserved_utm_prefix`. Idempotency keys are not supported here: a retried
    request may create a second code, which you can deactivate.

    Args:
        body (CreateReferralCodeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | ReferralCodeEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
