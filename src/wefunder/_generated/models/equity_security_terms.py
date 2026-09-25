from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.equity_security_terms_share_class_type_1 import EquitySecurityTermsShareClassType1
from ..models.equity_security_terms_share_class_type_2_type_1 import EquitySecurityTermsShareClassType2Type1
from ..models.equity_security_terms_share_class_type_3_type_1 import EquitySecurityTermsShareClassType3Type1
from ..types import UNSET, Unset

T = TypeVar("T", bound="EquitySecurityTerms")


@_attrs_define
class EquitySecurityTerms:
    """
    Attributes:
        share_price (None | str | Unset): Price per share in USD, decimal string. Example: 2.5.
        pre_money_valuation (None | str | Unset): Pre-money valuation in USD, decimal string. Example: 15000000.
        share_class (EquitySecurityTermsShareClassType1 | EquitySecurityTermsShareClassType2Type1 |
            EquitySecurityTermsShareClassType3Type1 | None | Unset):  Example: preferred.
    """

    share_price: None | str | Unset = UNSET
    pre_money_valuation: None | str | Unset = UNSET
    share_class: (
        EquitySecurityTermsShareClassType1
        | EquitySecurityTermsShareClassType2Type1
        | EquitySecurityTermsShareClassType3Type1
        | None
        | Unset
    ) = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        share_price: None | str | Unset
        if isinstance(self.share_price, Unset):
            share_price = UNSET
        else:
            share_price = self.share_price

        pre_money_valuation: None | str | Unset
        if isinstance(self.pre_money_valuation, Unset):
            pre_money_valuation = UNSET
        else:
            pre_money_valuation = self.pre_money_valuation

        share_class: None | str | Unset
        if isinstance(self.share_class, Unset):
            share_class = UNSET
        elif (
            isinstance(self.share_class, EquitySecurityTermsShareClassType1)
            or isinstance(self.share_class, EquitySecurityTermsShareClassType2Type1)
            or isinstance(self.share_class, EquitySecurityTermsShareClassType3Type1)
        ):
            share_class = self.share_class.value
        else:
            share_class = self.share_class

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if share_price is not UNSET:
            field_dict["share_price"] = share_price
        if pre_money_valuation is not UNSET:
            field_dict["pre_money_valuation"] = pre_money_valuation
        if share_class is not UNSET:
            field_dict["share_class"] = share_class

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_share_price(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        share_price = _parse_share_price(d.pop("share_price", UNSET))

        def _parse_pre_money_valuation(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        pre_money_valuation = _parse_pre_money_valuation(d.pop("pre_money_valuation", UNSET))

        def _parse_share_class(
            data: object,
        ) -> (
            EquitySecurityTermsShareClassType1
            | EquitySecurityTermsShareClassType2Type1
            | EquitySecurityTermsShareClassType3Type1
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_class_type_1 = EquitySecurityTermsShareClassType1(data)

                return share_class_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_class_type_2_type_1 = EquitySecurityTermsShareClassType2Type1(data)

                return share_class_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                share_class_type_3_type_1 = EquitySecurityTermsShareClassType3Type1(data)

                return share_class_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                EquitySecurityTermsShareClassType1
                | EquitySecurityTermsShareClassType2Type1
                | EquitySecurityTermsShareClassType3Type1
                | None
                | Unset,
                data,
            )

        share_class = _parse_share_class(d.pop("share_class", UNSET))

        equity_security_terms = cls(
            share_price=share_price,
            pre_money_valuation=pre_money_valuation,
            share_class=share_class,
        )

        equity_security_terms.additional_properties = d
        return equity_security_terms

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
