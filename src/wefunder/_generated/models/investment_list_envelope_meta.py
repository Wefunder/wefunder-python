from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.investment_list_envelope_meta_mode import InvestmentListEnvelopeMetaMode
from ..types import UNSET, Unset
from typing import cast
import datetime






T = TypeVar("T", bound="InvestmentListEnvelopeMeta")



@_attrs_define
class InvestmentListEnvelopeMeta:
    """ 
        Attributes:
            mode (InvestmentListEnvelopeMetaMode | Unset): `bootstrap` for list pages, `delta` for sync pages (cursor or
                updated_since).
            has_more (bool | Unset):
            next_cursor (str | Unset): Always present. Pass it back as `cursor` on the next call, even when `has_more` is
                false.
            page_count (int | Unset):
            published_through (datetime.datetime | None | Unset): When the newest change this page can reflect was
                published. Records changed after this arrive on the next sync.
     """

    mode: InvestmentListEnvelopeMetaMode | Unset = UNSET
    has_more: bool | Unset = UNSET
    next_cursor: str | Unset = UNSET
    page_count: int | Unset = UNSET
    published_through: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value


        has_more = self.has_more

        next_cursor = self.next_cursor

        page_count = self.page_count

        published_through: None | str | Unset
        if isinstance(self.published_through, Unset):
            published_through = UNSET
        elif isinstance(self.published_through, datetime.datetime):
            published_through = self.published_through.isoformat()
        else:
            published_through = self.published_through


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if mode is not UNSET:
            field_dict["mode"] = mode
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if next_cursor is not UNSET:
            field_dict["next_cursor"] = next_cursor
        if page_count is not UNSET:
            field_dict["page_count"] = page_count
        if published_through is not UNSET:
            field_dict["published_through"] = published_through

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: InvestmentListEnvelopeMetaMode | Unset
        if isinstance(_mode,  Unset):
            mode = UNSET
        else:
            mode = InvestmentListEnvelopeMetaMode(_mode)




        has_more = d.pop("has_more", UNSET)

        next_cursor = d.pop("next_cursor", UNSET)

        page_count = d.pop("page_count", UNSET)

        def _parse_published_through(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_through_type_0 = datetime.datetime.fromisoformat(data)



                return published_through_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_through = _parse_published_through(d.pop("published_through", UNSET))


        investment_list_envelope_meta = cls(
            mode=mode,
            has_more=has_more,
            next_cursor=next_cursor,
            page_count=page_count,
            published_through=published_through,
        )


        investment_list_envelope_meta.additional_properties = d
        return investment_list_envelope_meta

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
