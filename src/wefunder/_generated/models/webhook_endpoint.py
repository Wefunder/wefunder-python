from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.webhook_endpoint_attributes import WebhookEndpointAttributes





T = TypeVar("T", bound="WebhookEndpoint")



@_attrs_define
class WebhookEndpoint:
    """ 
        Attributes:
            id (str | Unset):  Example: whe_8f3ExampleEndpoint00.
            type_ (str | Unset):  Example: webhook_endpoint.
            attributes (WebhookEndpointAttributes | Unset):
     """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    attributes: WebhookEndpointAttributes | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.webhook_endpoint_attributes import WebhookEndpointAttributes # noqa: PLC0415
        id = self.id

        type_ = self.type_

        attributes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if attributes is not UNSET:
            field_dict["attributes"] = attributes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_endpoint_attributes import WebhookEndpointAttributes # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: WebhookEndpointAttributes | Unset
        if isinstance(_attributes,  Unset):
            attributes = UNSET
        else:
            attributes = WebhookEndpointAttributes.from_dict(_attributes)




        webhook_endpoint = cls(
            id=id,
            type_=type_,
            attributes=attributes,
        )


        webhook_endpoint.additional_properties = d
        return webhook_endpoint

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
