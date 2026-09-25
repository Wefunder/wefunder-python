from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.validation_error_error_details_item import ValidationErrorErrorDetailsItem





T = TypeVar("T", bound="ValidationErrorError")



@_attrs_define
class ValidationErrorError:
    """ 
        Attributes:
            type_ (str | Unset):  Example: validation_error.
            message (str | Unset):  Example: Validation failed.
            details (list[ValidationErrorErrorDetailsItem] | Unset):
     """

    type_: str | Unset = UNSET
    message: str | Unset = UNSET
    details: list[ValidationErrorErrorDetailsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.validation_error_error_details_item import ValidationErrorErrorDetailsItem # noqa: PLC0415
        type_ = self.type_

        message = self.message

        details: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if message is not UNSET:
            field_dict["message"] = message
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.validation_error_error_details_item import ValidationErrorErrorDetailsItem # noqa: PLC0415
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        message = d.pop("message", UNSET)

        _details = d.pop("details", UNSET)
        details: list[ValidationErrorErrorDetailsItem] | Unset = UNSET
        if _details is not UNSET:
            details = []
            for details_item_data in _details:
                details_item = ValidationErrorErrorDetailsItem.from_dict(details_item_data)



                details.append(details_item)


        validation_error_error = cls(
            type_=type_,
            message=message,
            details=details,
        )


        validation_error_error.additional_properties = d
        return validation_error_error

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
