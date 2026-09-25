from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_webhook_endpoint_body_events_item import UpdateWebhookEndpointBodyEventsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWebhookEndpointBody")


@_attrs_define
class UpdateWebhookEndpointBody:
    """
    Attributes:
        url (str | Unset):
        events (list[UpdateWebhookEndpointBodyEventsItem] | Unset):
    """

    url: str | Unset = UNSET
    events: list[UpdateWebhookEndpointBodyEventsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if url is not UNSET:
            field_dict["url"] = url
        if events is not UNSET:
            field_dict["events"] = events

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url", UNSET)

        _events = d.pop("events", UNSET)
        events: list[UpdateWebhookEndpointBodyEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = UpdateWebhookEndpointBodyEventsItem(events_item_data)

                events.append(events_item)

        update_webhook_endpoint_body = cls(
            url=url,
            events=events,
        )

        update_webhook_endpoint_body.additional_properties = d
        return update_webhook_endpoint_body

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
