from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_search_result_type import CompanySearchResultType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.company_search_result_attributes import CompanySearchResultAttributes





T = TypeVar("T", bound="CompanySearchResult")



@_attrs_define
class CompanySearchResult:
    """ One company from the site search bar (GET /companies/search).

        Attributes:
            id (str | Unset): The company's id (`co_...`) for `GET /companies/{id}`. Example: co_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            type_ (CompanySearchResultType | Unset):
            attributes (CompanySearchResultAttributes | Unset):
     """

    id: str | Unset = UNSET
    type_: CompanySearchResultType | Unset = UNSET
    attributes: CompanySearchResultAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_search_result_attributes import CompanySearchResultAttributes # noqa: PLC0415
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
        from ..models.company_search_result_attributes import CompanySearchResultAttributes # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: CompanySearchResultType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = CompanySearchResultType(_type_)




        _attributes = d.pop("attributes", UNSET)
        attributes: CompanySearchResultAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = CompanySearchResultAttributes.from_dict(_attributes)




        company_search_result = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        company_search_result.additional_properties = d
        return company_search_result

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
