from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemberLinkCreateInput")


@_attrs_define
class MemberLinkCreateInput:
    """
    Attributes:
        reference (str | Unset): Your opaque member id. Repeating it on the same offering returns the live link.
        wefunder_user_id (str | Unset): Pre-bind the link to a member whose Wefunder account you know (`usr_` id). A
            repeated `reference` naming a different account is a 409.
    """

    reference: str | Unset = UNSET
    wefunder_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reference = self.reference

        wefunder_user_id = self.wefunder_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference is not UNSET:
            field_dict["reference"] = reference
        if wefunder_user_id is not UNSET:
            field_dict["wefunder_user_id"] = wefunder_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        reference = d.pop("reference", UNSET)

        wefunder_user_id = d.pop("wefunder_user_id", UNSET)

        member_link_create_input = cls(
            reference=reference,
            wefunder_user_id=wefunder_user_id,
        )

        member_link_create_input.additional_properties = d
        return member_link_create_input

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
