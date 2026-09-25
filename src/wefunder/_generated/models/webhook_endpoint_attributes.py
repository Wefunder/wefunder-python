from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_endpoint_attributes_mode import WebhookEndpointAttributesMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="WebhookEndpointAttributes")


@_attrs_define
class WebhookEndpointAttributes:
    """
    Attributes:
        url (str | Unset):
        mode (WebhookEndpointAttributesMode | Unset):
        events (list[str] | Unset):
        enabled (bool | Unset):
        secret (str | Unset): Signing secret. Present only in create and rotate_secret responses.
        failing_since (datetime.datetime | None | Unset):
        last_delivery_at (datetime.datetime | None | Unset):
        last_delivery_status (None | str | Unset): Outcome of the most recent delivery: the HTTP status code as a string
            (for
            example `"200"` or `"503"`), or, when no response came back, one of
            `timeout`, `blocked_url`, `tls_error`, `connection_failed`.
             Example: 200.
        created_at (datetime.datetime | Unset):
    """

    url: str | Unset = UNSET
    mode: WebhookEndpointAttributesMode | Unset = UNSET
    events: list[str] | Unset = UNSET
    enabled: bool | Unset = UNSET
    secret: str | Unset = UNSET
    failing_since: datetime.datetime | None | Unset = UNSET
    last_delivery_at: datetime.datetime | None | Unset = UNSET
    last_delivery_status: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events

        enabled = self.enabled

        secret = self.secret

        failing_since: None | str | Unset
        if isinstance(self.failing_since, Unset):
            failing_since = UNSET
        elif isinstance(self.failing_since, datetime.datetime):
            failing_since = self.failing_since.isoformat()
        else:
            failing_since = self.failing_since

        last_delivery_at: None | str | Unset
        if isinstance(self.last_delivery_at, Unset):
            last_delivery_at = UNSET
        elif isinstance(self.last_delivery_at, datetime.datetime):
            last_delivery_at = self.last_delivery_at.isoformat()
        else:
            last_delivery_at = self.last_delivery_at

        last_delivery_status: None | str | Unset
        if isinstance(self.last_delivery_status, Unset):
            last_delivery_status = UNSET
        else:
            last_delivery_status = self.last_delivery_status

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if mode is not UNSET:
            field_dict["mode"] = mode
        if events is not UNSET:
            field_dict["events"] = events
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if secret is not UNSET:
            field_dict["secret"] = secret
        if failing_since is not UNSET:
            field_dict["failing_since"] = failing_since
        if last_delivery_at is not UNSET:
            field_dict["last_delivery_at"] = last_delivery_at
        if last_delivery_status is not UNSET:
            field_dict["last_delivery_status"] = last_delivery_status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: WebhookEndpointAttributesMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = WebhookEndpointAttributesMode(_mode)

        events = cast(list[str], d.pop("events", UNSET))

        enabled = d.pop("enabled", UNSET)

        secret = d.pop("secret", UNSET)

        def _parse_failing_since(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failing_since_type_0 = datetime.datetime.fromisoformat(data)

                return failing_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        failing_since = _parse_failing_since(d.pop("failing_since", UNSET))

        def _parse_last_delivery_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_delivery_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_delivery_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_delivery_at = _parse_last_delivery_at(d.pop("last_delivery_at", UNSET))

        def _parse_last_delivery_status(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_delivery_status = _parse_last_delivery_status(d.pop("last_delivery_status", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        webhook_endpoint_attributes = cls(
            url=url,
            mode=mode,
            events=events,
            enabled=enabled,
            secret=secret,
            failing_since=failing_since,
            last_delivery_at=last_delivery_at,
            last_delivery_status=last_delivery_status,
            created_at=created_at,
        )

        webhook_endpoint_attributes.additional_properties = d
        return webhook_endpoint_attributes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
