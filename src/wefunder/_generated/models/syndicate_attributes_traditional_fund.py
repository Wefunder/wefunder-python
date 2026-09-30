from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SyndicateAttributesTraditionalFund")


@_attrs_define
class SyndicateAttributesTraditionalFund:
    """Present only when `syndicate_type` is `traditional_fund`.

    Attributes:
        require_minimum_investment (bool | Unset):
        minimum_investment_amount (None | str | Unset):
    """

    require_minimum_investment: bool | Unset = UNSET
    minimum_investment_amount: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        require_minimum_investment = self.require_minimum_investment

        minimum_investment_amount: None | str | Unset
        if isinstance(self.minimum_investment_amount, Unset):
            minimum_investment_amount = UNSET
        else:
            minimum_investment_amount = self.minimum_investment_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if require_minimum_investment is not UNSET:
            field_dict["require_minimum_investment"] = require_minimum_investment
        if minimum_investment_amount is not UNSET:
            field_dict["minimum_investment_amount"] = minimum_investment_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        require_minimum_investment = d.pop("require_minimum_investment", UNSET)

        def _parse_minimum_investment_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        minimum_investment_amount = _parse_minimum_investment_amount(d.pop("minimum_investment_amount", UNSET))

        syndicate_attributes_traditional_fund = cls(
            require_minimum_investment=require_minimum_investment,
            minimum_investment_amount=minimum_investment_amount,
        )

        syndicate_attributes_traditional_fund.additional_properties = d
        return syndicate_attributes_traditional_fund

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
