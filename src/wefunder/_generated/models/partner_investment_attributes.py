from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.partner_investment_attributes_status import PartnerInvestmentAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.partner_investment_attributes_accreditation_type_0 import PartnerInvestmentAttributesAccreditationType0





T = TypeVar("T", bound="PartnerInvestmentAttributes")



@_attrs_define
class PartnerInvestmentAttributes:
    """ 
        Attributes:
            amount_cents (int | Unset):  Example: 2500000.
            status (PartnerInvestmentAttributesStatus | Unset):  Example: confirmed.
            spv_id (str | Unset):  Example: spv_abc123.
            investor_id (None | str | Unset):  Example: investor_usr456.
            accreditation (None | PartnerInvestmentAttributesAccreditationType0 | Unset):
            confirmed_at (datetime.datetime | None | Unset):
            created_at (datetime.datetime | Unset):  Example: 2025-01-15T10:00:00Z.
     """

    amount_cents: int | Unset = UNSET
    status: PartnerInvestmentAttributesStatus | Unset = UNSET
    spv_id: str | Unset = UNSET
    investor_id: None | str | Unset = UNSET
    accreditation: None | PartnerInvestmentAttributesAccreditationType0 | Unset = UNSET
    confirmed_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_investment_attributes_accreditation_type_0 import PartnerInvestmentAttributesAccreditationType0 # noqa: PLC0415
        amount_cents = self.amount_cents

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        spv_id = self.spv_id

        investor_id: None | str | Unset
        if isinstance(self.investor_id, Unset):
            investor_id = UNSET
        else:
            investor_id = self.investor_id

        accreditation: dict[str, Any] | None | Unset
        if isinstance(self.accreditation, Unset):
            accreditation = UNSET
        elif isinstance(self.accreditation, PartnerInvestmentAttributesAccreditationType0):
            accreditation = self.accreditation.to_dict()
        else:
            accreditation = self.accreditation

        confirmed_at: None | str | Unset
        if isinstance(self.confirmed_at, Unset):
            confirmed_at = UNSET
        elif isinstance(self.confirmed_at, datetime.datetime):
            confirmed_at = self.confirmed_at.isoformat()
        else:
            confirmed_at = self.confirmed_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if amount_cents is not UNSET:
            field_dict["amount_cents"] = amount_cents
        if status is not UNSET:
            field_dict["status"] = status
        if spv_id is not UNSET:
            field_dict["spv_id"] = spv_id
        if investor_id is not UNSET:
            field_dict["investor_id"] = investor_id
        if accreditation is not UNSET:
            field_dict["accreditation"] = accreditation
        if confirmed_at is not UNSET:
            field_dict["confirmed_at"] = confirmed_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_investment_attributes_accreditation_type_0 import PartnerInvestmentAttributesAccreditationType0 # noqa: PLC0415
        d = dict(src_dict)
        amount_cents = d.pop("amount_cents", UNSET)

        _status = d.pop("status", UNSET)
        status: PartnerInvestmentAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = PartnerInvestmentAttributesStatus(_status)




        spv_id = d.pop("spv_id", UNSET)

        def _parse_investor_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investor_id = _parse_investor_id(d.pop("investor_id", UNSET))


        def _parse_accreditation(data: object) -> None | PartnerInvestmentAttributesAccreditationType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                accreditation_type_0 = PartnerInvestmentAttributesAccreditationType0.from_dict(data)



                return accreditation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PartnerInvestmentAttributesAccreditationType0 | Unset, data)

        accreditation = _parse_accreditation(d.pop("accreditation", UNSET))


        def _parse_confirmed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                confirmed_at_type_0 = datetime.datetime.fromisoformat(data)



                return confirmed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        confirmed_at = _parse_confirmed_at(d.pop("confirmed_at", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        partner_investment_attributes = cls(
            amount_cents=amount_cents,
            status=status,
            spv_id=spv_id,
            investor_id=investor_id,
            accreditation=accreditation,
            confirmed_at=confirmed_at,
            created_at=created_at,
        )


        partner_investment_attributes.additional_properties = d
        return partner_investment_attributes

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
