from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.partner_investment_attributes_accreditation_type_0_status import PartnerInvestmentAttributesAccreditationType0Status
from ..models.partner_investment_attributes_accreditation_type_0_type import PartnerInvestmentAttributesAccreditationType0Type
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="PartnerInvestmentAttributesAccreditationType0")



@_attrs_define
class PartnerInvestmentAttributesAccreditationType0:
    """ 
        Attributes:
            type_ (PartnerInvestmentAttributesAccreditationType0Type | Unset):  Example: verified.
            status (PartnerInvestmentAttributesAccreditationType0Status | Unset):  Example: pending.
            basis (None | str | Unset):  Example: income.
            submitted_at (datetime.datetime | None | Unset):
     """

    type_: PartnerInvestmentAttributesAccreditationType0Type | Unset = UNSET
    status: PartnerInvestmentAttributesAccreditationType0Status | Unset = UNSET
    basis: None | str | Unset = UNSET
    submitted_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        basis: None | str | Unset
        if isinstance(self.basis, Unset):
            basis = UNSET
        else:
            basis = self.basis

        submitted_at: None | str | Unset
        if isinstance(self.submitted_at, Unset):
            submitted_at = UNSET
        elif isinstance(self.submitted_at, datetime.datetime):
            submitted_at = self.submitted_at.isoformat()
        else:
            submitted_at = self.submitted_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if basis is not UNSET:
            field_dict["basis"] = basis
        if submitted_at is not UNSET:
            field_dict["submitted_at"] = submitted_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PartnerInvestmentAttributesAccreditationType0Type | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PartnerInvestmentAttributesAccreditationType0Type(_type_)




        _status = d.pop("status", UNSET)
        status: PartnerInvestmentAttributesAccreditationType0Status | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PartnerInvestmentAttributesAccreditationType0Status(_status)




        def _parse_basis(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        basis = _parse_basis(d.pop("basis", UNSET))


        def _parse_submitted_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                submitted_at_type_0 = datetime.datetime.fromisoformat(data)



                return submitted_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        submitted_at = _parse_submitted_at(d.pop("submitted_at", UNSET))


        partner_investment_attributes_accreditation_type_0 = cls(
            type_=type_,
            status=status,
            basis=basis,
            submitted_at=submitted_at,
        )


        partner_investment_attributes_accreditation_type_0.additional_properties = d
        return partner_investment_attributes_accreditation_type_0

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
