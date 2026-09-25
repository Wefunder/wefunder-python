from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.partner_webhook_subscription_attributes import PartnerWebhookSubscriptionAttributes


T = TypeVar("T", bound="PartnerWebhookSubscriptionWithSecret")


@_attrs_define
class PartnerWebhookSubscriptionWithSecret:
    """
    Attributes:
        id (str | Unset):  Example: whs_abc123.
        type_ (str | Unset):  Example: webhook_subscription.
        attributes (PartnerWebhookSubscriptionAttributes | Unset):
    """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: PartnerWebhookSubscriptionAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

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
        from ..models.partner_webhook_subscription_attributes import (
            PartnerWebhookSubscriptionAttributes,  # noqa: PLC0415
        )

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: PartnerWebhookSubscriptionAttributes | Unset
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = PartnerWebhookSubscriptionAttributes.from_dict(_attributes)

        partner_webhook_subscription_with_secret = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )

        partner_webhook_subscription_with_secret.additional_properties = d
        return partner_webhook_subscription_with_secret

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
