from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_syndicate_join_session_body_join_session_display import (
    CreateSyndicateJoinSessionBodyJoinSessionDisplay,
)
from ..models.create_syndicate_join_session_body_join_session_mode import CreateSyndicateJoinSessionBodyJoinSessionMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateSyndicateJoinSessionBodyJoinSession")


@_attrs_define
class CreateSyndicateJoinSessionBodyJoinSession:
    """
    Attributes:
        email (str):  Example: jane@example.com.
        name (str | Unset):  Example: Jane Smith.
        mode (CreateSyndicateJoinSessionBodyJoinSessionMode | Unset):  Default:
            CreateSyndicateJoinSessionBodyJoinSessionMode.HOSTED.
        display (CreateSyndicateJoinSessionBodyJoinSessionDisplay | Unset):
        require_approval (bool | Unset): Whether the resulting membership needs manager approval before it is joined.
        success_url (str | Unset): HTTPS URL to send the recipient to after they finish.
        cancel_url (str | Unset): HTTPS URL to send the recipient to if they cancel.
    """

    email: str
    name: str | Unset = UNSET
    mode: CreateSyndicateJoinSessionBodyJoinSessionMode | Unset = CreateSyndicateJoinSessionBodyJoinSessionMode.HOSTED
    display: CreateSyndicateJoinSessionBodyJoinSessionDisplay | Unset = UNSET
    require_approval: bool | Unset = UNSET
    success_url: str | Unset = UNSET
    cancel_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        name = self.name

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        display: str | Unset = UNSET
        if not isinstance(self.display, Unset):
            display = self.display.value

        require_approval = self.require_approval

        success_url = self.success_url

        cancel_url = self.cancel_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if mode is not UNSET:
            field_dict["mode"] = mode
        if display is not UNSET:
            field_dict["display"] = display
        if require_approval is not UNSET:
            field_dict["require_approval"] = require_approval
        if success_url is not UNSET:
            field_dict["success_url"] = success_url
        if cancel_url is not UNSET:
            field_dict["cancel_url"] = cancel_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email")

        name = d.pop("name", UNSET)

        _mode = d.pop("mode", UNSET)
        mode: CreateSyndicateJoinSessionBodyJoinSessionMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CreateSyndicateJoinSessionBodyJoinSessionMode(_mode)

        _display = d.pop("display", UNSET)
        display: CreateSyndicateJoinSessionBodyJoinSessionDisplay | Unset
        if isinstance(_display, Unset):
            display = UNSET
        else:
            display = CreateSyndicateJoinSessionBodyJoinSessionDisplay(_display)

        require_approval = d.pop("require_approval", UNSET)

        success_url = d.pop("success_url", UNSET)

        cancel_url = d.pop("cancel_url", UNSET)

        create_syndicate_join_session_body_join_session = cls(
            email=email,
            name=name,
            mode=mode,
            display=display,
            require_approval=require_approval,
            success_url=success_url,
            cancel_url=cancel_url,
        )

        create_syndicate_join_session_body_join_session.additional_properties = d
        return create_syndicate_join_session_body_join_session

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
