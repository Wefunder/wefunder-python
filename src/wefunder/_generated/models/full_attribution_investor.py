from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FullAttributionInvestor")



@_attrs_define
class FullAttributionInvestor:
    """ Full investor details

        Attributes:
            id (int | Unset):  Example: 6789.
            name (str | Unset):  Example: John Smith.
            email (str | Unset):  Example: john@example.com.
            username (str | Unset):  Example: johnsmith.
     """

    id: int | Unset = UNSET
    name: str | Unset = UNSET
    email: str | Unset = UNSET
    username: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        email = self.email

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if email is not UNSET:
            field_dict["email"] = email
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        email = d.pop("email", UNSET)

        username = d.pop("username", UNSET)

        full_attribution_investor = cls(
            id=id,
            name=name,
            email=email,
            username=username,
        )


        full_attribution_investor.additional_properties = d
        return full_attribution_investor

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
