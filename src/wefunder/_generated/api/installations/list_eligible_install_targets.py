from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.eligible_target_list_envelope import EligibleTargetListEnvelope
from ...models.error import Error
from ...models.list_eligible_install_targets_target_type import ListEligibleInstallTargetsTargetType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    target_type: ListEligibleInstallTargetsTargetType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_target_type: str | Unset = UNSET
    if not isinstance(target_type, Unset):
        json_target_type = target_type.value

    params["target_type"] = json_target_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/installations/eligible",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> EligibleTargetListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = EligibleTargetListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error.from_dict(response.json())

        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[EligibleTargetListEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    target_type: ListEligibleInstallTargetsTargetType | Unset = UNSET,
) -> Response[EligibleTargetListEnvelope | Error]:
    """List where you can install your app

     Companies the token's user can edit and syndicates they manage, with the tier an install would
    be granted at and the current install if one exists. Requires a token authorized by a user.

    Args:
        target_type (ListEligibleInstallTargetsTargetType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EligibleTargetListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    target_type: ListEligibleInstallTargetsTargetType | Unset = UNSET,
) -> EligibleTargetListEnvelope | Error | None:
    """List where you can install your app

     Companies the token's user can edit and syndicates they manage, with the tier an install would
    be granted at and the current install if one exists. Requires a token authorized by a user.

    Args:
        target_type (ListEligibleInstallTargetsTargetType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EligibleTargetListEnvelope | Error
    """

    return sync_detailed(
        client=client,
        target_type=target_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    target_type: ListEligibleInstallTargetsTargetType | Unset = UNSET,
) -> Response[EligibleTargetListEnvelope | Error]:
    """List where you can install your app

     Companies the token's user can edit and syndicates they manage, with the tier an install would
    be granted at and the current install if one exists. Requires a token authorized by a user.

    Args:
        target_type (ListEligibleInstallTargetsTargetType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EligibleTargetListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        target_type=target_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    target_type: ListEligibleInstallTargetsTargetType | Unset = UNSET,
) -> EligibleTargetListEnvelope | Error | None:
    """List where you can install your app

     Companies the token's user can edit and syndicates they manage, with the tier an install would
    be granted at and the current install if one exists. Requires a token authorized by a user.

    Args:
        target_type (ListEligibleInstallTargetsTargetType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EligibleTargetListEnvelope | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            target_type=target_type,
        )
    ).parsed
