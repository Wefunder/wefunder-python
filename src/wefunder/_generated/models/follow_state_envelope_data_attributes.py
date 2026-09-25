from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FollowStateEnvelopeDataAttributes")



@_attrs_define
class FollowStateEnvelopeDataAttributes:
    """ 
        Attributes:
            followed (bool | Unset): Whether the user follows the company after this call.
            changed (bool | Unset): Whether this call changed anything (false when already in the requested state).
     """

    followed: bool | Unset = UNSET
    changed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        followed = self.followed

        changed = self.changed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if followed is not UNSET:
            field_dict["followed"] = followed
        if changed is not UNSET:
            field_dict["changed"] = changed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        followed = d.pop("followed", UNSET)

        changed = d.pop("changed", UNSET)

        follow_state_envelope_data_attributes = cls(
            followed=followed,
            changed=changed,
        )


        follow_state_envelope_data_attributes.additional_properties = d
        return follow_state_envelope_data_attributes

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
