from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.partner_webhook_event_data import PartnerWebhookEventData





T = TypeVar("T", bound="PartnerWebhookEvent")



@_attrs_define
class PartnerWebhookEvent:
    """ The payload delivered to a subscribed webhook URL.

        Attributes:
            id (str | Unset):  Example: evt_abc123.
            event (str | Unset): The event type. SPV: `spv.created`, `spv.opened`, `spv.updated`,
                `spv.closing`, `spv.closed`, `spv.canceled`. Invites/sessions:
                `invite.created`, `invite.opened`, `invite.invested`, `invite.expired`,
                `investment_session.created`, `investment_session.completed`. Investments:
                `investment.created`, `investment.confirmed`, `investment.canceled`,
                `investment.accreditation_verified`, `investment.accreditation_failed`.
                Disbursement: `disbursement.initiated`, `disbursement.completed`,
                `disbursement.failed`. Plus `webhook.test`.
                 Example: investment.created.
            created_at (datetime.datetime | Unset):  Example: 2025-01-15T15:00:00Z.
            data (PartnerWebhookEventData | Unset): Event-specific payload (e.g. the affected SPV and investment).
            partner_reference (None | str | Unset): Echoes the SPV's `metadata.partner_reference` when present. Example:
                acme-series-a-2025.
     """

    id: str | Unset = UNSET
    event: str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    data: PartnerWebhookEventData | Unset = UNSET
    partner_reference: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.partner_webhook_event_data import PartnerWebhookEventData # noqa: PLC0415
        id = self.id

        event = self.event

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        partner_reference: None | str | Unset
        if isinstance(self.partner_reference, Unset):
            partner_reference = UNSET
        else:
            partner_reference = self.partner_reference


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if event is not UNSET:
            field_dict["event"] = event
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if data is not UNSET:
            field_dict["data"] = data
        if partner_reference is not UNSET:
            field_dict["partner_reference"] = partner_reference

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.partner_webhook_event_data import PartnerWebhookEventData # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        event = d.pop("event", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        _data = d.pop("data", UNSET)
        data: PartnerWebhookEventData | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = PartnerWebhookEventData.from_dict(_data)




        def _parse_partner_reference(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_reference = _parse_partner_reference(d.pop("partner_reference", UNSET))


        partner_webhook_event = cls(
            id=id,
            event=event,
            created_at=created_at,
            data=data,
            partner_reference=partner_reference,
        )


        partner_webhook_event.additional_properties = d
        return partner_webhook_event

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
