from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WebhookSubscriptionListEnvelopeMeta")



@_attrs_define
class WebhookSubscriptionListEnvelopeMeta:
    """ 
        Attributes:
            total (int | Unset): Number of active subscriptions Example: 2.
            limit (int | Unset): Maximum subscriptions per application Example: 10.
     """

    total: int | Unset = UNSET
    limit: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total = self.total

        limit = self.limit


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        limit = d.pop("limit", UNSET)

        webhook_subscription_list_envelope_meta = cls(
            total=total,
            limit=limit,
        )


        webhook_subscription_list_envelope_meta.additional_properties = d
        return webhook_subscription_list_envelope_meta

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
