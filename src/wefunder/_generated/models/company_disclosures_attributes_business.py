from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CompanyDisclosuresAttributesBusiness")



@_attrs_define
class CompanyDisclosuresAttributesBusiness:
    """ 
        Attributes:
            legal_name (None | str | Unset):
            legal_form (None | str | Unset):
            jurisdiction (None | str | Unset):
            incorporated_on (datetime.date | None | Unset):
            employees (int | None | Unset):
     """

    legal_name: None | str | Unset = UNSET
    legal_form: None | str | Unset = UNSET
    jurisdiction: None | str | Unset = UNSET
    incorporated_on: datetime.date | None | Unset = UNSET
    employees: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        legal_name: None | str | Unset
        if isinstance(self.legal_name, Unset):
            legal_name = UNSET
        else:
            legal_name = self.legal_name

        legal_form: None | str | Unset
        if isinstance(self.legal_form, Unset):
            legal_form = UNSET
        else:
            legal_form = self.legal_form

        jurisdiction: None | str | Unset
        if isinstance(self.jurisdiction, Unset):
            jurisdiction = UNSET
        else:
            jurisdiction = self.jurisdiction

        incorporated_on: None | str | Unset
        if isinstance(self.incorporated_on, Unset):
            incorporated_on = UNSET
        elif isinstance(self.incorporated_on, datetime.date):
            incorporated_on = self.incorporated_on.isoformat()
        else:
            incorporated_on = self.incorporated_on

        employees: int | None | Unset
        if isinstance(self.employees, Unset):
            employees = UNSET
        else:
            employees = self.employees


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if legal_form is not UNSET:
            field_dict["legal_form"] = legal_form
        if jurisdiction is not UNSET:
            field_dict["jurisdiction"] = jurisdiction
        if incorporated_on is not UNSET:
            field_dict["incorporated_on"] = incorporated_on
        if employees is not UNSET:
            field_dict["employees"] = employees

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_legal_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_name = _parse_legal_name(d.pop("legal_name", UNSET))


        def _parse_legal_form(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        legal_form = _parse_legal_form(d.pop("legal_form", UNSET))


        def _parse_jurisdiction(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        jurisdiction = _parse_jurisdiction(d.pop("jurisdiction", UNSET))


        def _parse_incorporated_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                incorporated_on_type_0 = datetime.date.fromisoformat(data)



                return incorporated_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        incorporated_on = _parse_incorporated_on(d.pop("incorporated_on", UNSET))


        def _parse_employees(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        employees = _parse_employees(d.pop("employees", UNSET))


        company_disclosures_attributes_business = cls(
            legal_name=legal_name,
            legal_form=legal_form,
            jurisdiction=jurisdiction,
            incorporated_on=incorporated_on,
            employees=employees,
        )


        company_disclosures_attributes_business.additional_properties = d
        return company_disclosures_attributes_business

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
