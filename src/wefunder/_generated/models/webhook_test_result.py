from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_test_result_payload_preview import WebhookTestResultPayloadPreview


T = TypeVar("T", bound="WebhookTestResult")


@_attrs_define
class WebhookTestResult:
    """
    Attributes:
        message (str | Unset):  Example: Test webhook queued for delivery.
        delivery_id (UUID | Unset):  Example: f47ac10b-58cc-4372-a567-0e02b2c3d479.
        payload_preview (WebhookTestResultPayloadPreview | Unset): The payload that was sent
    """

    message: str | Unset = UNSET
    delivery_id: UUID | Unset = UNSET
    payload_preview: WebhookTestResultPayloadPreview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        delivery_id: str | Unset = UNSET
        if not isinstance(self.delivery_id, Unset):
            delivery_id = str(self.delivery_id)

        payload_preview: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload_preview, Unset):
            payload_preview = self.payload_preview.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if delivery_id is not UNSET:
            field_dict["delivery_id"] = delivery_id
        if payload_preview is not UNSET:
            field_dict["payload_preview"] = payload_preview

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_test_result_payload_preview import WebhookTestResultPayloadPreview  # noqa: PLC0415

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _delivery_id = d.pop("delivery_id", UNSET)
        delivery_id: UUID | Unset
        if isinstance(_delivery_id, Unset):
            delivery_id = UNSET
        else:
            delivery_id = UUID(_delivery_id)

        _payload_preview = d.pop("payload_preview", UNSET)
        payload_preview: WebhookTestResultPayloadPreview | Unset
        if isinstance(_payload_preview, Unset):
            payload_preview = UNSET
        else:
            payload_preview = WebhookTestResultPayloadPreview.from_dict(_payload_preview)

        webhook_test_result = cls(
            message=message,
            delivery_id=delivery_id,
            payload_preview=payload_preview,
        )

        webhook_test_result.additional_properties = d
        return webhook_test_result

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
