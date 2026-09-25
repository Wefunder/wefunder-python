from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.company_pitch_attributes_authored_by import CompanyPitchAttributesAuthoredBy
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.company_pitch_attributes_perks_type_0 import CompanyPitchAttributesPerksType0
    from ..models.company_pitch_attributes_story import CompanyPitchAttributesStory


T = TypeVar("T", bound="CompanyPitchAttributes")


@_attrs_define
class CompanyPitchAttributes:
    """
    Attributes:
        offering_id (None | str | Unset): The round the page shows this viewer (`ofr_...`), whose perks these are; null
            when the viewer may see none.
        title (str | Unset): The heading the page puts over the story (the founder's own, or the default).
        url (None | str | Unset): The company's page on wefunder.com.
        authored_by (CompanyPitchAttributesAuthoredBy | Unset): `company`: the founder wrote the story. `wefunder`: a
            Wefunder-prepared deal memo the company did not participate in.
        disclaimer (None | str | Unset): The page's notice on a Wefunder-prepared deal memo; null when the company
            authored the story.
        story (CompanyPitchAttributesStory | Unset): The story in document order, as the page renders it. Empty `blocks`
            when the company has no story.
        perks (CompanyPitchAttributesPerksType0 | None | Unset): The perk tiers the page shows; null when the viewer may
            see no round.
    """

    offering_id: None | str | Unset = UNSET
    title: str | Unset = UNSET
    url: None | str | Unset = UNSET
    authored_by: CompanyPitchAttributesAuthoredBy | Unset = UNSET
    disclaimer: None | str | Unset = UNSET
    story: CompanyPitchAttributesStory | Unset = UNSET
    perks: CompanyPitchAttributesPerksType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.company_pitch_attributes_perks_type_0 import CompanyPitchAttributesPerksType0  # noqa: PLC0415

        offering_id: None | str | Unset
        if isinstance(self.offering_id, Unset):
            offering_id = UNSET
        else:
            offering_id = self.offering_id

        title = self.title

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        authored_by: str | Unset = UNSET
        if not isinstance(self.authored_by, Unset):
            authored_by = self.authored_by.value

        disclaimer: None | str | Unset
        if isinstance(self.disclaimer, Unset):
            disclaimer = UNSET
        else:
            disclaimer = self.disclaimer

        story: dict[str, Any] | Unset = UNSET
        if not isinstance(self.story, Unset):
            story = self.story.to_dict()

        perks: dict[str, Any] | None | Unset
        if isinstance(self.perks, Unset):
            perks = UNSET
        elif isinstance(self.perks, CompanyPitchAttributesPerksType0):
            perks = self.perks.to_dict()
        else:
            perks = self.perks

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if title is not UNSET:
            field_dict["title"] = title
        if url is not UNSET:
            field_dict["url"] = url
        if authored_by is not UNSET:
            field_dict["authored_by"] = authored_by
        if disclaimer is not UNSET:
            field_dict["disclaimer"] = disclaimer
        if story is not UNSET:
            field_dict["story"] = story
        if perks is not UNSET:
            field_dict["perks"] = perks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.company_pitch_attributes_perks_type_0 import CompanyPitchAttributesPerksType0  # noqa: PLC0415
        from ..models.company_pitch_attributes_story import CompanyPitchAttributesStory  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_offering_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        offering_id = _parse_offering_id(d.pop("offering_id", UNSET))

        title = d.pop("title", UNSET)

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        _authored_by = d.pop("authored_by", UNSET)
        authored_by: CompanyPitchAttributesAuthoredBy | Unset
        if isinstance(_authored_by, Unset):
            authored_by = UNSET
        else:
            authored_by = CompanyPitchAttributesAuthoredBy(_authored_by)

        def _parse_disclaimer(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        disclaimer = _parse_disclaimer(d.pop("disclaimer", UNSET))

        _story = d.pop("story", UNSET)
        story: CompanyPitchAttributesStory | Unset
        if isinstance(_story, Unset):
            story = UNSET
        else:
            story = CompanyPitchAttributesStory.from_dict(_story)

        def _parse_perks(data: object) -> CompanyPitchAttributesPerksType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                perks_type_0 = CompanyPitchAttributesPerksType0.from_dict(data)

                return perks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompanyPitchAttributesPerksType0 | None | Unset, data)

        perks = _parse_perks(d.pop("perks", UNSET))

        company_pitch_attributes = cls(
            offering_id=offering_id,
            title=title,
            url=url,
            authored_by=authored_by,
            disclaimer=disclaimer,
            story=story,
            perks=perks,
        )

        company_pitch_attributes.additional_properties = d
        return company_pitch_attributes

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
