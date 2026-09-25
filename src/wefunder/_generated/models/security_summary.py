from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.security_summary_type import SecuritySummaryType

T = TypeVar("T", bound="SecuritySummary")


@_attrs_define
class SecuritySummary:
    """The kind of security without its terms — the `type` / `label` pair shared by every
    `Security` variant. Used where the terms live elsewhere (portfolio positions) or are
    not final (a Testing-the-Waters round's `intended_security`).

        Attributes:
            type_ (SecuritySummaryType):  Example: safe.
            label (str):  Example: SAFE.
    """

    type_: SecuritySummaryType
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SecuritySummaryType(d.pop("type"))

        label = d.pop("label")

        security_summary = cls(
            type_=type_,
            label=label,
        )

        security_summary.additional_properties = d
        return security_summary

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
