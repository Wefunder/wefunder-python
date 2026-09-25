from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PaginationMeta")



@_attrs_define
class PaginationMeta:
    """ 
        Attributes:
            count (int | Unset):  Example: 25.
            has_more (bool | Unset):  Example: True.
            next_cursor (int | None | str | Unset): Opaque cursor — pass back as `cursor` for the next page. An integer id
                for
                id-paginated lists, an ISO 8601 timestamp for timestamp-paginated ones
                (`/activity`). Absent or null on the last page.
                 Example: 12345.
     """

    count: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    next_cursor: int | None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        count = self.count

        has_more = self.has_more

        next_cursor: int | None | str | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if count is not UNSET:
            field_dict["count"] = count
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        count = d.pop("count", UNSET)

        has_more = d.pop("has_more", UNSET)

        def _parse_next_cursor(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))


        pagination_meta = cls(
            count=count,
            has_more=has_more,
            next_cursor=next_cursor,
        )


        pagination_meta.additional_properties = d
        return pagination_meta

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
