from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.installation_attributes_status import InstallationAttributesStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.installation_attributes_target import InstallationAttributesTarget


T = TypeVar("T", bound="InstallationAttributes")


@_attrs_define
class InstallationAttributes:
    """
    Attributes:
        target (InstallationAttributesTarget | Unset):
        tier (str | Unset): founder / admin / editor for a company; full_access / operator for a syndicate.
        scopes (list[str] | Unset):
        status (InstallationAttributesStatus | Unset):
        installed_at (datetime.datetime | Unset):
        installed_by (None | str | Unset):
        revoked_at (datetime.datetime | None | Unset):
    """

    target: InstallationAttributesTarget | Unset = UNSET
    tier: str | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    status: InstallationAttributesStatus | Unset = UNSET
    installed_at: datetime.datetime | Unset = UNSET
    installed_by: None | str | Unset = UNSET
    revoked_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        target: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.to_dict()

        tier = self.tier

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        installed_at: str | Unset = UNSET
        if not isinstance(self.installed_at, Unset):
            installed_at = self.installed_at.isoformat()

        installed_by: None | str | Unset
        if isinstance(self.installed_by, Unset):
            installed_by = UNSET
        else:
            installed_by = self.installed_by

        revoked_at: None | str | Unset
        if isinstance(self.revoked_at, Unset):
            revoked_at = UNSET
        elif isinstance(self.revoked_at, datetime.datetime):
            revoked_at = self.revoked_at.isoformat()
        else:
            revoked_at = self.revoked_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target is not UNSET:
            field_dict["target"] = target
        if tier is not UNSET:
            field_dict["tier"] = tier
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if status is not UNSET:
            field_dict["status"] = status
        if installed_at is not UNSET:
            field_dict["installed_at"] = installed_at
        if installed_by is not UNSET:
            field_dict["installed_by"] = installed_by
        if revoked_at is not UNSET:
            field_dict["revoked_at"] = revoked_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.installation_attributes_target import InstallationAttributesTarget  # noqa: PLC0415

        d = dict(src_dict)
        _target = d.pop("target", UNSET)
        target: InstallationAttributesTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = InstallationAttributesTarget.from_dict(_target)

        tier = d.pop("tier", UNSET)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        _status = d.pop("status", UNSET)
        status: InstallationAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = InstallationAttributesStatus(_status)

        _installed_at = d.pop("installed_at", UNSET)
        installed_at: datetime.datetime | Unset
        if isinstance(_installed_at, Unset):
            installed_at = UNSET
        else:
            installed_at = datetime.datetime.fromisoformat(_installed_at)

        def _parse_installed_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        installed_by = _parse_installed_by(d.pop("installed_by", UNSET))

        def _parse_revoked_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revoked_at_type_0 = datetime.datetime.fromisoformat(data)

                return revoked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        revoked_at = _parse_revoked_at(d.pop("revoked_at", UNSET))

        installation_attributes = cls(
            target=target,
            tier=tier,
            scopes=scopes,
            status=status,
            installed_at=installed_at,
            installed_by=installed_by,
            revoked_at=revoked_at,
        )

        installation_attributes.additional_properties = d
        return installation_attributes

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
