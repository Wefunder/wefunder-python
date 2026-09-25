from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_partner_invite_body_direction import CreatePartnerInviteBodyDirection
from ..types import UNSET, Unset






T = TypeVar("T", bound="CreatePartnerInviteBody")



@_attrs_define
class CreatePartnerInviteBody:
    """ 
        Attributes:
            direction (CreatePartnerInviteBodyDirection):
            company_id (int | Unset): Required for founder_to_partner direction
            partner_email (str | Unset): Required for founder_to_partner direction
            access_level (int | Unset): 1=anonymized (default), 2=detailed (future) Default: 1.
     """

    direction: CreatePartnerInviteBodyDirection
    company_id: int | Unset = UNSET
    partner_email: str | Unset = UNSET
    access_level: int | Unset = 1
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        direction = self.direction.value

        company_id = self.company_id

        partner_email = self.partner_email

        access_level = self.access_level


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "direction": direction,
        })
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if partner_email is not UNSET:
            field_dict["partner_email"] = partner_email
        if access_level is not UNSET:
            field_dict["access_level"] = access_level

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direction = CreatePartnerInviteBodyDirection(d.pop("direction"))




        company_id = d.pop("company_id", UNSET)

        partner_email = d.pop("partner_email", UNSET)

        access_level = d.pop("access_level", UNSET)

        create_partner_invite_body = cls(
            direction=direction,
            company_id=company_id,
            partner_email=partner_email,
            access_level=access_level,
        )


        create_partner_invite_body.additional_properties = d
        return create_partner_invite_body

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
