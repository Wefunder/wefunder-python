from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.test_webhook_endpoint_body_event import TestWebhookEndpointBodyEvent
from ..types import UNSET, Unset






T = TypeVar("T", bound="TestWebhookEndpointBody")



@_attrs_define
class TestWebhookEndpointBody:
    """ 
        Attributes:
            event (TestWebhookEndpointBodyEvent | Unset): Event to simulate. Defaults to the endpoint's first subscribed
                event.
     """

    event: TestWebhookEndpointBodyEvent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        event: str | Unset = UNSET
        if not isinstance(self.event, Unset):
            event = self.event.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if event is not UNSET:
            field_dict["event"] = event

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _event = d.pop("event", UNSET)
        event: TestWebhookEndpointBodyEvent | Unset
        if isinstance(_event,  Unset):
            event = UNSET
        else:
            event = TestWebhookEndpointBodyEvent(_event)




        test_webhook_endpoint_body = cls(
            event=event,
        )


        test_webhook_endpoint_body.additional_properties = d
        return test_webhook_endpoint_body

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
