from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.followed_company_type import FollowedCompanyType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.followed_company_attributes import FollowedCompanyAttributes





T = TypeVar("T", bound="FollowedCompany")



@_attrs_define
class FollowedCompany:
    """ One company on the authenticated user's watchlist (GET /users/me/follows).

        Attributes:
            id (str | Unset): The company's id (`co_...`) for `GET /companies/{id}`. Example: co_8Kd0aB3xQ9k2vF8mNp1zT5wY.
            type_ (FollowedCompanyType | Unset):
            attributes (FollowedCompanyAttributes | Unset):
     """

    id: str | Unset = UNSET
    type_: FollowedCompanyType | Unset = UNSET
    attributes: FollowedCompanyAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.followed_company_attributes import FollowedCompanyAttributes # noqa: PLC0415
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
        from ..models.followed_company_attributes import FollowedCompanyAttributes # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FollowedCompanyType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = FollowedCompanyType(_type_)




        _attributes = d.pop("attributes", UNSET)
        attributes: FollowedCompanyAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = FollowedCompanyAttributes.from_dict(_attributes)




        followed_company = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        followed_company.additional_properties = d
        return followed_company

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
