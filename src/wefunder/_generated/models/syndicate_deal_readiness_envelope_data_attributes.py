from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.syndicate_deal_readiness_envelope_data_attributes_status import (
    SyndicateDealReadinessEnvelopeDataAttributesStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.syndicate_deal_readiness_item import SyndicateDealReadinessItem


T = TypeVar("T", bound="SyndicateDealReadinessEnvelopeDataAttributes")


@_attrs_define
class SyndicateDealReadinessEnvelopeDataAttributes:
    """
    Attributes:
        ready (bool | Unset): Every item before `sign_and_open` is complete.
        status (SyndicateDealReadinessEnvelopeDataAttributesStatus | Unset):
        items (list[SyndicateDealReadinessItem] | Unset):
    """

    ready: bool | Unset = UNSET
    status: SyndicateDealReadinessEnvelopeDataAttributesStatus | Unset = UNSET
    items: list[SyndicateDealReadinessItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ready = self.ready

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ready is not UNSET:
            field_dict["ready"] = ready
        if status is not UNSET:
            field_dict["status"] = status
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.syndicate_deal_readiness_item import SyndicateDealReadinessItem  # noqa: PLC0415

        d = dict(src_dict)
        ready = d.pop("ready", UNSET)

        _status = d.pop("status", UNSET)
        status: SyndicateDealReadinessEnvelopeDataAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SyndicateDealReadinessEnvelopeDataAttributesStatus(_status)

        _items = d.pop("items", UNSET)
        items: list[SyndicateDealReadinessItem] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = SyndicateDealReadinessItem.from_dict(items_item_data)

                items.append(items_item)

        syndicate_deal_readiness_envelope_data_attributes = cls(
            ready=ready,
            status=status,
            items=items,
        )

        syndicate_deal_readiness_envelope_data_attributes.additional_properties = d
        return syndicate_deal_readiness_envelope_data_attributes

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
