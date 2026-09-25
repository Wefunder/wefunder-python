from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteLinkCreateInput")


@_attrs_define
class InviteLinkCreateInput:
    """All fields optional. With no `email`/`wefunder_user_id` the link is
    **reusable**; with either it becomes a **per-person** invite. `email` and
    `wefunder_user_id` are mutually exclusive. `max_uses` is rejected for
    per-person invites; `send_email` is rejected without a recipient.

        Attributes:
            allocation_cents (int | None | Unset): Budget cap, in cents. Reusable → total budget across all claims of the
                link. Per-person → the single recipient's cap.
                 Example: 5000000.
            max_uses (int | None | Unset): Claim cap for a reusable link. Null = unlimited. Not allowed for per-person
                invites. Example: 50.
            email (None | str | Unset): Recipient email. Makes the link per-person. Mutually exclusive with
                `wefunder_user_id`. Example: investor@example.com.
            wefunder_user_id (None | str | Unset): Id (`usr_...`) of an existing Wefunder user to invite. Mutually exclusive
                with `email`; must resolve to a user (else 404). Example: usr_existing123.
            first_name (None | str | Unset): Recipient first name (per-person only). Example: Jane.
            last_name (None | str | Unset): Recipient last name (per-person only). Example: Investor.
            message (None | str | Unset): Personal message included in the invite email (per-person only). Example: Excited
                to have you in this deal!.
            send_email (bool | Unset): Whether to email the invite (per-person only). Rejected on a reusable create.
                Default: True.
    """

    allocation_cents: int | None | Unset = UNSET
    max_uses: int | None | Unset = UNSET
    email: None | str | Unset = UNSET
    wefunder_user_id: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    message: None | str | Unset = UNSET
    send_email: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allocation_cents: int | None | Unset
        if isinstance(self.allocation_cents, Unset):
            allocation_cents = UNSET
        else:
            allocation_cents = self.allocation_cents

        max_uses: int | None | Unset
        if isinstance(self.max_uses, Unset):
            max_uses = UNSET
        else:
            max_uses = self.max_uses

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        wefunder_user_id: None | str | Unset
        if isinstance(self.wefunder_user_id, Unset):
            wefunder_user_id = UNSET
        else:
            wefunder_user_id = self.wefunder_user_id

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        send_email = self.send_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation_cents is not UNSET:
            field_dict["allocation_cents"] = allocation_cents
        if max_uses is not UNSET:
            field_dict["max_uses"] = max_uses
        if email is not UNSET:
            field_dict["email"] = email
        if wefunder_user_id is not UNSET:
            field_dict["wefunder_user_id"] = wefunder_user_id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if message is not UNSET:
            field_dict["message"] = message
        if send_email is not UNSET:
            field_dict["send_email"] = send_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_allocation_cents(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        allocation_cents = _parse_allocation_cents(d.pop("allocation_cents", UNSET))

        def _parse_max_uses(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_uses = _parse_max_uses(d.pop("max_uses", UNSET))

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_wefunder_user_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        wefunder_user_id = _parse_wefunder_user_id(d.pop("wefunder_user_id", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        send_email = d.pop("send_email", UNSET)

        invite_link_create_input = cls(
            allocation_cents=allocation_cents,
            max_uses=max_uses,
            email=email,
            wefunder_user_id=wefunder_user_id,
            first_name=first_name,
            last_name=last_name,
            message=message,
            send_email=send_email,
        )

        invite_link_create_input.additional_properties = d
        return invite_link_create_input

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
