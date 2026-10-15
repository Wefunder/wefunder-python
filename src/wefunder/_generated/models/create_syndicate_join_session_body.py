from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_syndicate_join_session_body_join_session import CreateSyndicateJoinSessionBodyJoinSession


T = TypeVar("T", bound="CreateSyndicateJoinSessionBody")


@_attrs_define
class CreateSyndicateJoinSessionBody:
    """
    Attributes:
        join_session (CreateSyndicateJoinSessionBodyJoinSession):
    """

    join_session: CreateSyndicateJoinSessionBodyJoinSession
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        join_session = self.join_session.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "join_session": join_session,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_syndicate_join_session_body_join_session import (
            CreateSyndicateJoinSessionBodyJoinSession,  # noqa: PLC0415
        )

        d = dict(src_dict)
        join_session = CreateSyndicateJoinSessionBodyJoinSession.from_dict(d.pop("join_session"))

        create_syndicate_join_session_body = cls(
            join_session=join_session,
        )

        create_syndicate_join_session_body.additional_properties = d
        return create_syndicate_join_session_body

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
