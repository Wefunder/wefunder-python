from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.installation_attributes_target_type import InstallationAttributesTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InstallationAttributesTarget")


@_attrs_define
class InstallationAttributesTarget:
    """
    Attributes:
        type_ (InstallationAttributesTargetType | Unset):
        id (str | Unset): `co_…` or `syn_…`
        name (str | Unset):
    """

    type_: InstallationAttributesTargetType | Unset = UNSET
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        id = self.id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: InstallationAttributesTargetType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = InstallationAttributesTargetType(_type_)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        installation_attributes_target = cls(
            type_=type_,
            id=id,
            name=name,
        )

        installation_attributes_target.additional_properties = d
        return installation_attributes_target

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
