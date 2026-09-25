from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_error_details import ErrorErrorDetails


T = TypeVar("T", bound="ErrorError")


@_attrs_define
class ErrorError:
    """
    Attributes:
        type_ (str | Unset):  Example: unauthorized.
        message (str | Unset):  Example: Invalid or expired token.
        details (ErrorErrorDetails | Unset):
        request_id (str | Unset): Unique identifier for this request. Quote it in support tickets. Example: req_abc123.
        remediation (str | Unset): When present, a hint on how to resolve the error. Example: Obtain a new access token
            using the OAuth 2.0 flow..
    """

    type_: str | Unset = UNSET
    message: str | Unset = UNSET
    details: ErrorErrorDetails | Unset = UNSET
    request_id: str | Unset = UNSET
    remediation: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        message = self.message

        details: dict[str, Any] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = self.details.to_dict()

        request_id = self.request_id

        remediation = self.remediation

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if remediation is not UNSET:
            field_dict["remediation"] = remediation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_error_details import ErrorErrorDetails  # noqa: PLC0415

        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: ErrorErrorDetails | Unset
        if isinstance(_details, Unset):
            details = UNSET
        else:
            details = ErrorErrorDetails.from_dict(_details)

        request_id = d.pop("request_id", UNSET)

        remediation = d.pop("remediation", UNSET)

        error_error = cls(
            type_=type_,
            message=message,
            details=details,
            request_id=request_id,
            remediation=remediation,
        )

        error_error.additional_properties = d
        return error_error

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
