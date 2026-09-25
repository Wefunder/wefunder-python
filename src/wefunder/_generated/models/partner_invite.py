from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.partner_invite_direction import PartnerInviteDirection
from ..models.partner_invite_status import PartnerInviteStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PartnerInvite")


@_attrs_define
class PartnerInvite:
    """An invite to establish a partner-company connection

    Attributes:
        id (int | Unset):  Example: 123.
        token (str | Unset): Unique invite token (use in accept URL) Example: abc123xyz789.
        direction (PartnerInviteDirection | Unset): Who initiated the invite Example: partner_to_founder.
        status (PartnerInviteStatus | Unset):  Example: pending.
        access_level (int | Unset): Access level granted on acceptance (1=anonymized, 2=detailed) Example: 1.
        company_id (int | None | Unset): Target company (null for partner_to_founder until accepted) Example: 789.
        company_name (None | str | Unset):  Example: My Startup Inc..
        partner_email (None | str | Unset): Partner email (for founder_to_partner invites) Example: partner@agency.com.
        expires_at (datetime.datetime | Unset):  Example: 2025-04-15T10:30:00Z.
        created_at (datetime.datetime | Unset):  Example: 2025-03-15T10:30:00Z.
        accept_url (str | Unset): URL to accept the invite Example:
            https://wefunder.com/attribution/invites/abc123xyz789.
    """

    id: int | Unset = UNSET
    token: str | Unset = UNSET
    direction: PartnerInviteDirection | Unset = UNSET
    status: PartnerInviteStatus | Unset = UNSET
    access_level: int | Unset = UNSET
    company_id: int | None | Unset = UNSET
    company_name: None | str | Unset = UNSET
    partner_email: None | str | Unset = UNSET
    expires_at: datetime.datetime | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    accept_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        token = self.token

        direction: str | Unset = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        access_level = self.access_level

        company_id: int | None | Unset
        if isinstance(self.company_id, Unset):
            company_id = UNSET
        else:
            company_id = self.company_id

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        partner_email: None | str | Unset
        if isinstance(self.partner_email, Unset):
            partner_email = UNSET
        else:
            partner_email = self.partner_email

        expires_at: str | Unset = UNSET
        if not isinstance(self.expires_at, Unset):
            expires_at = self.expires_at.isoformat()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        accept_url = self.accept_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if direction is not UNSET:
            field_dict["direction"] = direction
        if status is not UNSET:
            field_dict["status"] = status
        if access_level is not UNSET:
            field_dict["access_level"] = access_level
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if partner_email is not UNSET:
            field_dict["partner_email"] = partner_email
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if accept_url is not UNSET:
            field_dict["accept_url"] = accept_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        token = d.pop("token", UNSET)

        _direction = d.pop("direction", UNSET)
        direction: PartnerInviteDirection | Unset
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = PartnerInviteDirection(_direction)

        _status = d.pop("status", UNSET)
        status: PartnerInviteStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PartnerInviteStatus(_status)

        access_level = d.pop("access_level", UNSET)

        def _parse_company_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        company_id = _parse_company_id(d.pop("company_id", UNSET))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_partner_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        partner_email = _parse_partner_email(d.pop("partner_email", UNSET))

        _expires_at = d.pop("expires_at", UNSET)
        expires_at: datetime.datetime | Unset
        if isinstance(_expires_at, Unset):
            expires_at = UNSET
        else:
            expires_at = datetime.datetime.fromisoformat(_expires_at)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        accept_url = d.pop("accept_url", UNSET)

        partner_invite = cls(
            id=id,
            token=token,
            direction=direction,
            status=status,
            access_level=access_level,
            company_id=company_id,
            company_name=company_name,
            partner_email=partner_email,
            expires_at=expires_at,
            created_at=created_at,
            accept_url=accept_url,
        )

        partner_invite.additional_properties = d
        return partner_invite

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
