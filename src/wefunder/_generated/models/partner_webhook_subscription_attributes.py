from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="PartnerWebhookSubscriptionAttributes")



@_attrs_define
class PartnerWebhookSubscriptionAttributes:
    """ 
        Attributes:
            url (str | Unset):  Example: https://partner.com/webhooks/wefunder.
            events (list[str] | Unset):  Example: ['spv.opened', 'spv.closed'].
            active (bool | Unset):  Example: True.
            created_at (datetime.datetime | Unset):  Example: 2025-01-15T10:00:00Z.
     """

    url: str | Unset = UNSET
    events: list[str] | Unset = UNSET
    active: bool | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = self.events



        active = self.active

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if url is not UNSET:
            field_dict["url"] = url
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        events = cast(list[str], d.pop("events", UNSET))


        active = d.pop("active", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        partner_webhook_subscription_attributes = cls(
            url=url,
            events=events,
            active=active,
            created_at=created_at,
        )


        partner_webhook_subscription_attributes.additional_properties = d
        return partner_webhook_subscription_attributes

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
