from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CompanyDisclosuresAttributesOutstandingNotesType0Item")



@_attrs_define
class CompanyDisclosuresAttributesOutstandingNotesType0Item:
    """ 
        Attributes:
            amount (None | str | Unset):
            outstanding_principal (None | str | Unset):
            valuation_cap (None | str | Unset):
            uncapped (bool | Unset):
            interest_rate_percent (None | str | Unset):
            discount_percent (None | str | Unset):
            maturity_date (datetime.date | None | Unset):
            description (None | str | Unset):
     """

    amount: None | str | Unset = UNSET
    outstanding_principal: None | str | Unset = UNSET
    valuation_cap: None | str | Unset = UNSET
    uncapped: bool | Unset = UNSET
    interest_rate_percent: None | str | Unset = UNSET
    discount_percent: None | str | Unset = UNSET
    maturity_date: datetime.date | None | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        outstanding_principal: None | str | Unset
        if isinstance(self.outstanding_principal, Unset):
            outstanding_principal = UNSET
        else:
            outstanding_principal = self.outstanding_principal

        valuation_cap: None | str | Unset
        if isinstance(self.valuation_cap, Unset):
            valuation_cap = UNSET
        else:
            valuation_cap = self.valuation_cap

        uncapped = self.uncapped

        interest_rate_percent: None | str | Unset
        if isinstance(self.interest_rate_percent, Unset):
            interest_rate_percent = UNSET
        else:
            interest_rate_percent = self.interest_rate_percent

        discount_percent: None | str | Unset
        if isinstance(self.discount_percent, Unset):
            discount_percent = UNSET
        else:
            discount_percent = self.discount_percent

        maturity_date: None | str | Unset
        if isinstance(self.maturity_date, Unset):
            maturity_date = UNSET
        elif isinstance(self.maturity_date, datetime.date):
            maturity_date = self.maturity_date.isoformat()
        else:
            maturity_date = self.maturity_date

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount is not UNSET:
            field_dict["amount"] = amount
        if outstanding_principal is not UNSET:
            field_dict["outstanding_principal"] = outstanding_principal
        if valuation_cap is not UNSET:
            field_dict["valuation_cap"] = valuation_cap
        if uncapped is not UNSET:
            field_dict["uncapped"] = uncapped
        if interest_rate_percent is not UNSET:
            field_dict["interest_rate_percent"] = interest_rate_percent
        if discount_percent is not UNSET:
            field_dict["discount_percent"] = discount_percent
        if maturity_date is not UNSET:
            field_dict["maturity_date"] = maturity_date
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_outstanding_principal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outstanding_principal = _parse_outstanding_principal(d.pop("outstanding_principal", UNSET))


        def _parse_valuation_cap(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        valuation_cap = _parse_valuation_cap(d.pop("valuation_cap", UNSET))


        uncapped = d.pop("uncapped", UNSET)

        def _parse_interest_rate_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interest_rate_percent = _parse_interest_rate_percent(d.pop("interest_rate_percent", UNSET))


        def _parse_discount_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        discount_percent = _parse_discount_percent(d.pop("discount_percent", UNSET))


        def _parse_maturity_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maturity_date_type_0 = datetime.date.fromisoformat(data)



                return maturity_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        maturity_date = _parse_maturity_date(d.pop("maturity_date", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        company_disclosures_attributes_outstanding_notes_type_0_item = cls(
            amount=amount,
            outstanding_principal=outstanding_principal,
            valuation_cap=valuation_cap,
            uncapped=uncapped,
            interest_rate_percent=interest_rate_percent,
            discount_percent=discount_percent,
            maturity_date=maturity_date,
            description=description,
        )


        company_disclosures_attributes_outstanding_notes_type_0_item.additional_properties = d
        return company_disclosures_attributes_outstanding_notes_type_0_item

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
