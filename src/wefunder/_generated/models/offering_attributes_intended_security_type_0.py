from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.offering_attributes_intended_security_type_0_type import OfferingAttributesIntendedSecurityType0Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="OfferingAttributesIntendedSecurityType0")


@_attrs_define
class OfferingAttributesIntendedSecurityType0:
    """Testing-the-Waters rounds only: the kind of security the company says it intends to
    issue when the round opens, with no terms (none are final). Null for a live round,
    and for a TTW round whose terms are still to be decided.

        Attributes:
            type_ (OfferingAttributesIntendedSecurityType0Type | Unset):
            label (str | Unset):  Example: SAFE.
    """

    type_: OfferingAttributesIntendedSecurityType0Type | Unset = UNSET
    label: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: OfferingAttributesIntendedSecurityType0Type | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OfferingAttributesIntendedSecurityType0Type(_type_)

        label = d.pop("label", UNSET)

        offering_attributes_intended_security_type_0 = cls(
            type_=type_,
            label=label,
        )

        offering_attributes_intended_security_type_0.additional_properties = d
        return offering_attributes_intended_security_type_0

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
