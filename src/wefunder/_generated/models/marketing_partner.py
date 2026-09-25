from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.marketing_partner_status import MarketingPartnerStatus
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="MarketingPartner")



@_attrs_define
class MarketingPartner:
    """ A registered marketing partner

        Attributes:
            id (int | Unset):  Example: 123.
            user_id (int | Unset):  Example: 456.
            company_name (str | Unset):  Example: Acme Marketing Agency.
            website (None | str | Unset):  Example: https://acme-marketing.com.
            status (MarketingPartnerStatus | Unset):  Example: approved.
            created_at (datetime.datetime | Unset):  Example: 2025-03-15T10:30:00Z.
     """

    id: int | Unset = UNSET
    user_id: int | Unset = UNSET
    company_name: str | Unset = UNSET
    website: None | str | Unset = UNSET
    status: MarketingPartnerStatus | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user_id = self.user_id

        company_name = self.company_name

        website: None | str | Unset
        if isinstance(self.website, Unset):
            website = UNSET
        else:
            website = self.website

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if website is not UNSET:
            field_dict["website"] = website
        if status is not UNSET:
            field_dict["status"] = status
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user_id = d.pop("user_id", UNSET)

        company_name = d.pop("company_name", UNSET)

        def _parse_website(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website = _parse_website(d.pop("website", UNSET))


        _status = d.pop("status", UNSET)
        status: MarketingPartnerStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = MarketingPartnerStatus(_status)




        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        marketing_partner = cls(
            id=id,
            user_id=user_id,
            company_name=company_name,
            website=website,
            status=status,
            created_at=created_at,
        )


        marketing_partner.additional_properties = d
        return marketing_partner

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
