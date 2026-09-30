from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ReorderSyndicateMembersBody")


@_attrs_define
class ReorderSyndicateMembersBody:
    """
    Attributes:
        member_ids (list[str]): Member ids as returned by the list endpoint (`mem_…`), in the desired display order.
            Unknown ids return 404 and change nothing. Example: ['mem_8Kd0aB3xQ9k2', 'mem_vF8mNp1zT5wY',
            'mem_2Lq7cR4sX0bE'].
    """

    member_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_ids = self.member_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "member_ids": member_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        member_ids = cast(list[str], d.pop("member_ids"))

        reorder_syndicate_members_body = cls(
            member_ids=member_ids,
        )

        reorder_syndicate_members_body.additional_properties = d
        return reorder_syndicate_members_body

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
