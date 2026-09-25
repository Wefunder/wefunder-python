from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PartnerWebhookSubscriptionCreateInput")



@_attrs_define
class PartnerWebhookSubscriptionCreateInput:
    """ 
        Attributes:
            url (str):  Example: https://partner.com/webhooks/wefunder.
            events (list[str]):  Example: ['spv.opened', 'spv.closed', 'investment.created', 'investment.confirmed'].
     """

    url: str
    events: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = self.events




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "url": url,
            "events": events,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = cast(list[str], d.pop("events"))


        partner_webhook_subscription_create_input = cls(
            url=url,
            events=events,
        )


        partner_webhook_subscription_create_input.additional_properties = d
        return partner_webhook_subscription_create_input

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
