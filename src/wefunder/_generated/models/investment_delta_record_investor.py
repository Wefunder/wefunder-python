from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.investment_delta_record_investor_address import InvestmentDeltaRecordInvestorAddress





T = TypeVar("T", bound="InvestmentDeltaRecordInvestor")



@_attrs_define
class InvestmentDeltaRecordInvestor:
    """ 
        Attributes:
            id (str | Unset): Investor external id (`usr_…`).
            deactivated (bool | Unset): True once the investor's Wefunder account has been deactivated. The identity fields
                are then
                redacted (`name`/`legal_name` = `[deleted user]`, the rest null) and the record is republished
                with `reason: investor_deactivated`; overwrite your copy. The investment itself persists.
            via_entity (bool | Unset):
            name (str | Unset): PII scope.
            legal_name (str | Unset): PII scope.
            email (None | str | Unset): PII scope.
            address (InvestmentDeltaRecordInvestorAddress | Unset): PII scope.
            bio (None | str | Unset): PII scope.
     """

    id: str | Unset = UNSET
    deactivated: bool | Unset = UNSET
    via_entity: bool | Unset = UNSET
    name: str | Unset = UNSET
    legal_name: str | Unset = UNSET
    email: None | str | Unset = UNSET
    address: InvestmentDeltaRecordInvestorAddress | Unset = UNSET
    bio: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.investment_delta_record_investor_address import InvestmentDeltaRecordInvestorAddress # noqa: PLC0415
        id = self.id

        deactivated = self.deactivated

        via_entity = self.via_entity

        name = self.name

        legal_name = self.legal_name

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        bio: None | str | Unset
        if isinstance(self.bio, Unset):
            bio = UNSET
        else:
            bio = self.bio


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if deactivated is not UNSET:
            field_dict["deactivated"] = deactivated
        if via_entity is not UNSET:
            field_dict["via_entity"] = via_entity
        if name is not UNSET:
            field_dict["name"] = name
        if legal_name is not UNSET:
            field_dict["legal_name"] = legal_name
        if email is not UNSET:
            field_dict["email"] = email
        if address is not UNSET:
            field_dict["address"] = address
        if bio is not UNSET:
            field_dict["bio"] = bio

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.investment_delta_record_investor_address import InvestmentDeltaRecordInvestorAddress # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        deactivated = d.pop("deactivated", UNSET)

        via_entity = d.pop("via_entity", UNSET)

        name = d.pop("name", UNSET)

        legal_name = d.pop("legal_name", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        _address = d.pop("address", UNSET)
        address: InvestmentDeltaRecordInvestorAddress | Unset
        if isinstance(_address,  Unset):
            address = UNSET
        else:
            address = InvestmentDeltaRecordInvestorAddress.from_dict(_address)




        def _parse_bio(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bio = _parse_bio(d.pop("bio", UNSET))


        investment_delta_record_investor = cls(
            id=id,
            deactivated=deactivated,
            via_entity=via_entity,
            name=name,
            legal_name=legal_name,
            email=email,
            address=address,
            bio=bio,
        )


        investment_delta_record_investor.additional_properties = d
        return investment_delta_record_investor

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
