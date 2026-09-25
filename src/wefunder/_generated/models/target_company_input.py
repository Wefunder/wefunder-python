from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="TargetCompanyInput")



@_attrs_define
class TargetCompanyInput:
    """ 
        Attributes:
            name (str):  Example: Acme Inc.
            legal_name (str | Unset):  Example: Acme Inc..
            website (str | Unset):  Example: https://acme.com.
            description (str | Unset):  Example: AI-powered productivity tools.
            state_of_incorporation (str | Unset): Two-letter US state code. Example: DE.
     """

    name: str
    legal_name: str | Unset = UNSET
    website: str | Unset = UNSET
    description: str | Unset = UNSET
    state_of_incorporation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        legal_name = self.legal_name

        website = self.website

        description = self.description

        state_of_incorporation = self.state_of_incorporation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if website is not UNSET:
            field_dict["website"] = website
        if description is not UNSET:
            field_dict["description"] = description
        if state_of_incorporation is not UNSET:
            field_dict["state_of_incorporation"] = state_of_incorporation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        legal_name = d.pop("legal_name", UNSET)

        website = d.pop("website", UNSET)

        description = d.pop("description", UNSET)

        state_of_incorporation = d.pop("state_of_incorporation", UNSET)

        target_company_input = cls(
            name=name,
            legal_name=legal_name,
            website=website,
            description=description,
            state_of_incorporation=state_of_incorporation,
        )


        target_company_input.additional_properties = d
        return target_company_input

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
