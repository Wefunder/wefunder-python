from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="DebtSecurityTerms")



@_attrs_define
class DebtSecurityTerms:
    """ 
        Attributes:
            interest_rate_percent (None | str | Unset):  Example: 8.
            maturity_months (int | None | Unset):  Example: 36.
            first_payment_date (datetime.date | None | Unset):
     """

    interest_rate_percent: None | str | Unset = UNSET
    maturity_months: int | None | Unset = UNSET
    first_payment_date: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        interest_rate_percent: None | str | Unset
        if isinstance(self.interest_rate_percent, Unset):
            interest_rate_percent = UNSET
        else:
            interest_rate_percent = self.interest_rate_percent

        maturity_months: int | None | Unset
        if isinstance(self.maturity_months, Unset):
            maturity_months = UNSET
        else:
            maturity_months = self.maturity_months

        first_payment_date: None | str | Unset
        if isinstance(self.first_payment_date, Unset):
            first_payment_date = UNSET
        elif isinstance(self.first_payment_date, datetime.date):
            first_payment_date = self.first_payment_date.isoformat()
        else:
            first_payment_date = self.first_payment_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if interest_rate_percent is not UNSET:
            field_dict["interest_rate_percent"] = interest_rate_percent
        if maturity_months is not UNSET:
            field_dict["maturity_months"] = maturity_months
        if first_payment_date is not UNSET:
            field_dict["first_payment_date"] = first_payment_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_interest_rate_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        interest_rate_percent = _parse_interest_rate_percent(d.pop("interest_rate_percent", UNSET))


        def _parse_maturity_months(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        maturity_months = _parse_maturity_months(d.pop("maturity_months", UNSET))


        def _parse_first_payment_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_payment_date_type_0 = datetime.date.fromisoformat(data)



                return first_payment_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        first_payment_date = _parse_first_payment_date(d.pop("first_payment_date", UNSET))


        debt_security_terms = cls(
            interest_rate_percent=interest_rate_percent,
            maturity_months=maturity_months,
            first_payment_date=first_payment_date,
        )


        debt_security_terms.additional_properties = d
        return debt_security_terms

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
