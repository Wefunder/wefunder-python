from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.pitch_block_type import PitchBlockType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.pitch_block_links_item import PitchBlockLinksItem





T = TypeVar("T", bound="PitchBlock")



@_attrs_define
class PitchBlock:
    """ One block of the story. `type` says which of the other keys are present.

        Attributes:
            type_ (PitchBlockType | Unset):
            level (int | Unset): Heading level 1–6 (`heading` only).
            text (str | Unset): Plain text (`heading`, `paragraph`, and `footnote`). A footnote reference in running text
                appears as `[n]`.
            number (int | Unset): The footnote's number, matching its `[n]` reference (`footnote` only).
            ordered (bool | Unset): Numbered list (`list` only).
            start (int | Unset): First number of an ordered list that resumes after an image or nested list split it (`list`
                only, when above 1).
            items (list[str] | Unset): Plain-text list items (`list` only).
            links (list[PitchBlockLinksItem] | Unset): The hyperlinks in this block's text, in order, as the page links them
                (`paragraph`, `heading`, `list`; absent when there are none). Anchor text stays inline in `text` / `items`.
            url (str | Unset): Absolute URL of the image or video (`image` and `video`).
            link (str | Unset): Where the page links this image or video to, when it is wrapped in a hyperlink (`image` and
                `video`; absent otherwise).
            alt (None | str | Unset): The image's alt text; almost always null on Wefunder pitches (`image` only).
            filename (None | str | Unset): The image file's name, often the only hint at its content, e.g.
                `Tier_3_Final.png` (`image` only).
            provider (str | Unset): `youtube`, `vimeo`, `wistia`, `loom`, `upload` (hosted by Wefunder), or `other` (`video`
                only).
     """

    type_: PitchBlockType | Unset = UNSET
    level: int | Unset = UNSET
    text: str | Unset = UNSET
    number: int | Unset = UNSET
    ordered: bool | Unset = UNSET
    start: int | Unset = UNSET
    items: list[str] | Unset = UNSET
    links: list[PitchBlockLinksItem] | Unset = UNSET
    url: str | Unset = UNSET
    link: str | Unset = UNSET
    alt: None | str | Unset = UNSET
    filename: None | str | Unset = UNSET
    provider: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.pitch_block_links_item import PitchBlockLinksItem # noqa: PLC0415
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        level = self.level

        text = self.text

        number = self.number

        ordered = self.ordered

        start = self.start

        items: list[str] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = self.items



        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)



        url = self.url

        link = self.link

        alt: None | str | Unset
        if isinstance(self.alt, Unset):
            alt = UNSET
        else:
            alt = self.alt

        filename: None | str | Unset
        if isinstance(self.filename, Unset):
            filename = UNSET
        else:
            filename = self.filename

        provider = self.provider


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if level is not UNSET:
            field_dict["level"] = level
        if text is not UNSET:
            field_dict["text"] = text
        if number is not UNSET:
            field_dict["number"] = number
        if ordered is not UNSET:
            field_dict["ordered"] = ordered
        if start is not UNSET:
            field_dict["start"] = start
        if items is not UNSET:
            field_dict["items"] = items
        if links is not UNSET:
            field_dict["links"] = links
        if url is not UNSET:
            field_dict["url"] = url
        if link is not UNSET:
            field_dict["link"] = link
        if alt is not UNSET:
            field_dict["alt"] = alt
        if filename is not UNSET:
            field_dict["filename"] = filename
        if provider is not UNSET:
            field_dict["provider"] = provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pitch_block_links_item import PitchBlockLinksItem # noqa: PLC0415
        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: PitchBlockType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PitchBlockType(_type_)




        level = d.pop("level", UNSET)

        text = d.pop("text", UNSET)

        number = d.pop("number", UNSET)

        ordered = d.pop("ordered", UNSET)

        start = d.pop("start", UNSET)

        items = cast(list[str], d.pop("items", UNSET))


        _links = d.pop("links", UNSET)
        links: list[PitchBlockLinksItem] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = PitchBlockLinksItem.from_dict(links_item_data)



                links.append(links_item)


        url = d.pop("url", UNSET)

        link = d.pop("link", UNSET)

        def _parse_alt(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        alt = _parse_alt(d.pop("alt", UNSET))


        def _parse_filename(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        filename = _parse_filename(d.pop("filename", UNSET))


        provider = d.pop("provider", UNSET)

        pitch_block = cls(
            type_=type_,
            level=level,
            text=text,
            number=number,
            ordered=ordered,
            start=start,
            items=items,
            links=links,
            url=url,
            link=link,
            alt=alt,
            filename=filename,
            provider=provider,
        )


        pitch_block.additional_properties = d
        return pitch_block

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
