from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CompanyDisclosuresAttributesVotingPowerType0Item")



@_attrs_define
class CompanyDisclosuresAttributesVotingPowerType0Item:
    """ 
        Attributes:
            name (None | str | Unset):
            holding (None | str | Unset): Number and class of securities held, as disclosed.
            voting_power_percent (None | str | Unset):
     """

    name: None | str | Unset = UNSET
    holding: None | str | Unset = UNSET
    voting_power_percent: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        holding: None | str | Unset
        if isinstance(self.holding, Unset):
            holding = UNSET
        else:
            holding = self.holding

        voting_power_percent: None | str | Unset
        if isinstance(self.voting_power_percent, Unset):
            voting_power_percent = UNSET
        else:
            voting_power_percent = self.voting_power_percent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if holding is not UNSET:
            field_dict["holding"] = holding
        if voting_power_percent is not UNSET:
            field_dict["voting_power_percent"] = voting_power_percent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_holding(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        holding = _parse_holding(d.pop("holding", UNSET))


        def _parse_voting_power_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        voting_power_percent = _parse_voting_power_percent(d.pop("voting_power_percent", UNSET))


        company_disclosures_attributes_voting_power_type_0_item = cls(
            name=name,
            holding=holding,
            voting_power_percent=voting_power_percent,
        )


        company_disclosures_attributes_voting_power_type_0_item.additional_properties = d
        return company_disclosures_attributes_voting_power_type_0_item

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
