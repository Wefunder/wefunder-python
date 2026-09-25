from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.intent_attributes_status import IntentAttributesStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.intent_attributes_execution_result_type_0 import IntentAttributesExecutionResultType0


T = TypeVar("T", bound="IntentAttributes")


@_attrs_define
class IntentAttributes:
    """
    Attributes:
        action (str | Unset):  Example: syndicates.close_deal.
        status (IntentAttributesStatus | Unset):  Example: pending.
        resource_type (str | Unset):  Example: Club.
        resource_id (int | None | str | Unset): For Club resources, the syndicate's id (`syn_...`). For every other
            `resource_type` (contract change plans, tranches, applications, ...) the
            resource's integer id, since those models have no external id yet.
             Example: syn_aB3xQ9k2vF8mNp1zT5wY7Qc4.
        impact_summary (str | Unset):  Example: Close the Acme Corp Series A deal. 47 investors have committed $2.3M..
        review_url (str | Unset): URL where a human can review and approve/reject this intent Example:
            https://wefunder.com/intents/a1b2c3d4-e5f6-7890-abcd-ef1234567890/review.
        requested_by_agent (None | str | Unset): Human-readable name of the agent that proposed this intent Example:
            Claude via MCP.
        expires_at (datetime.datetime | None | Unset):  Example: 2025-03-01T12:00:00Z.
        approved_at (datetime.datetime | None | Unset):  Example: 2025-03-01T12:00:00Z.
        executed_at (datetime.datetime | None | Unset):  Example: 2025-03-01T12:00:00Z.
        rejection_reason (None | str | Unset):  Example: Example text.
        execution_result (IntentAttributesExecutionResultType0 | None | Unset): Action-specific result data (only
            present when status is executed)
        created_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
        updated_at (datetime.datetime | Unset):  Example: 2025-03-01T12:00:00Z.
    """

    action: str | Unset = UNSET
    status: IntentAttributesStatus | Unset = UNSET
    resource_type: str | Unset = UNSET
    resource_id: int | None | str | Unset = UNSET
    impact_summary: str | Unset = UNSET
    review_url: str | Unset = UNSET
    requested_by_agent: None | str | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    approved_at: datetime.datetime | None | Unset = UNSET
    executed_at: datetime.datetime | None | Unset = UNSET
    rejection_reason: None | str | Unset = UNSET
    execution_result: IntentAttributesExecutionResultType0 | None | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.intent_attributes_execution_result_type_0 import (
            IntentAttributesExecutionResultType0,  # noqa: PLC0415
        )

        action = self.action

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        resource_type = self.resource_type

        resource_id: int | None | str | Unset
        if isinstance(self.resource_id, Unset):
            resource_id = UNSET
        else:
            resource_id = self.resource_id

        impact_summary = self.impact_summary

        review_url = self.review_url

        requested_by_agent: None | str | Unset
        if isinstance(self.requested_by_agent, Unset):
            requested_by_agent = UNSET
        else:
            requested_by_agent = self.requested_by_agent

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        approved_at: None | str | Unset
        if isinstance(self.approved_at, Unset):
            approved_at = UNSET
        elif isinstance(self.approved_at, datetime.datetime):
            approved_at = self.approved_at.isoformat()
        else:
            approved_at = self.approved_at

        executed_at: None | str | Unset
        if isinstance(self.executed_at, Unset):
            executed_at = UNSET
        elif isinstance(self.executed_at, datetime.datetime):
            executed_at = self.executed_at.isoformat()
        else:
            executed_at = self.executed_at

        rejection_reason: None | str | Unset
        if isinstance(self.rejection_reason, Unset):
            rejection_reason = UNSET
        else:
            rejection_reason = self.rejection_reason

        execution_result: dict[str, Any] | None | Unset
        if isinstance(self.execution_result, Unset):
            execution_result = UNSET
        elif isinstance(self.execution_result, IntentAttributesExecutionResultType0):
            execution_result = self.execution_result.to_dict()
        else:
            execution_result = self.execution_result

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if action is not UNSET:
            field_dict["action"] = action
        if status is not UNSET:
            field_dict["status"] = status
        if resource_type is not UNSET:
            field_dict["resource_type"] = resource_type
        if resource_id is not UNSET:
            field_dict["resource_id"] = resource_id
        if impact_summary is not UNSET:
            field_dict["impact_summary"] = impact_summary
        if review_url is not UNSET:
            field_dict["review_url"] = review_url
        if requested_by_agent is not UNSET:
            field_dict["requested_by_agent"] = requested_by_agent
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if approved_at is not UNSET:
            field_dict["approved_at"] = approved_at
        if executed_at is not UNSET:
            field_dict["executed_at"] = executed_at
        if rejection_reason is not UNSET:
            field_dict["rejection_reason"] = rejection_reason
        if execution_result is not UNSET:
            field_dict["execution_result"] = execution_result
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.intent_attributes_execution_result_type_0 import (
            IntentAttributesExecutionResultType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        action = d.pop("action", UNSET)

        _status = d.pop("status", UNSET)
        status: IntentAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IntentAttributesStatus(_status)

        resource_type = d.pop("resource_type", UNSET)

        def _parse_resource_id(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        resource_id = _parse_resource_id(d.pop("resource_id", UNSET))

        impact_summary = d.pop("impact_summary", UNSET)

        review_url = d.pop("review_url", UNSET)

        def _parse_requested_by_agent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        requested_by_agent = _parse_requested_by_agent(d.pop("requested_by_agent", UNSET))

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))

        def _parse_approved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_at_type_0 = datetime.datetime.fromisoformat(data)

                return approved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        approved_at = _parse_approved_at(d.pop("approved_at", UNSET))

        def _parse_executed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                executed_at_type_0 = datetime.datetime.fromisoformat(data)

                return executed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        executed_at = _parse_executed_at(d.pop("executed_at", UNSET))

        def _parse_rejection_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason", UNSET))

        def _parse_execution_result(data: object) -> IntentAttributesExecutionResultType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_result_type_0 = IntentAttributesExecutionResultType0.from_dict(data)

                return execution_result_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IntentAttributesExecutionResultType0 | None | Unset, data)

        execution_result = _parse_execution_result(d.pop("execution_result", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        intent_attributes = cls(
            action=action,
            status=status,
            resource_type=resource_type,
            resource_id=resource_id,
            impact_summary=impact_summary,
            review_url=review_url,
            requested_by_agent=requested_by_agent,
            expires_at=expires_at,
            approved_at=approved_at,
            executed_at=executed_at,
            rejection_reason=rejection_reason,
            execution_result=execution_result,
            created_at=created_at,
            updated_at=updated_at,
        )

        intent_attributes.additional_properties = d
        return intent_attributes

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
