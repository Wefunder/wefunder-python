from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spv_terms_safe_type import SpvTermsSafeType
from ..models.spv_terms_structure import SpvTermsStructure
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpvTerms")


@_attrs_define
class SpvTerms:
    """Investment terms for an SPV.

    Attributes:
        structure (SpvTermsStructure):  Example: safe.
        valuation_cap_cents (int):  Example: 1000000000.
        minimum_investment_cents (int):  Example: 1000000.
        target_raise_cents (int):  Example: 100000000.
        safe_type (SpvTermsSafeType | Unset): Required when `structure` is `safe`. Example: post_money.
        discount_percent (int | None | Unset): Discount percentage (e.g. 20 for 20%).
        max_raise_cents (int | None | Unset):  Example: 200000000.
    """

    structure: SpvTermsStructure
    valuation_cap_cents: int
    minimum_investment_cents: int
    target_raise_cents: int
    safe_type: SpvTermsSafeType | Unset = UNSET
    discount_percent: int | None | Unset = UNSET
    max_raise_cents: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        structure = self.structure.value

        valuation_cap_cents = self.valuation_cap_cents

        minimum_investment_cents = self.minimum_investment_cents

        target_raise_cents = self.target_raise_cents

        safe_type: str | Unset = UNSET
        if not isinstance(self.safe_type, Unset):
            safe_type = self.safe_type.value

        discount_percent: int | None | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        max_raise_cents: int | None | Unset
        if isinstance(self.max_raise_cents, Unset):
            max_raise_cents = UNSET
        else:
            max_raise_cents = self.max_raise_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "structure": structure,
                "valuation_cap_cents": valuation_cap_cents,
                "minimum_investment_cents": minimum_investment_cents,
                "target_raise_cents": target_raise_cents,
            }
        )
        if safe_type is not UNSET:
            field_dict["safe_type"] = safe_type
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if max_raise_cents is not UNSET:
            field_dict["max_raise_cents"] = max_raise_cents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        structure = SpvTermsStructure(d.pop("structure"))

        valuation_cap_cents = d.pop("valuation_cap_cents")

        minimum_investment_cents = d.pop("minimum_investment_cents")

        target_raise_cents = d.pop("target_raise_cents")

        _safe_type = d.pop("safe_type", UNSET)
        safe_type: SpvTermsSafeType | Unset
        if isinstance(_safe_type, Unset):
            safe_type = UNSET
        else:
            safe_type = SpvTermsSafeType(_safe_type)

        def _parse_discount_percent(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discount_percent", UNSET))

        def _parse_max_raise_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_raise_cents = _parse_max_raise_cents(d.pop("max_raise_cents", UNSET))

        spv_terms = cls(
            structure=structure,
            valuation_cap_cents=valuation_cap_cents,
            minimum_investment_cents=minimum_investment_cents,
            target_raise_cents=target_raise_cents,
            safe_type=safe_type,
            discount_percent=discount_percent,
            max_raise_cents=max_raise_cents,
        )

        spv_terms.additional_properties = d
        return spv_terms

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
