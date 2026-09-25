from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.safe_security_type import SafeSecurityType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.safe_security_terms import SafeSecurityTerms


T = TypeVar("T", bound="SafeSecurity")


@_attrs_define
class SafeSecurity:
    """
    Attributes:
        type_ (SafeSecurityType | Unset):
        label (str | Unset):  Example: SAFE.
        terms (SafeSecurityTerms | Unset):
    """

    type_: SafeSecurityType | Unset = UNSET
    label: str | Unset = UNSET
    terms: SafeSecurityTerms | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        label = self.label

        terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if label is not UNSET:
            field_dict["label"] = label
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.safe_security_terms import SafeSecurityTerms  # noqa: PLC0415

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: SafeSecurityType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SafeSecurityType(_type_)

        label = d.pop("label", UNSET)

        _terms = d.pop("terms", UNSET)
        terms: SafeSecurityTerms | Unset
        if isinstance(_terms, Unset):
            terms = UNSET
        else:
            terms = SafeSecurityTerms.from_dict(_terms)

        safe_security = cls(
            type_=type_,
            label=label,
            terms=terms,
        )

        safe_security.additional_properties = d
        return safe_security

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
