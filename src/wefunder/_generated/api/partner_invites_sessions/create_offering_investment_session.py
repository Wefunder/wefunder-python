from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_offering_investment_session_body import CreateOfferingInvestmentSessionBody
from ...models.error import Error
from ...models.investment_session_envelope import InvestmentSessionEnvelope
from ...models.validation_error import ValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    body: CreateOfferingInvestmentSessionBody,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/offerings/{id}/investment_sessions".format(
            id=quote(str(id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error | InvestmentSessionEnvelope | ValidationError | None:
    if response.status_code == 201:
        response_201 = InvestmentSessionEnvelope.from_dict(response.json())

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

    if response.status_code == 409:
        response_409 = Error.from_dict(response.json())

        return response_409

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
    body: CreateOfferingInvestmentSessionBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | InvestmentSessionEnvelope | ValidationError]:
    """Create an investment session

     Canonical path: the offering comes from the URL, so `spv_id` may be
    omitted from the body (if sent it must match, else 422 `offering_mismatch`).
    Authorized for any offering the caller may act on (an install on its
    syndicate or company, a role on it, or created by your app).

    Creates a single-use, recipient-specific hosted investment session (analogous to
    a Stripe Checkout Session) on the SPV named by `spv_id` in the body. The session
    walks one investor through accreditation, document signing, and payment, and
    produces a durable `Investment` on success. Returns a `url` the recipient opens
    to begin. If the recipient already has an active session on the SPV, that
    session is returned instead of creating a duplicate; if another app holds
    that recipient's active session there, the create is refused with 409
    `session_conflict` (a recipient has one active session per offering).

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingInvestmentSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvestmentSessionEnvelope | ValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateOfferingInvestmentSessionBody,
    idempotency_key: str | Unset = UNSET,
) -> Error | InvestmentSessionEnvelope | ValidationError | None:
    """Create an investment session

     Canonical path: the offering comes from the URL, so `spv_id` may be
    omitted from the body (if sent it must match, else 422 `offering_mismatch`).
    Authorized for any offering the caller may act on (an install on its
    syndicate or company, a role on it, or created by your app).

    Creates a single-use, recipient-specific hosted investment session (analogous to
    a Stripe Checkout Session) on the SPV named by `spv_id` in the body. The session
    walks one investor through accreditation, document signing, and payment, and
    produces a durable `Investment` on success. Returns a `url` the recipient opens
    to begin. If the recipient already has an active session on the SPV, that
    session is returned instead of creating a duplicate; if another app holds
    that recipient's active session there, the create is refused with 409
    `session_conflict` (a recipient has one active session per offering).

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingInvestmentSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error | InvestmentSessionEnvelope | ValidationError
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateOfferingInvestmentSessionBody,
    idempotency_key: str | Unset = UNSET,
) -> Response[Error | InvestmentSessionEnvelope | ValidationError]:
    """Create an investment session

     Canonical path: the offering comes from the URL, so `spv_id` may be
    omitted from the body (if sent it must match, else 422 `offering_mismatch`).
    Authorized for any offering the caller may act on (an install on its
    syndicate or company, a role on it, or created by your app).

    Creates a single-use, recipient-specific hosted investment session (analogous to
    a Stripe Checkout Session) on the SPV named by `spv_id` in the body. The session
    walks one investor through accreditation, document signing, and payment, and
    produces a durable `Investment` on success. Returns a `url` the recipient opens
    to begin. If the recipient already has an active session on the SPV, that
    session is returned instead of creating a duplicate; if another app holds
    that recipient's active session there, the create is refused with 409
    `session_conflict` (a recipient has one active session per offering).

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingInvestmentSessionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error | InvestmentSessionEnvelope | ValidationError]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: CreateOfferingInvestmentSessionBody,
    idempotency_key: str | Unset = UNSET,
) -> Error | InvestmentSessionEnvelope | ValidationError | None:
    """Create an investment session

     Canonical path: the offering comes from the URL, so `spv_id` may be
    omitted from the body (if sent it must match, else 422 `offering_mismatch`).
    Authorized for any offering the caller may act on (an install on its
    syndicate or company, a role on it, or created by your app).

    Creates a single-use, recipient-specific hosted investment session (analogous to
    a Stripe Checkout Session) on the SPV named by `spv_id` in the body. The session
    walks one investor through accreditation, document signing, and payment, and
    produces a durable `Investment` on success. Returns a `url` the recipient opens
    to begin. If the recipient already has an active session on the SPV, that
    session is returned instead of creating a duplicate; if another app holds
    that recipient's active session there, the create is refused with 409
    `session_conflict` (a recipient has one active session per offering).

    Args:
        id (str):
        idempotency_key (str | Unset):
        body (CreateOfferingInvestmentSessionBody):

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
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
