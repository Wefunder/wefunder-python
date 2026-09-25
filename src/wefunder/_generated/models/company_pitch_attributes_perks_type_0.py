from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.perk_tier import PerkTier


T = TypeVar("T", bound="CompanyPitchAttributesPerksType0")


@_attrs_define
class CompanyPitchAttributesPerksType0:
    """The perk tiers the page shows; null when the viewer may see no round.

    Attributes:
        offering_id (None | str | Unset): The round these perks belong to (`ofr_...`) when it is the round the page
            shows. Null when the sidebar reads a round the viewer cannot resolve yet (a Testing-the-Waters page shows the
            perks of the round it converts into, which is still being set up).
        currency (str | Unset): ISO 4217 code the tier amounts are denominated in, e.g. `USD` or `EUR`.
        described_in_pitch (bool | Unset): Heuristic. True when the tiers are a placeholder ("See investor overview
            page", or one identical short sentence on every tier) and the real perks are in the story, usually as images.
        tiers (list[PerkTier] | Unset):
    """

    offering_id: None | str | Unset = UNSET
    currency: str | Unset = UNSET
    described_in_pitch: bool | Unset = UNSET
    tiers: list[PerkTier] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offering_id: None | str | Unset
        if isinstance(self.offering_id, Unset):
            offering_id = UNSET
        else:
            offering_id = self.offering_id

        currency = self.currency

        described_in_pitch = self.described_in_pitch

        tiers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tiers, Unset):
            tiers = []
            for tiers_item_data in self.tiers:
                tiers_item = tiers_item_data.to_dict()
                tiers.append(tiers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if currency is not UNSET:
            field_dict["currency"] = currency
        if described_in_pitch is not UNSET:
            field_dict["described_in_pitch"] = described_in_pitch
        if tiers is not UNSET:
            field_dict["tiers"] = tiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.perk_tier import PerkTier  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_offering_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        offering_id = _parse_offering_id(d.pop("offering_id", UNSET))

        currency = d.pop("currency", UNSET)

        described_in_pitch = d.pop("described_in_pitch", UNSET)

        _tiers = d.pop("tiers", UNSET)
        tiers: list[PerkTier] | Unset = UNSET
        if _tiers is not UNSET:
            tiers = []
            for tiers_item_data in _tiers:
                tiers_item = PerkTier.from_dict(tiers_item_data)

                tiers.append(tiers_item)

        company_pitch_attributes_perks_type_0 = cls(
            offering_id=offering_id,
            currency=currency,
            described_in_pitch=described_in_pitch,
            tiers=tiers,
        )

        company_pitch_attributes_perks_type_0.additional_properties = d
        return company_pitch_attributes_perks_type_0

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
