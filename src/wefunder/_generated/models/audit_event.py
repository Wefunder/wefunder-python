from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.audit_event_attributes import AuditEventAttributes


T = TypeVar("T", bound="AuditEvent")


@_attrs_define
class AuditEvent:
    """JSON:API resource representing an audit event

    Attributes:
        id (UUID | Unset): Event id (UUID). Example: 6f1c2d3e-4a5b-4c6d-8e9f-0a1b2c3d4e5f.
        type_ (str | Unset):  Example: audit_event.
        attributes (AuditEventAttributes | Unset):
    """

    id: UUID | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: AuditEventAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: str | Unset = UNSET
        if not isinstance(self.id, Unset):
            id = str(self.id)

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_event_attributes import AuditEventAttributes  # noqa: PLC0415

        d = dict(src_dict)
        _id = d.pop("id", UNSET)
        id: UUID | Unset
        if isinstance(_id, Unset):
            id = UNSET
        else:
            id = UUID(_id)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: AuditEventAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AuditEventAttributes.from_dict(_attributes)

        audit_event = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        audit_event.additional_properties = d
        return audit_event

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
