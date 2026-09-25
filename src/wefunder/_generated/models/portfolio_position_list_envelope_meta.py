from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="PortfolioPositionListEnvelopeMeta")



@_attrs_define
class PortfolioPositionListEnvelopeMeta:
    """ 
        Attributes:
            has_more (bool | Unset):
            page_count (int | Unset):
            next_cursor (int | None | Unset): Pass as `cursor` to fetch the next page. Absent on the last page.
     """

    has_more: bool | Unset = UNSET
    page_count: int | Unset = UNSET
    next_cursor: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_more = self.has_more

        page_count = self.page_count

        next_cursor: int | None | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_more = d.pop("has_more", UNSET)

        page_count = d.pop("page_count", UNSET)

        def _parse_next_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))


        portfolio_position_list_envelope_meta = cls(
            has_more=has_more,
            page_count=page_count,
            next_cursor=next_cursor,
        )


        portfolio_position_list_envelope_meta.additional_properties = d
        return portfolio_position_list_envelope_meta

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
