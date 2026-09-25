from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IntentReview")


@_attrs_define
class IntentReview:
    """Lightweight handle to a pending intent a permitted human must approve for the action to take effect. The full intent
    is not readable through this API; the review_url is the approval link. Returned under `meta.<action>_intent` by the
    endpoints that server-mint an intent (partner SPV close/cancel, syndicate deal close/finalize).

        Attributes:
            id (str | Unset): The intent's id (`int_...`). Poll it at `GET /intents/{intent_id}`. Example:
                int_aB3xQ9k2vF8mNp1zT5wY7Qc4.
            status (str | Unset):  Example: pending.
            review_url (str | Unset):  Example: https://wefunder.com/intents/a1b2c3d4-e5f6-7890-abcd-ef1234567890/review.
    """

    id: str | Unset = UNSET
    status: str | Unset = UNSET
    review_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        status = self.status

        review_url = self.review_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if status is not UNSET:
            field_dict["status"] = status
        if review_url is not UNSET:
            field_dict["review_url"] = review_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        status = d.pop("status", UNSET)

        review_url = d.pop("review_url", UNSET)

        intent_review = cls(
            id=id,
            status=status,
            review_url=review_url,
        )

        intent_review.additional_properties = d
        return intent_review

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
