from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_pitch_type import CompanyPitchType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_pitch_attributes import CompanyPitchAttributes


T = TypeVar("T", bound="CompanyPitch")


@_attrs_define
class CompanyPitch:
    """The company page's pitch (the Overview tab's story) as ordered blocks, plus the round's perk tiers.

    Attributes:
        id (str | Unset): The company's id (`co_...`).
        type_ (CompanyPitchType | Unset):
        attributes (CompanyPitchAttributes | Unset):
    """

    id: str | Unset = UNSET
    type_: CompanyPitchType | Unset = UNSET
    attributes: CompanyPitchAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_pitch_attributes import CompanyPitchAttributes  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CompanyPitchType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CompanyPitchType(_type_)

        _attributes = d.pop("attributes", UNSET)
        attributes: CompanyPitchAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = CompanyPitchAttributes.from_dict(_attributes)

        company_pitch = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        company_pitch.additional_properties = d
        return company_pitch

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
