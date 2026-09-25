from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.company_update_type import CompanyUpdateType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.company_update_attributes import CompanyUpdateAttributes





T = TypeVar("T", bound="CompanyUpdate")



@_attrs_define
class CompanyUpdate:
    """ One post from a company's Posts tab. Plain text, never HTML.

        Attributes:
            id (None | str | Unset): The post's public id (its share token); pass as `update_id` for the full text.
            type_ (CompanyUpdateType | Unset):
            attributes (CompanyUpdateAttributes | Unset):
     """

    id: None | str | Unset = UNSET
    type_: CompanyUpdateType | Unset = UNSET
    attributes: CompanyUpdateAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.company_update_attributes import CompanyUpdateAttributes # noqa: PLC0415
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
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
        from ..models.company_update_attributes import CompanyUpdateAttributes # noqa: PLC0415
        d = dict(src_dict)
        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: CompanyUpdateType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = CompanyUpdateType(_type_)




        _attributes = d.pop("attributes", UNSET)
        attributes: CompanyUpdateAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = CompanyUpdateAttributes.from_dict(_attributes)




        company_update = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        company_update.additional_properties = d
        return company_update

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
