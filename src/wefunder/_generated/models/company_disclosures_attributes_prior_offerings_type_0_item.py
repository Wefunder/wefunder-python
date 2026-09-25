from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompanyDisclosuresAttributesPriorOfferingsType0Item")


@_attrs_define
class CompanyDisclosuresAttributesPriorOfferingsType0Item:
    """
    Attributes:
        date (datetime.date | None | Unset):
        exemption (None | str | Unset):
        security_type (None | str | Unset):
        amount_sold (None | str | Unset):
        use_of_proceeds (None | str | Unset):
        offering_id (None | str | Unset): The Wefunder offering (`ofr_...`) when the prior offering ran here.
    """

    date: datetime.date | None | Unset = UNSET
    exemption: None | str | Unset = UNSET
    security_type: None | str | Unset = UNSET
    amount_sold: None | str | Unset = UNSET
    use_of_proceeds: None | str | Unset = UNSET
    offering_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.date):
            date = self.date.isoformat()
        else:
            date = self.date

        exemption: None | str | Unset
        if isinstance(self.exemption, Unset):
            exemption = UNSET
        else:
            exemption = self.exemption

        security_type: None | str | Unset
        if isinstance(self.security_type, Unset):
            security_type = UNSET
        else:
            security_type = self.security_type

        amount_sold: None | str | Unset
        if isinstance(self.amount_sold, Unset):
            amount_sold = UNSET
        else:
            amount_sold = self.amount_sold

        use_of_proceeds: None | str | Unset
        if isinstance(self.use_of_proceeds, Unset):
            use_of_proceeds = UNSET
        else:
            use_of_proceeds = self.use_of_proceeds

        offering_id: None | str | Unset
        if isinstance(self.offering_id, Unset):
            offering_id = UNSET
        else:
            offering_id = self.offering_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if exemption is not UNSET:
            field_dict["exemption"] = exemption
        if security_type is not UNSET:
            field_dict["security_type"] = security_type
        if amount_sold is not UNSET:
            field_dict["amount_sold"] = amount_sold
        if use_of_proceeds is not UNSET:
            field_dict["use_of_proceeds"] = use_of_proceeds
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

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

        def _parse_exemption(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exemption = _parse_exemption(d.pop("exemption", UNSET))

        def _parse_security_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        security_type = _parse_security_type(d.pop("security_type", UNSET))

        def _parse_amount_sold(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        amount_sold = _parse_amount_sold(d.pop("amount_sold", UNSET))

        def _parse_use_of_proceeds(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        use_of_proceeds = _parse_use_of_proceeds(d.pop("use_of_proceeds", UNSET))

        def _parse_offering_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        offering_id = _parse_offering_id(d.pop("offering_id", UNSET))

        company_disclosures_attributes_prior_offerings_type_0_item = cls(
            date=date,
            exemption=exemption,
            security_type=security_type,
            amount_sold=amount_sold,
            use_of_proceeds=use_of_proceeds,
            offering_id=offering_id,
        )

        company_disclosures_attributes_prior_offerings_type_0_item.additional_properties = d
        return company_disclosures_attributes_prior_offerings_type_0_item

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
