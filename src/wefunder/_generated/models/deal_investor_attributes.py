from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deal_investor_attributes_status import DealInvestorAttributesStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DealInvestorAttributes")


@_attrs_define
class DealInvestorAttributes:
    """
    Attributes:
        user_id (int | Unset): Internal integer id. Deprecated — use `user` (`usr_...`) instead. Example: 456.
        user (str | Unset): The investor's id (`usr_...`). Example: usr_aB3xQ9k2vF8mNp1zT5wY7Qc4.
        user_name (None | str | Unset):  Example: Jane Smith.
        user_email (None | str | Unset): **Moderator-only.** Investor's email address.
            Returns null for non-moderator callers (users who are not a manager/operator).
             Example: user@example.com.
        avatar_url (None | str | Unset): Investor's profile photo URL Example:
            https://uploads.wefunder.com/uploads/user/avatar/456/large_photo.jpg.
        amount (str | Unset): Investment amount in cents, as a string to avoid floating-point precision issues Example:
            500000.
        status (DealInvestorAttributesStatus | Unset): The investor's most advanced commitment in this deal —
            `confirmed` is final, `pending` is committed but not yet final. Example: confirmed.
        invested_at (datetime.datetime | Unset): ISO 8601 timestamp when the investment was created Example:
            2025-03-01T12:00:00Z.
    """

    user_id: int | Unset = UNSET
    user: str | Unset = UNSET
    user_name: None | str | Unset = UNSET
    user_email: None | str | Unset = UNSET
    avatar_url: None | str | Unset = UNSET
    amount: str | Unset = UNSET
    status: DealInvestorAttributesStatus | Unset = UNSET
    invested_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user = self.user

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        user_email: None | str | Unset
        if isinstance(self.user_email, Unset):
            user_email = UNSET
        else:
            user_email = self.user_email

        avatar_url: None | str | Unset
        if isinstance(self.avatar_url, Unset):
            avatar_url = UNSET
        else:
            avatar_url = self.avatar_url

        amount = self.amount

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        invested_at: str | Unset = UNSET
        if not isinstance(self.invested_at, Unset):
            invested_at = self.invested_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if user is not UNSET:
            field_dict["user"] = user
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if user_email is not UNSET:
            field_dict["user_email"] = user_email
        if avatar_url is not UNSET:
            field_dict["avatar_url"] = avatar_url
        if amount is not UNSET:
            field_dict["amount"] = amount
        if status is not UNSET:
            field_dict["status"] = status
        if invested_at is not UNSET:
            field_dict["invested_at"] = invested_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("user_id", UNSET)

        user = d.pop("user", UNSET)

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        def _parse_user_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_email = _parse_user_email(d.pop("user_email", UNSET))

        def _parse_avatar_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avatar_url = _parse_avatar_url(d.pop("avatar_url", UNSET))

        amount = d.pop("amount", UNSET)

        _status = d.pop("status", UNSET)
        status: DealInvestorAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DealInvestorAttributesStatus(_status)

        _invested_at = d.pop("invested_at", UNSET)
        invested_at: datetime.datetime | Unset
        if isinstance(_invested_at, Unset):
            invested_at = UNSET
        else:
            invested_at = datetime.datetime.fromisoformat(_invested_at)

        deal_investor_attributes = cls(
            user_id=user_id,
            user=user,
            user_name=user_name,
            user_email=user_email,
            avatar_url=avatar_url,
            amount=amount,
            status=status,
            invested_at=invested_at,
        )

        deal_investor_attributes.additional_properties = d
        return deal_investor_attributes

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
