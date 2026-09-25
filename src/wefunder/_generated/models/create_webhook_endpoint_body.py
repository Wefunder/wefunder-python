from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_webhook_endpoint_body_events_item import CreateWebhookEndpointBodyEventsItem
from ..models.create_webhook_endpoint_body_mode import CreateWebhookEndpointBodyMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWebhookEndpointBody")


@_attrs_define
class CreateWebhookEndpointBody:
    """
    Attributes:
        url (str): Public HTTPS URL to receive deliveries (private/internal IPs rejected). Example:
            https://yourapp.com/webhooks/wefunder.
        events (list[CreateWebhookEndpointBodyEventsItem]): Event names to subscribe to (from the event catalog). At
            least one. Example: ['offering.opened', 'investment.executed'].
        mode (CreateWebhookEndpointBodyMode | Unset):  Default: CreateWebhookEndpointBodyMode.LIVE.
    """

    url: str
    events: list[CreateWebhookEndpointBodyEventsItem]
    mode: CreateWebhookEndpointBodyMode | Unset = CreateWebhookEndpointBodyMode.LIVE
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
                "events": events,
            }
        )
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = CreateWebhookEndpointBodyEventsItem(events_item_data)

            events.append(events_item)

        _mode = d.pop("mode", UNSET)
        mode: CreateWebhookEndpointBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateWebhookEndpointBodyMode(_mode)

        create_webhook_endpoint_body = cls(
            url=url,
            events=events,
            mode=mode,
        )

        create_webhook_endpoint_body.additional_properties = d
        return create_webhook_endpoint_body

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
