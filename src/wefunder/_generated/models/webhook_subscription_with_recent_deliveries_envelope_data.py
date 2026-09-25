from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_subscription_events_item import WebhookSubscriptionEventsItem
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.webhook_delivery import WebhookDelivery





T = TypeVar("T", bound="WebhookSubscriptionWithRecentDeliveriesEnvelopeData")



@_attrs_define
class WebhookSubscriptionWithRecentDeliveriesEnvelopeData:
    """ 
        Attributes:
            id (int | Unset):  Example: 123.
            campaign_id (int | Unset):  Example: 789.
            target_url (str | Unset):  Example: https://yourapp.com/webhooks/wefunder.
            events (list[WebhookSubscriptionEventsItem] | Unset):  Example: ['investment.applied', 'investment.confirmed'].
            active (bool | Unset): Whether the subscription is active Example: True.
            consecutive_failures (int | Unset): Number of consecutive delivery failures (resets on success) Example: 0.
            created_at (datetime.datetime | Unset):  Example: 2025-03-15T10:30:00Z.
            updated_at (datetime.datetime | Unset):  Example: 2025-03-15T10:30:00Z.
            recent_deliveries (list[WebhookDelivery] | Unset): Last 10 delivery attempts
     """

    id: int | Unset = UNSET
    campaign_id: int | Unset = UNSET
    target_url: str | Unset = UNSET
    events: list[WebhookSubscriptionEventsItem] | Unset = UNSET
    active: bool | Unset = UNSET
    consecutive_failures: int | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    recent_deliveries: list[WebhookDelivery] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_delivery import WebhookDelivery # noqa: PLC0415
        id = self.id

        campaign_id = self.campaign_id

        target_url = self.target_url

        events: list[str] | Unset = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.value
                events.append(events_item)



        active = self.active

        consecutive_failures = self.consecutive_failures

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        recent_deliveries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.recent_deliveries, Unset):
            recent_deliveries = []
            for recent_deliveries_item_data in self.recent_deliveries:
                recent_deliveries_item = recent_deliveries_item_data.to_dict()
                recent_deliveries.append(recent_deliveries_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if target_url is not UNSET:
            field_dict["target_url"] = target_url
        if events is not UNSET:
            field_dict["events"] = events
        if active is not UNSET:
            field_dict["active"] = active
        if consecutive_failures is not UNSET:
            field_dict["consecutive_failures"] = consecutive_failures
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if recent_deliveries is not UNSET:
            field_dict["recent_deliveries"] = recent_deliveries

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_delivery import WebhookDelivery # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        campaign_id = d.pop("campaign_id", UNSET)

        target_url = d.pop("target_url", UNSET)

        _events = d.pop("events", UNSET)
        events: list[WebhookSubscriptionEventsItem] | Unset = UNSET
        if _events is not UNSET:
            events = []
            for events_item_data in _events:
                events_item = WebhookSubscriptionEventsItem(events_item_data)



                events.append(events_item)


        active = d.pop("active", UNSET)

        consecutive_failures = d.pop("consecutive_failures", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at,  Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)




        _recent_deliveries = d.pop("recent_deliveries", UNSET)
        recent_deliveries: list[WebhookDelivery] | Unset = UNSET
        if _recent_deliveries is not UNSET:
            recent_deliveries = []
            for recent_deliveries_item_data in _recent_deliveries:
                recent_deliveries_item = WebhookDelivery.from_dict(recent_deliveries_item_data)



                recent_deliveries.append(recent_deliveries_item)


        webhook_subscription_with_recent_deliveries_envelope_data = cls(
            id=id,
            campaign_id=campaign_id,
            target_url=target_url,
            events=events,
            active=active,
            consecutive_failures=consecutive_failures,
            created_at=created_at,
            updated_at=updated_at,
            recent_deliveries=recent_deliveries,
        )


        webhook_subscription_with_recent_deliveries_envelope_data.additional_properties = d
        return webhook_subscription_with_recent_deliveries_envelope_data

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
