from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectedAppAttributes")


@_attrs_define
class ConnectedAppAttributes:
    """
    Attributes:
        name (str | Unset):  Example: ChatGPT via Wefunder MCP.
        scopes (list[str] | Unset): All scopes across active tokens for this app Example: ['read:syndicates',
            'write:syndicates'].
        last_active_at (datetime.datetime | None | Unset): When the most recent token was last used Example:
            2025-03-01T12:00:00Z.
        action_count (int | Unset): Total audit events for this app Example: 34.
        created_at (datetime.datetime | None | Unset): When the user first authorized this app Example:
            2025-03-01T12:00:00Z.
    """

    name: str | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    last_active_at: datetime.datetime | None | Unset = UNSET
    action_count: int | Unset = UNSET
    created_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        last_active_at: None | str | Unset
        if isinstance(self.last_active_at, Unset):
            last_active_at = UNSET
        elif isinstance(self.last_active_at, datetime.datetime):
            last_active_at = self.last_active_at.isoformat()
        else:
            last_active_at = self.last_active_at

        action_count = self.action_count

        created_at: None | str | Unset
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if last_active_at is not UNSET:
            field_dict["last_active_at"] = last_active_at
        if action_count is not UNSET:
            field_dict["action_count"] = action_count
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        def _parse_last_active_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_active_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_active_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_active_at = _parse_last_active_at(d.pop("last_active_at", UNSET))

        action_count = d.pop("action_count", UNSET)

        def _parse_created_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = datetime.datetime.fromisoformat(data)

                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_at = _parse_created_at(d.pop("created_at", UNSET))

        connected_app_attributes = cls(
            name=name,
            scopes=scopes,
            last_active_at=last_active_at,
            action_count=action_count,
            created_at=created_at,
        )

        connected_app_attributes.additional_properties = d
        return connected_app_attributes

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
