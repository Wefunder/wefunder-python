from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="InvestmentDeltaRecordContractsItem")



@_attrs_define
class InvestmentDeltaRecordContractsItem:
    """ 
        Attributes:
            name (None | str | Unset):
            override_amount_cents (int | None | Unset):
            early_bird (bool | Unset):
     """

    name: None | str | Unset = UNSET
    override_amount_cents: int | None | Unset = UNSET
    early_bird: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        override_amount_cents: int | None | Unset
        if isinstance(self.override_amount_cents, Unset):
            override_amount_cents = UNSET
        else:
            override_amount_cents = self.override_amount_cents

        early_bird = self.early_bird


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if override_amount_cents is not UNSET:
            field_dict["override_amount_cents"] = override_amount_cents
        if early_bird is not UNSET:
            field_dict["early_bird"] = early_bird

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


        def _parse_override_amount_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        override_amount_cents = _parse_override_amount_cents(d.pop("override_amount_cents", UNSET))


        early_bird = d.pop("early_bird", UNSET)

        investment_delta_record_contracts_item = cls(
            name=name,
            override_amount_cents=override_amount_cents,
            early_bird=early_bird,
        )


        investment_delta_record_contracts_item.additional_properties = d
        return investment_delta_record_contracts_item

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
