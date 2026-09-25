from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_disclosures_type import CompanyDisclosuresType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.company_disclosures_attributes import CompanyDisclosuresAttributes





T = TypeVar("T", bound="CompanyDisclosures")



@_attrs_define
class CompanyDisclosures:
    """ The company's public Form C disclosures (the site's Details tab), one section per key. A section is null when the
    company hides it on the site.

        Attributes:
            id (str | Unset): The company's id (`co_...`).
            type_ (CompanyDisclosuresType | Unset):
            attributes (CompanyDisclosuresAttributes | Unset):
     """

    id: str | Unset = UNSET
    type_: CompanyDisclosuresType | Unset = UNSET
    attributes: CompanyDisclosuresAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_disclosures_attributes import CompanyDisclosuresAttributes # noqa: PLC0415
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_disclosures_attributes import CompanyDisclosuresAttributes # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CompanyDisclosuresType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = CompanyDisclosuresType(_type_)




        _attributes = d.pop("attributes", UNSET)
        attributes: CompanyDisclosuresAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = CompanyDisclosuresAttributes.from_dict(_attributes)




        company_disclosures = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        company_disclosures.additional_properties = d
        return company_disclosures

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
