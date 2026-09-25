from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CompanyDisclosuresAttributesCapitalStructureType0Item")



@_attrs_define
class CompanyDisclosuresAttributesCapitalStructureType0Item:
    """ 
        Attributes:
            class_of_security (None | str | Unset):
            authorized (None | str | Unset):
            outstanding (None | str | Unset):
            voting_rights (None | str | Unset):
            other_rights (None | str | Unset):
     """

    class_of_security: None | str | Unset = UNSET
    authorized: None | str | Unset = UNSET
    outstanding: None | str | Unset = UNSET
    voting_rights: None | str | Unset = UNSET
    other_rights: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        class_of_security: None | str | Unset
        if isinstance(self.class_of_security, Unset):
            class_of_security = UNSET
        else:
            class_of_security = self.class_of_security

        authorized: None | str | Unset
        if isinstance(self.authorized, Unset):
            authorized = UNSET
        else:
            authorized = self.authorized

        outstanding: None | str | Unset
        if isinstance(self.outstanding, Unset):
            outstanding = UNSET
        else:
            outstanding = self.outstanding

        voting_rights: None | str | Unset
        if isinstance(self.voting_rights, Unset):
            voting_rights = UNSET
        else:
            voting_rights = self.voting_rights

        other_rights: None | str | Unset
        if isinstance(self.other_rights, Unset):
            other_rights = UNSET
        else:
            other_rights = self.other_rights


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if class_of_security is not UNSET:
            field_dict["class_of_security"] = class_of_security
        if authorized is not UNSET:
            field_dict["authorized"] = authorized
        if outstanding is not UNSET:
            field_dict["outstanding"] = outstanding
        if voting_rights is not UNSET:
            field_dict["voting_rights"] = voting_rights
        if other_rights is not UNSET:
            field_dict["other_rights"] = other_rights

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_class_of_security(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        class_of_security = _parse_class_of_security(d.pop("class_of_security", UNSET))


        def _parse_authorized(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        authorized = _parse_authorized(d.pop("authorized", UNSET))


        def _parse_outstanding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outstanding = _parse_outstanding(d.pop("outstanding", UNSET))


        def _parse_voting_rights(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voting_rights = _parse_voting_rights(d.pop("voting_rights", UNSET))


        def _parse_other_rights(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        other_rights = _parse_other_rights(d.pop("other_rights", UNSET))


        company_disclosures_attributes_capital_structure_type_0_item = cls(
            class_of_security=class_of_security,
            authorized=authorized,
            outstanding=outstanding,
            voting_rights=voting_rights,
            other_rights=other_rights,
        )


        company_disclosures_attributes_capital_structure_type_0_item.additional_properties = d
        return company_disclosures_attributes_capital_structure_type_0_item

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
