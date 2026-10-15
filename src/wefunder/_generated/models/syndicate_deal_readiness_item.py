from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.syndicate_deal_readiness_item_key import SyndicateDealReadinessItemKey
from ..models.syndicate_deal_readiness_item_status import SyndicateDealReadinessItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="SyndicateDealReadinessItem")


@_attrs_define
class SyndicateDealReadinessItem:
    """
    Attributes:
        key (SyndicateDealReadinessItemKey | Unset):
        label (str | Unset):  Example: Amount the SPV invests in the company.
        status (SyndicateDealReadinessItemStatus | Unset):
        detail (None | str | Unset): What is missing, in a sentence.
        action_url (None | str | Unset): The wefunder.com page where a person completes this step, when there is one.
        blocked_by (list[str] | Unset): Keys of the items that must be complete first.
    """

    key: SyndicateDealReadinessItemKey | Unset = UNSET
    label: str | Unset = UNSET
    status: SyndicateDealReadinessItemStatus | Unset = UNSET
    detail: None | str | Unset = UNSET
    action_url: None | str | Unset = UNSET
    blocked_by: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key: str | Unset = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.value

        label = self.label

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        action_url: None | str | Unset
        if isinstance(self.action_url, Unset):
            action_url = UNSET
        else:
            action_url = self.action_url

        blocked_by: list[str] | Unset = UNSET
        if not isinstance(self.blocked_by, Unset):
            blocked_by = self.blocked_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if label is not UNSET:
            field_dict["label"] = label
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if action_url is not UNSET:
            field_dict["action_url"] = action_url
        if blocked_by is not UNSET:
            field_dict["blocked_by"] = blocked_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _key = d.pop("key", UNSET)
        key: SyndicateDealReadinessItemKey | Unset
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = SyndicateDealReadinessItemKey(_key)

        label = d.pop("label", UNSET)

        _status = d.pop("status", UNSET)
        status: SyndicateDealReadinessItemStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SyndicateDealReadinessItemStatus(_status)

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_action_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        action_url = _parse_action_url(d.pop("action_url", UNSET))

        blocked_by = cast(list[str], d.pop("blocked_by", UNSET))

        syndicate_deal_readiness_item = cls(
            key=key,
            label=label,
            status=status,
            detail=detail,
            action_url=action_url,
            blocked_by=blocked_by,
        )

        syndicate_deal_readiness_item.additional_properties = d
        return syndicate_deal_readiness_item

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
