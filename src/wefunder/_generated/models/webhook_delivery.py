from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_delivery_status import WebhookDeliveryStatus
from ..types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime






T = TypeVar("T", bound="WebhookDelivery")



@_attrs_define
class WebhookDelivery:
    """ A single webhook delivery attempt

        Attributes:
            id (int | Unset):  Example: 456.
            delivery_uuid (UUID | Unset): Unique delivery identifier (use for idempotency) Example:
                f47ac10b-58cc-4372-a567-0e02b2c3d479.
            event_type (str | Unset): The event that triggered this delivery Example: investment.applied.
            status (WebhookDeliveryStatus | Unset):  Example: delivered.
            attempts (int | Unset): Number of delivery attempts Example: 1.
            response_code (int | None | Unset): HTTP status code from the last attempt Example: 200.
            last_attempt_at (datetime.datetime | None | Unset):  Example: 2025-03-15T10:31:00Z.
            created_at (datetime.datetime | Unset):  Example: 2025-03-15T10:30:00Z.
     """

    id: int | Unset = UNSET
    delivery_uuid: UUID | Unset = UNSET
    event_type: str | Unset = UNSET
    status: WebhookDeliveryStatus | Unset = UNSET
    attempts: int | Unset = UNSET
    response_code: int | None | Unset = UNSET
    last_attempt_at: datetime.datetime | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        delivery_uuid: str | Unset = UNSET
        if not isinstance(self.delivery_uuid, Unset):
            delivery_uuid = str(self.delivery_uuid)

        event_type = self.event_type

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        attempts = self.attempts

        response_code: int | None | Unset
        if isinstance(self.response_code, Unset):
            response_code = UNSET
        else:
            response_code = self.response_code

        last_attempt_at: None | str | Unset
        if isinstance(self.last_attempt_at, Unset):
            last_attempt_at = UNSET
        elif isinstance(self.last_attempt_at, datetime.datetime):
            last_attempt_at = self.last_attempt_at.isoformat()
        else:
            last_attempt_at = self.last_attempt_at

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if delivery_uuid is not UNSET:
            field_dict["delivery_uuid"] = delivery_uuid
        if event_type is not UNSET:
            field_dict["event_type"] = event_type
        if status is not UNSET:
            field_dict["status"] = status
        if attempts is not UNSET:
            field_dict["attempts"] = attempts
        if response_code is not UNSET:
            field_dict["response_code"] = response_code
        if last_attempt_at is not UNSET:
            field_dict["last_attempt_at"] = last_attempt_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _delivery_uuid = d.pop("delivery_uuid", UNSET)
        delivery_uuid: UUID | Unset
        if isinstance(_delivery_uuid,  Unset):
            delivery_uuid = UNSET
        else:
            delivery_uuid = UUID(_delivery_uuid)




        event_type = d.pop("event_type", UNSET)

        _status = d.pop("status", UNSET)
        status: WebhookDeliveryStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = WebhookDeliveryStatus(_status)




        attempts = d.pop("attempts", UNSET)

        def _parse_response_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        response_code = _parse_response_code(d.pop("response_code", UNSET))


        def _parse_last_attempt_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_attempt_at_type_0 = datetime.datetime.fromisoformat(data)



                return last_attempt_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_attempt_at = _parse_last_attempt_at(d.pop("last_attempt_at", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        webhook_delivery = cls(
            id=id,
            delivery_uuid=delivery_uuid,
            event_type=event_type,
            status=status,
            attempts=attempts,
            response_code=response_code,
            last_attempt_at=last_attempt_at,
            created_at=created_at,
        )


        webhook_delivery.additional_properties = d
        return webhook_delivery

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
