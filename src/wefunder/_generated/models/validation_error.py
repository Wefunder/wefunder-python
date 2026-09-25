from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error_error import ValidationErrorError


T = TypeVar("T", bound="ValidationError")


@_attrs_define
class ValidationError:
    """Returned on `422 Unprocessable Entity` when request fields fail validation.
    `details` is an array of per-field problems.

        Attributes:
            error (ValidationErrorError | Unset):
    """

    error: ValidationErrorError | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_error_error import ValidationErrorError  # noqa: PLC0415

        d = dict(src_dict)
        _error = d.pop("error", UNSET)
        error: ValidationErrorError | Unset
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = ValidationErrorError.from_dict(_error)

        validation_error = cls(
            error=error,
        )

        validation_error.additional_properties = d
        return validation_error

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
