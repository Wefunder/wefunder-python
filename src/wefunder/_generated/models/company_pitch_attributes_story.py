from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pitch_block import PitchBlock


T = TypeVar("T", bound="CompanyPitchAttributesStory")


@_attrs_define
class CompanyPitchAttributesStory:
    """The story in document order, as the page renders it. Empty `blocks` when the company has no story.

    Attributes:
        blocks (list[PitchBlock] | Unset):
        image_count (int | Unset):
        video_count (int | Unset):
        inline_images_omitted (int | Unset): Images the page renders from an inline `data:` URL, which have no fetchable
            URL and are left out of `blocks`. Almost always 0.
        character_count (int | Unset): Characters of text across paragraph, heading, list, and footnote blocks.
    """

    blocks: list[PitchBlock] | Unset = UNSET
    image_count: int | Unset = UNSET
    video_count: int | Unset = UNSET
    inline_images_omitted: int | Unset = UNSET
    character_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blocks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = []
            for blocks_item_data in self.blocks:
                blocks_item = blocks_item_data.to_dict()
                blocks.append(blocks_item)

        image_count = self.image_count

        video_count = self.video_count

        inline_images_omitted = self.inline_images_omitted

        character_count = self.character_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if image_count is not UNSET:
            field_dict["image_count"] = image_count
        if video_count is not UNSET:
            field_dict["video_count"] = video_count
        if inline_images_omitted is not UNSET:
            field_dict["inline_images_omitted"] = inline_images_omitted
        if character_count is not UNSET:
            field_dict["character_count"] = character_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pitch_block import PitchBlock  # noqa: PLC0415

        d = dict(src_dict)
        _blocks = d.pop("blocks", UNSET)
        blocks: list[PitchBlock] | Unset = UNSET
        if _blocks is not UNSET:
            blocks = []
            for blocks_item_data in _blocks:
                blocks_item = PitchBlock.from_dict(blocks_item_data)

                blocks.append(blocks_item)

        image_count = d.pop("image_count", UNSET)

        video_count = d.pop("video_count", UNSET)

        inline_images_omitted = d.pop("inline_images_omitted", UNSET)

        character_count = d.pop("character_count", UNSET)

        company_pitch_attributes_story = cls(
            blocks=blocks,
            image_count=image_count,
            video_count=video_count,
            inline_images_omitted=inline_images_omitted,
            character_count=character_count,
        )

        company_pitch_attributes_story.additional_properties = d
        return company_pitch_attributes_story

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
