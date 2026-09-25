from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InviteLinkUpdateInput")


@_attrs_define
class InviteLinkUpdateInput:
    """Only link terms are mutable; recipient identity, `reuse`, and the URL token cannot change. Other fields are ignored.

    Attributes:
        allocation_cents (int | None | Unset):  Example: 5000000.
        max_uses (int | None | Unset): Rejected for per-person invites and when set below the current `uses_count`.
            Example: 50.
    """

    allocation_cents: int | None | Unset = UNSET
    max_uses: int | None | Unset = UNSET
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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if allocation_cents is not UNSET:
            field_dict["allocation_cents"] = allocation_cents
        if max_uses is not UNSET:
            field_dict["max_uses"] = max_uses

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

        invite_link_update_input = cls(
            allocation_cents=allocation_cents,
            max_uses=max_uses,
        )

        invite_link_update_input.additional_properties = d
        return invite_link_update_input

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
