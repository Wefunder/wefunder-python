from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="CompanyDisclosuresAttributesRelatedPartiesType0PartiesItem")



@_attrs_define
class CompanyDisclosuresAttributesRelatedPartiesType0PartiesItem:
    """ 
        Attributes:
            name (None | str | Unset):
            relationship (None | str | Unset):
            amount (None | str | Unset):
            date (datetime.date | None | Unset):
            outstanding_principal (None | str | Unset):
            description (None | str | Unset):
     """

    name: None | str | Unset = UNSET
    relationship: None | str | Unset = UNSET
    amount: None | str | Unset = UNSET
    date: datetime.date | None | Unset = UNSET
    outstanding_principal: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        relationship: None | str | Unset
        if isinstance(self.relationship, Unset):
            relationship = UNSET
        else:
            relationship = self.relationship

        amount: None | str | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        outstanding_principal: None | str | Unset
        if isinstance(self.outstanding_principal, Unset):
            outstanding_principal = UNSET
        else:
            outstanding_principal = self.outstanding_principal

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date is not UNSET:
            field_dict["date"] = date
        if outstanding_principal is not UNSET:
            field_dict["outstanding_principal"] = outstanding_principal
        if description is not UNSET:
            field_dict["description"] = description

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


        def _parse_relationship(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        relationship = _parse_relationship(d.pop("relationship", UNSET))


        def _parse_amount(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        def _parse_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = datetime.date.fromisoformat(data)



                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))


        def _parse_outstanding_principal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        outstanding_principal = _parse_outstanding_principal(d.pop("outstanding_principal", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        company_disclosures_attributes_related_parties_type_0_parties_item = cls(
            name=name,
            relationship=relationship,
            amount=amount,
            date=date,
            outstanding_principal=outstanding_principal,
            description=description,
        )


        company_disclosures_attributes_related_parties_type_0_parties_item.additional_properties = d
        return company_disclosures_attributes_related_parties_type_0_parties_item

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
