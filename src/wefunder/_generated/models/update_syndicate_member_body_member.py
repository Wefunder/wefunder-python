from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateSyndicateMemberBodyMember")



@_attrs_define
class UpdateSyndicateMemberBodyMember:
    """ 
        Attributes:
            title (str | Unset):  Example: Lead Investor.
            carry_percentage_override (str | Unset):  Example: 20.0.
     """

    title: str | Unset = UNSET
    carry_percentage_override: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        carry_percentage_override = self.carry_percentage_override


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if carry_percentage_override is not UNSET:
            field_dict["carry_percentage_override"] = carry_percentage_override

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        carry_percentage_override = d.pop("carry_percentage_override", UNSET)

        update_syndicate_member_body_member = cls(
            title=title,
            carry_percentage_override=carry_percentage_override,
        )


        update_syndicate_member_body_member.additional_properties = d
        return update_syndicate_member_body_member

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
