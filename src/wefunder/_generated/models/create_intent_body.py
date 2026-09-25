from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_intent_body_action_name import CreateIntentBodyActionName
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_intent_body_params import CreateIntentBodyParams





T = TypeVar("T", bound="CreateIntentBody")



@_attrs_define
class CreateIntentBody:
    """ 
        Attributes:
            action_name (CreateIntentBodyActionName): The action to perform Example: syndicates.close_deal.
            resource_type (str): The resource type the action targets, as the action table names it; the example is the
                syndicate type. Example: Club.
            resource_id (str): The resource's id in the API's vocabulary — the syndicate's `syn_...` for a `syndicates.*`
                action. Example: syn_aB3xQ9k2vF8mNp1zT5wY7Qc4.
            params (CreateIntentBodyParams | Unset): Action-specific parameters Example: {'fundraise_id': 99}.
            idempotency_key (str | Unset): Client-provided key naming this one operation. While an intent with this key is
                pending, approved, executing, or executed, the same operation returns it (200); a different operation under the
                same key is a 409. Example: close-acme-series-a.
            requested_by_agent (str | Unset): Human-readable name of the agent proposing the action Example: Claude via MCP.
     """

    action_name: CreateIntentBodyActionName
    resource_type: str
    resource_id: str
    params: CreateIntentBodyParams | Unset = UNSET
    idempotency_key: str | Unset = UNSET
    requested_by_agent: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_intent_body_params import CreateIntentBodyParams # noqa: PLC0415
        action_name = self.action_name.value

        resource_type = self.resource_type

        resource_id = self.resource_id

        params: dict[str, Any] | Unset = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        idempotency_key = self.idempotency_key

        requested_by_agent = self.requested_by_agent


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "action_name": action_name,
            "resource_type": resource_type,
            "resource_id": resource_id,
        })
        if params is not UNSET:
            field_dict["params"] = params
        if idempotency_key is not UNSET:
            field_dict["idempotency_key"] = idempotency_key
        if requested_by_agent is not UNSET:
            field_dict["requested_by_agent"] = requested_by_agent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_intent_body_params import CreateIntentBodyParams # noqa: PLC0415
        d = dict(src_dict)
        action_name = CreateIntentBodyActionName(d.pop("action_name"))




        resource_type = d.pop("resource_type")

        resource_id = d.pop("resource_id")

        _params = d.pop("params", UNSET)
        params: CreateIntentBodyParams | Unset
        if isinstance(_params,  Unset):
            params = UNSET
        else:
            params = CreateIntentBodyParams.from_dict(_params)




        idempotency_key = d.pop("idempotency_key", UNSET)

        requested_by_agent = d.pop("requested_by_agent", UNSET)

        create_intent_body = cls(
            action_name=action_name,
            resource_type=resource_type,
            resource_id=resource_id,
            params=params,
            idempotency_key=idempotency_key,
            requested_by_agent=requested_by_agent,
        )


        create_intent_body.additional_properties = d
        return create_intent_body

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
