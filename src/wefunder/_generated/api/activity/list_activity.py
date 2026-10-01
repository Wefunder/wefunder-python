import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_event_list_envelope import AuditEventListEnvelope
from ...models.error import Error
from ...models.list_activity_status import ListActivityStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    app_id: int | Unset = UNSET,
    action_pattern: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    status: ListActivityStatus | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["app_id"] = app_id

    params["action_pattern"] = action_pattern

    params["resource_type"] = resource_type

    params["resource_id"] = resource_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_since: str | Unset = UNSET
    if not isinstance(since, Unset):
        json_since = since.isoformat()
    params["since"] = json_since

    json_until: str | Unset = UNSET
    if not isinstance(until, Unset):
        json_until = until.isoformat()
    params["until"] = json_until

    params["cursor"] = cursor

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/activity",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditEventListEnvelope | Error | None:
    if response.status_code == 200:
        response_200 = AuditEventListEnvelope.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Error.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditEventListEnvelope | Error]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    app_id: int | Unset = UNSET,
    action_pattern: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    status: ListActivityStatus | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[AuditEventListEnvelope | Error]:
    """List activity events

     Returns actions taken by OAuth apps authorized by the current user.
    This is the API backing the user-facing activity feed at Settings > Activity.

    Args:
        app_id (int | Unset):
        action_pattern (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        status (ListActivityStatus | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        action_pattern=action_pattern,
        resource_type=resource_type,
        resource_id=resource_id,
        status=status,
        since=since,
        until=until,
        cursor=cursor,
        per_page=per_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    app_id: int | Unset = UNSET,
    action_pattern: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    status: ListActivityStatus | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> AuditEventListEnvelope | Error | None:
    """List activity events

     Returns actions taken by OAuth apps authorized by the current user.
    This is the API backing the user-facing activity feed at Settings > Activity.

    Args:
        app_id (int | Unset):
        action_pattern (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        status (ListActivityStatus | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventListEnvelope | Error
    """

    return sync_detailed(
        client=client,
        app_id=app_id,
        action_pattern=action_pattern,
        resource_type=resource_type,
        resource_id=resource_id,
        status=status,
        since=since,
        until=until,
        cursor=cursor,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    app_id: int | Unset = UNSET,
    action_pattern: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    status: ListActivityStatus | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> Response[AuditEventListEnvelope | Error]:
    """List activity events

     Returns actions taken by OAuth apps authorized by the current user.
    This is the API backing the user-facing activity feed at Settings > Activity.

    Args:
        app_id (int | Unset):
        action_pattern (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        status (ListActivityStatus | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditEventListEnvelope | Error]
    """

    kwargs = _get_kwargs(
        app_id=app_id,
        action_pattern=action_pattern,
        resource_type=resource_type,
        resource_id=resource_id,
        status=status,
        since=since,
        until=until,
        cursor=cursor,
        per_page=per_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    app_id: int | Unset = UNSET,
    action_pattern: str | Unset = UNSET,
    resource_type: str | Unset = UNSET,
    resource_id: str | Unset = UNSET,
    status: ListActivityStatus | Unset = UNSET,
    since: datetime.datetime | Unset = UNSET,
    until: datetime.datetime | Unset = UNSET,
    cursor: str | Unset = UNSET,
    per_page: int | Unset = 25,
) -> AuditEventListEnvelope | Error | None:
    """List activity events

     Returns actions taken by OAuth apps authorized by the current user.
    This is the API backing the user-facing activity feed at Settings > Activity.

    Args:
        app_id (int | Unset):
        action_pattern (str | Unset):
        resource_type (str | Unset):
        resource_id (str | Unset):
        status (ListActivityStatus | Unset):
        since (datetime.datetime | Unset):
        until (datetime.datetime | Unset):
        cursor (str | Unset):
        per_page (int | Unset):  Default: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditEventListEnvelope | Error
    """

    return (
        await asyncio_detailed(
            client=client,
            app_id=app_id,
            action_pattern=action_pattern,
            resource_type=resource_type,
            resource_id=resource_id,
            status=status,
            since=since,
            until=until,
            cursor=cursor,
            per_page=per_page,
        )
    ).parsed
