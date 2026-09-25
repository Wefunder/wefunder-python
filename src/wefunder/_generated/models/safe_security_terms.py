from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SafeSecurityTerms")



@_attrs_define
class SafeSecurityTerms:
    """ 
        Attributes:
            valuation_cap (None | str | Unset): Post-money valuation cap in USD, decimal string; null for an uncapped SAFE
                (never "0"). Example: 10000000.
            uncapped (bool | Unset): True when the SAFE has no valuation cap, as the deal page labels it. Always the inverse
                of `valuation_cap` being present.
            discount_percent (None | str | Unset): Discount to the next priced round, as a percentage; null when none.
                Example: 20.
            most_favored_nation (bool | Unset): Whether the SAFE carries an MFN clause.
            pro_rata (bool | Unset): Whether investors receive pro-rata rights in the next round.
     """

    valuation_cap: None | str | Unset = UNSET
    uncapped: bool | Unset = UNSET
    discount_percent: None | str | Unset = UNSET
    most_favored_nation: bool | Unset = UNSET
    pro_rata: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        valuation_cap: None | str | Unset
        if isinstance(self.valuation_cap, Unset):
            valuation_cap = UNSET
        else:
            valuation_cap = self.valuation_cap

        uncapped = self.uncapped

        discount_percent: None | str | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        most_favored_nation = self.most_favored_nation

        pro_rata = self.pro_rata


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if valuation_cap is not UNSET:
            field_dict["valuation_cap"] = valuation_cap
        if uncapped is not UNSET:
            field_dict["uncapped"] = uncapped
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if most_favored_nation is not UNSET:
            field_dict["most_favored_nation"] = most_favored_nation
        if pro_rata is not UNSET:
            field_dict["pro_rata"] = pro_rata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_valuation_cap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        valuation_cap = _parse_valuation_cap(d.pop("valuation_cap", UNSET))


        uncapped = d.pop("uncapped", UNSET)

        def _parse_discount_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discount_percent", UNSET))


        most_favored_nation = d.pop("most_favored_nation", UNSET)

        pro_rata = d.pop("pro_rata", UNSET)

        safe_security_terms = cls(
            valuation_cap=valuation_cap,
            uncapped=uncapped,
            discount_percent=discount_percent,
            most_favored_nation=most_favored_nation,
            pro_rata=pro_rata,
        )


        safe_security_terms.additional_properties = d
        return safe_security_terms

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
