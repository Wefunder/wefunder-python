from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_endpoint_test_result_envelope_data_error_type_1 import (
    WebhookEndpointTestResultEnvelopeDataErrorType1,
)
from ..models.webhook_endpoint_test_result_envelope_data_error_type_2_type_1 import (
    WebhookEndpointTestResultEnvelopeDataErrorType2Type1,
)
from ..models.webhook_endpoint_test_result_envelope_data_error_type_3_type_1 import (
    WebhookEndpointTestResultEnvelopeDataErrorType3Type1,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_endpoint_test_result_envelope_data_payload import WebhookEndpointTestResultEnvelopeDataPayload


T = TypeVar("T", bound="WebhookEndpointTestResultEnvelopeData")


@_attrs_define
class WebhookEndpointTestResultEnvelopeData:
    """
    Attributes:
        type_ (str | Unset):  Example: webhook_test.
        delivered (bool | Unset):
        response_code (int | None | Unset):
        error (None | Unset | WebhookEndpointTestResultEnvelopeDataErrorType1 |
            WebhookEndpointTestResultEnvelopeDataErrorType2Type1 | WebhookEndpointTestResultEnvelopeDataErrorType3Type1):
            Why no HTTP response came back. `null` when the endpoint responded, even with a
            non-2xx status (see `response_code`). `blocked_url` means the URL failed the
            HTTPS/public-address check at send time.
        duration_ms (int | Unset):
        event (str | Unset):
        payload (WebhookEndpointTestResultEnvelopeDataPayload | Unset): The exact signed envelope that was POSTed.
    """

    type_: str | Unset = UNSET
    delivered: bool | Unset = UNSET
    response_code: int | None | Unset = UNSET
    error: (
        None
        | Unset
        | WebhookEndpointTestResultEnvelopeDataErrorType1
        | WebhookEndpointTestResultEnvelopeDataErrorType2Type1
        | WebhookEndpointTestResultEnvelopeDataErrorType3Type1
    ) = UNSET
    duration_ms: int | Unset = UNSET
    event: str | Unset = UNSET
    payload: WebhookEndpointTestResultEnvelopeDataPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        delivered = self.delivered

        response_code: int | None | Unset
        if isinstance(self.response_code, Unset):
            response_code = UNSET
        else:
            response_code = self.response_code

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif (
            isinstance(self.error, WebhookEndpointTestResultEnvelopeDataErrorType1)
            or isinstance(self.error, WebhookEndpointTestResultEnvelopeDataErrorType2Type1)
            or isinstance(self.error, WebhookEndpointTestResultEnvelopeDataErrorType3Type1)
        ):
            error = self.error.value
        else:
            error = self.error

        duration_ms = self.duration_ms

        event = self.event

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if delivered is not UNSET:
            field_dict["delivered"] = delivered
        if response_code is not UNSET:
            field_dict["response_code"] = response_code
        if error is not UNSET:
            field_dict["error"] = error
        if duration_ms is not UNSET:
            field_dict["duration_ms"] = duration_ms
        if event is not UNSET:
            field_dict["event"] = event
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_endpoint_test_result_envelope_data_payload import (
            WebhookEndpointTestResultEnvelopeDataPayload,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        delivered = d.pop("delivered", UNSET)

        def _parse_response_code(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        response_code = _parse_response_code(d.pop("response_code", UNSET))

        def _parse_error(
            data: object,
        ) -> (
            None
            | Unset
            | WebhookEndpointTestResultEnvelopeDataErrorType1
            | WebhookEndpointTestResultEnvelopeDataErrorType2Type1
            | WebhookEndpointTestResultEnvelopeDataErrorType3Type1
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                error_type_1 = WebhookEndpointTestResultEnvelopeDataErrorType1(data)

                return error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                error_type_2_type_1 = WebhookEndpointTestResultEnvelopeDataErrorType2Type1(data)

                return error_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                error_type_3_type_1 = WebhookEndpointTestResultEnvelopeDataErrorType3Type1(data)

                return error_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | Unset
                | WebhookEndpointTestResultEnvelopeDataErrorType1
                | WebhookEndpointTestResultEnvelopeDataErrorType2Type1
                | WebhookEndpointTestResultEnvelopeDataErrorType3Type1,
                data,
            )

        error = _parse_error(d.pop("error", UNSET))

        duration_ms = d.pop("duration_ms", UNSET)

        event = d.pop("event", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: WebhookEndpointTestResultEnvelopeDataPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = WebhookEndpointTestResultEnvelopeDataPayload.from_dict(_payload)

        webhook_endpoint_test_result_envelope_data = cls(
            type_=type_,
            delivered=delivered,
            response_code=response_code,
            error=error,
            duration_ms=duration_ms,
            event=event,
            payload=payload,
        )

        webhook_endpoint_test_result_envelope_data.additional_properties = d
        return webhook_endpoint_test_result_envelope_data

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
