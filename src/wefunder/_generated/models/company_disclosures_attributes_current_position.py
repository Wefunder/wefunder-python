from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CompanyDisclosuresAttributesCurrentPosition")



@_attrs_define
class CompanyDisclosuresAttributesCurrentPosition:
    """ The founder's own disclosure of where the company stands today, each field when supplied.

        Attributes:
            cash_on_hand (None | str | Unset): USD, decimal string.
            cash_on_hand_as_of (datetime.date | None | Unset):
            average_monthly_revenue (None | str | Unset): USD, decimal string.
            average_monthly_cost_of_goods (None | str | Unset): USD, decimal string.
            average_monthly_expenses (None | str | Unset): USD, decimal string.
            average_monthly_burn (None | str | Unset): USD, decimal string.
     """

    cash_on_hand: None | str | Unset = UNSET
    cash_on_hand_as_of: datetime.date | None | Unset = UNSET
    average_monthly_revenue: None | str | Unset = UNSET
    average_monthly_cost_of_goods: None | str | Unset = UNSET
    average_monthly_expenses: None | str | Unset = UNSET
    average_monthly_burn: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        cash_on_hand: None | str | Unset
        if isinstance(self.cash_on_hand, Unset):
            cash_on_hand = UNSET
        else:
            cash_on_hand = self.cash_on_hand

        cash_on_hand_as_of: None | str | Unset
        if isinstance(self.cash_on_hand_as_of, Unset):
            cash_on_hand_as_of = UNSET
        elif isinstance(self.cash_on_hand_as_of, datetime.date):
            cash_on_hand_as_of = self.cash_on_hand_as_of.isoformat()
        else:
            cash_on_hand_as_of = self.cash_on_hand_as_of

        average_monthly_revenue: None | str | Unset
        if isinstance(self.average_monthly_revenue, Unset):
            average_monthly_revenue = UNSET
        else:
            average_monthly_revenue = self.average_monthly_revenue

        average_monthly_cost_of_goods: None | str | Unset
        if isinstance(self.average_monthly_cost_of_goods, Unset):
            average_monthly_cost_of_goods = UNSET
        else:
            average_monthly_cost_of_goods = self.average_monthly_cost_of_goods

        average_monthly_expenses: None | str | Unset
        if isinstance(self.average_monthly_expenses, Unset):
            average_monthly_expenses = UNSET
        else:
            average_monthly_expenses = self.average_monthly_expenses

        average_monthly_burn: None | str | Unset
        if isinstance(self.average_monthly_burn, Unset):
            average_monthly_burn = UNSET
        else:
            average_monthly_burn = self.average_monthly_burn


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cash_on_hand is not UNSET:
            field_dict["cash_on_hand"] = cash_on_hand
        if cash_on_hand_as_of is not UNSET:
            field_dict["cash_on_hand_as_of"] = cash_on_hand_as_of
        if average_monthly_revenue is not UNSET:
            field_dict["average_monthly_revenue"] = average_monthly_revenue
        if average_monthly_cost_of_goods is not UNSET:
            field_dict["average_monthly_cost_of_goods"] = average_monthly_cost_of_goods
        if average_monthly_expenses is not UNSET:
            field_dict["average_monthly_expenses"] = average_monthly_expenses
        if average_monthly_burn is not UNSET:
            field_dict["average_monthly_burn"] = average_monthly_burn

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_cash_on_hand(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cash_on_hand = _parse_cash_on_hand(d.pop("cash_on_hand", UNSET))


        def _parse_cash_on_hand_as_of(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cash_on_hand_as_of_type_0 = datetime.date.fromisoformat(data)



                return cash_on_hand_as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        cash_on_hand_as_of = _parse_cash_on_hand_as_of(d.pop("cash_on_hand_as_of", UNSET))


        def _parse_average_monthly_revenue(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average_monthly_revenue = _parse_average_monthly_revenue(d.pop("average_monthly_revenue", UNSET))


        def _parse_average_monthly_cost_of_goods(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average_monthly_cost_of_goods = _parse_average_monthly_cost_of_goods(d.pop("average_monthly_cost_of_goods", UNSET))


        def _parse_average_monthly_expenses(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average_monthly_expenses = _parse_average_monthly_expenses(d.pop("average_monthly_expenses", UNSET))


        def _parse_average_monthly_burn(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        average_monthly_burn = _parse_average_monthly_burn(d.pop("average_monthly_burn", UNSET))


        company_disclosures_attributes_current_position = cls(
            cash_on_hand=cash_on_hand,
            cash_on_hand_as_of=cash_on_hand_as_of,
            average_monthly_revenue=average_monthly_revenue,
            average_monthly_cost_of_goods=average_monthly_cost_of_goods,
            average_monthly_expenses=average_monthly_expenses,
            average_monthly_burn=average_monthly_burn,
        )


        company_disclosures_attributes_current_position.additional_properties = d
        return company_disclosures_attributes_current_position

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
