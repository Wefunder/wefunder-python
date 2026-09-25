from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.offering_list_envelope_meta_filters import OfferingListEnvelopeMetaFilters





T = TypeVar("T", bound="OfferingListEnvelopeMeta")



@_attrs_define
class OfferingListEnvelopeMeta:
    """ 
        Attributes:
            total_count (int | Unset): Total number of offerings across all pages. Example: 119.
            page_count (int | Unset): Number of offerings on this page (at most 25). Example: 25.
            has_more (bool | Unset):  Example: True.
            sort (str | Unset): The sort applied to this response. Example: most_raised.
            filters (OfferingListEnvelopeMetaFilters | Unset): The filters applied to this response (validated values),
                empty when none. Example: {'security': 'safe', 'testing_the_waters': False}.
            next_cursor (int | None | Unset): Opaque pagination cursor — pass as `cursor` to fetch the next page. Present
                only when `has_more` is true. Example: 25.
     """

    total_count: int | Unset = UNSET
    page_count: int | Unset = UNSET
    has_more: bool | Unset = UNSET
    sort: str | Unset = UNSET
    filters: OfferingListEnvelopeMetaFilters | Unset = UNSET
    next_cursor: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.offering_list_envelope_meta_filters import OfferingListEnvelopeMetaFilters # noqa: PLC0415
        total_count = self.total_count

        page_count = self.page_count

        has_more = self.has_more

        sort = self.sort

        filters: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filters, Unset):
            filters = self.filters.to_dict()

        next_cursor: int | None | Unset
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_count is not UNSET:
            field_dict["total_count"] = total_count
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if sort is not UNSET:
            field_dict["sort"] = sort
        if filters is not UNSET:
            field_dict["filters"] = filters
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.offering_list_envelope_meta_filters import OfferingListEnvelopeMetaFilters # noqa: PLC0415
        d = dict(src_dict)
        total_count = d.pop("total_count", UNSET)

        page_count = d.pop("page_count", UNSET)

        has_more = d.pop("has_more", UNSET)

        sort = d.pop("sort", UNSET)

        _filters = d.pop("filters", UNSET)
        filters: OfferingListEnvelopeMetaFilters | Unset
        if isinstance(_filters,  Unset):
            filters = UNSET
        else:
            filters = OfferingListEnvelopeMetaFilters.from_dict(_filters)




        def _parse_next_cursor(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor", UNSET))


        offering_list_envelope_meta = cls(
            total_count=total_count,
            page_count=page_count,
            has_more=has_more,
            sort=sort,
            filters=filters,
            next_cursor=next_cursor,
        )


        offering_list_envelope_meta.additional_properties = d
        return offering_list_envelope_meta

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
