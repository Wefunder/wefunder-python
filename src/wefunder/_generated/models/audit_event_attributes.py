from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.audit_event_attributes_status import AuditEventAttributesStatus
from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.audit_event_attributes_new_values_type_0 import AuditEventAttributesNewValuesType0
  from ..models.audit_event_attributes_old_values_type_0 import AuditEventAttributesOldValuesType0





T = TypeVar("T", bound="AuditEventAttributes")



@_attrs_define
class AuditEventAttributes:
    """ 
        Attributes:
            occurred_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
            actor_type (str | Unset): Type of actor (e.g. user, agent, system) Example: example.
            actor_name (None | str | Unset):  Example: ChatGPT via Wefunder MCP.
            action (str | Unset):  Example: syndicates.member.invited.
            resource_type (str | Unset):  Example: Club.
            resource_id (int | None | str | Unset): For Club resources, the syndicate's id (`syn_...`). For every other
                `resource_type` (contract change plans, tranches, applications, ...) the
                resource's integer id, since those models have no external id yet.
                 Example: syn_aB3xQ9k2vF8mNp1zT5wY7Qc4.
            resource_label (None | str | Unset):  Example: Acme Syndicate.
            old_values (AuditEventAttributesOldValuesType0 | None | Unset): Previous values of changed fields
            new_values (AuditEventAttributesNewValuesType0 | None | Unset): New values of changed fields
            changed_fields (list[str] | None | Unset): List of field names that changed
            status (AuditEventAttributesStatus | Unset):
            error_message (None | str | Unset):  Example: Example text.
            intent_id (None | str | Unset): Legacy UUID of the associated intent. Deprecated — use `intent` (`int_...`)
                instead.
            intent (None | str | Unset): The associated intent's id (`int_...`) if this event was triggered by an intent.
                Example: int_aB3xQ9k2vF8mNp1zT5wY7Qc4.
            created_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
     """

    occurred_at: datetime.datetime | Unset = UNSET
    actor_type: str | Unset = UNSET
    actor_name: None | str | Unset = UNSET
    action: str | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_id: int | None | str | Unset = UNSET
    resource_label: None | str | Unset = UNSET
    old_values: AuditEventAttributesOldValuesType0 | None | Unset = UNSET
    new_values: AuditEventAttributesNewValuesType0 | None | Unset = UNSET
    changed_fields: list[str] | None | Unset = UNSET
    status: AuditEventAttributesStatus | Unset = UNSET
    error_message: None | str | Unset = UNSET
    intent_id: None | str | Unset = UNSET
    intent: None | str | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.audit_event_attributes_new_values_type_0 import AuditEventAttributesNewValuesType0 # noqa: PLC0415
        from ..models.audit_event_attributes_old_values_type_0 import AuditEventAttributesOldValuesType0 # noqa: PLC0415
        occurred_at: str | Unset = UNSET
        if not isinstance(self.occurred_at, Unset):
            occurred_at = self.occurred_at.isoformat()

        actor_type = self.actor_type

        actor_name: None | str | Unset
        if isinstance(self.actor_name, Unset):
            actor_name = UNSET
        else:
            actor_name = self.actor_name

        action = self.action

        resource_type = self.resource_type

        resource_id: int | None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        resource_label: None | str | Unset
        if isinstance(self.resource_label, Unset):
            resource_label = UNSET
        else:
            resource_label = self.resource_label

        old_values: dict[str, Any] | None | Unset
        if isinstance(self.old_values, Unset):
            old_values = UNSET
        elif isinstance(self.old_values, AuditEventAttributesOldValuesType0):
            old_values = self.old_values.to_dict()
        else:
            old_values = self.old_values

        new_values: dict[str, Any] | None | Unset
        if isinstance(self.new_values, Unset):
            new_values = UNSET
        elif isinstance(self.new_values, AuditEventAttributesNewValuesType0):
            new_values = self.new_values.to_dict()
        else:
            new_values = self.new_values

        changed_fields: list[str] | None | Unset
        if isinstance(self.changed_fields, Unset):
            changed_fields = UNSET
        elif isinstance(self.changed_fields, list):
            changed_fields = self.changed_fields


        else:
            changed_fields = self.changed_fields

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value


        error_message: None | str | Unset
        if isinstance(self.error_message, Unset):
            error_message = UNSET
        else:
            error_message = self.error_message

        intent_id: None | str | Unset
        if isinstance(self.intent_id, Unset):
            intent_id = UNSET
        else:
            intent_id = self.intent_id

        intent: None | str | Unset
        if isinstance(self.intent, Unset):
            intent = UNSET
        else:
            intent = self.intent

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if occurred_at is not UNSET:
            field_dict["occurred_at"] = occurred_at
        if actor_type is not UNSET:
            field_dict["actor_type"] = actor_type
        if actor_name is not UNSET:
            field_dict["actor_name"] = actor_name
        if action is not UNSET:
            field_dict["action"] = action
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if resource_label is not UNSET:
            field_dict["resource_label"] = resource_label
        if old_values is not UNSET:
            field_dict["old_values"] = old_values
        if new_values is not UNSET:
            field_dict["new_values"] = new_values
        if changed_fields is not UNSET:
            field_dict["changed_fields"] = changed_fields
        if status is not UNSET:
            field_dict["status"] = status
        if error_message is not UNSET:
            field_dict["error_message"] = error_message
        if intent_id is not UNSET:
            field_dict["intent_id"] = intent_id
        if intent is not UNSET:
            field_dict["intent"] = intent
        if created_at is not UNSET:
            field_dict["created_at"] = created_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.audit_event_attributes_new_values_type_0 import AuditEventAttributesNewValuesType0 # noqa: PLC0415
        from ..models.audit_event_attributes_old_values_type_0 import AuditEventAttributesOldValuesType0 # noqa: PLC0415
        d = dict(src_dict)
        _occurred_at = d.pop("occurred_at", UNSET)
        occurred_at: datetime.datetime | Unset
        if isinstance(_occurred_at,  Unset):
            occurred_at = UNSET
        else:
            occurred_at = datetime.datetime.fromisoformat(_occurred_at)




        actor_type = d.pop("actor_type", UNSET)

        def _parse_actor_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        actor_name = _parse_actor_name(d.pop("actor_name", UNSET))


        action = d.pop("action", UNSET)

        resource_type = d.pop("resource_type", UNSET)

        def _parse_resource_id(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))


        def _parse_resource_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        resource_label = _parse_resource_label(d.pop("resource_label", UNSET))


        def _parse_old_values(data: object) -> AuditEventAttributesOldValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                old_values_type_0 = AuditEventAttributesOldValuesType0.from_dict(data)



                return old_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditEventAttributesOldValuesType0 | None | Unset, data)

        old_values = _parse_old_values(d.pop("old_values", UNSET))


        def _parse_new_values(data: object) -> AuditEventAttributesNewValuesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_values_type_0 = AuditEventAttributesNewValuesType0.from_dict(data)



                return new_values_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AuditEventAttributesNewValuesType0 | None | Unset, data)

        new_values = _parse_new_values(d.pop("new_values", UNSET))


        def _parse_changed_fields(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changed_fields_type_0 = cast(list[str], data)

                return changed_fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        changed_fields = _parse_changed_fields(d.pop("changed_fields", UNSET))


        _status = d.pop("status", UNSET)
        status: AuditEventAttributesStatus | Unset
        if isinstance(_status,  Unset):
            status = UNSET
        else:
            status = AuditEventAttributesStatus(_status)




        def _parse_error_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error_message = _parse_error_message(d.pop("error_message", UNSET))


        def _parse_intent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intent_id = _parse_intent_id(d.pop("intent_id", UNSET))


        def _parse_intent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        intent = _parse_intent(d.pop("intent", UNSET))


        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at,  Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)




        audit_event_attributes = cls(
            occurred_at=occurred_at,
            actor_type=actor_type,
            actor_name=actor_name,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            resource_label=resource_label,
            old_values=old_values,
            new_values=new_values,
            changed_fields=changed_fields,
            status=status,
            error_message=error_message,
            intent_id=intent_id,
            intent=intent,
            created_at=created_at,
        )


        audit_event_attributes.additional_properties = d
        return audit_event_attributes

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
