from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem")



@_attrs_define
class CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem:
    """ 
        Attributes:
            original_amount (None | str | Unset):
            outstanding_principal (None | str | Unset):
            current_with_payments (bool | None | Unset):
            maturity_date (datetime.date | None | Unset):
            description (None | str | Unset):
     """

    original_amount: None | str | Unset = UNSET
    outstanding_principal: None | str | Unset = UNSET
    current_with_payments: bool | None | Unset = UNSET
    maturity_date: datetime.date | None | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        original_amount: None | str | Unset
        if isinstance(self.original_amount, Unset):
            original_amount = UNSET
        else:
            original_amount = self.original_amount

        outstanding_principal: None | str | Unset
        if isinstance(self.outstanding_principal, Unset):
            outstanding_principal = UNSET
        else:
            outstanding_principal = self.outstanding_principal

        current_with_payments: bool | None | Unset
        if isinstance(self.current_with_payments, Unset):
            current_with_payments = UNSET
        else:
            current_with_payments = self.current_with_payments

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
        if original_amount is not UNSET:
            field_dict["original_amount"] = original_amount
        if outstanding_principal is not UNSET:
            field_dict["outstanding_principal"] = outstanding_principal
        if current_with_payments is not UNSET:
            field_dict["current_with_payments"] = current_with_payments
        if maturity_date is not UNSET:
            field_dict["maturity_date"] = maturity_date
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_original_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        original_amount = _parse_original_amount(d.pop("original_amount", UNSET))


        def _parse_outstanding_principal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outstanding_principal = _parse_outstanding_principal(d.pop("outstanding_principal", UNSET))


        def _parse_current_with_payments(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        current_with_payments = _parse_current_with_payments(d.pop("current_with_payments", UNSET))


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


        company_disclosures_attributes_outstanding_debts_type_0_items_item = cls(
            original_amount=original_amount,
            outstanding_principal=outstanding_principal,
            current_with_payments=current_with_payments,
            maturity_date=maturity_date,
            description=description,
        )


        company_disclosures_attributes_outstanding_debts_type_0_items_item.additional_properties = d
        return company_disclosures_attributes_outstanding_debts_type_0_items_item

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
