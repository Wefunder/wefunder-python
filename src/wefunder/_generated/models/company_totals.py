from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CompanyTotals")



@_attrs_define
class CompanyTotals:
    """ 
        Attributes:
            raised_on_wefunder_all_time (None | str | Unset): Sum of `wefunder_rounds[].amount_raised` — everything this
                company has raised on Wefunder that the viewer may see. The lifetime figure.
            profile_total_raised (None | str | Unset): The number on the company page's ticker bar — the current raise plus
                the past rounds the page folds in (which may include founder-reported off-platform rounds and exclude older
                Wefunder rounds).
            profile_reported_off_platform (None | str | Unset): The founder-reported off-platform portion of
                `profile_total_raised`.
            profile_includes_past_rounds (bool | None | Unset): Whether the page's ticker currently folds past rounds into
                its total. Null when the viewer may see no round (no ticker to read).
     """

    raised_on_wefunder_all_time: None | str | Unset = UNSET
    profile_total_raised: None | str | Unset = UNSET
    profile_reported_off_platform: None | str | Unset = UNSET
    profile_includes_past_rounds: bool | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        raised_on_wefunder_all_time: None | str | Unset
        if isinstance(self.raised_on_wefunder_all_time, Unset):
            raised_on_wefunder_all_time = UNSET
        else:
            raised_on_wefunder_all_time = self.raised_on_wefunder_all_time

        profile_total_raised: None | str | Unset
        if isinstance(self.profile_total_raised, Unset):
            profile_total_raised = UNSET
        else:
            profile_total_raised = self.profile_total_raised

        profile_reported_off_platform: None | str | Unset
        if isinstance(self.profile_reported_off_platform, Unset):
            profile_reported_off_platform = UNSET
        else:
            profile_reported_off_platform = self.profile_reported_off_platform

        profile_includes_past_rounds: bool | None | Unset
        if isinstance(self.profile_includes_past_rounds, Unset):
            profile_includes_past_rounds = UNSET
        else:
            profile_includes_past_rounds = self.profile_includes_past_rounds


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if raised_on_wefunder_all_time is not UNSET:
            field_dict["raised_on_wefunder_all_time"] = raised_on_wefunder_all_time
        if profile_total_raised is not UNSET:
            field_dict["profile_total_raised"] = profile_total_raised
        if profile_reported_off_platform is not UNSET:
            field_dict["profile_reported_off_platform"] = profile_reported_off_platform
        if profile_includes_past_rounds is not UNSET:
            field_dict["profile_includes_past_rounds"] = profile_includes_past_rounds

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_raised_on_wefunder_all_time(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raised_on_wefunder_all_time = _parse_raised_on_wefunder_all_time(d.pop("raised_on_wefunder_all_time", UNSET))


        def _parse_profile_total_raised(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_total_raised = _parse_profile_total_raised(d.pop("profile_total_raised", UNSET))


        def _parse_profile_reported_off_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        profile_reported_off_platform = _parse_profile_reported_off_platform(d.pop("profile_reported_off_platform", UNSET))


        def _parse_profile_includes_past_rounds(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        profile_includes_past_rounds = _parse_profile_includes_past_rounds(d.pop("profile_includes_past_rounds", UNSET))


        company_totals = cls(
            raised_on_wefunder_all_time=raised_on_wefunder_all_time,
            profile_total_raised=profile_total_raised,
            profile_reported_off_platform=profile_reported_off_platform,
            profile_includes_past_rounds=profile_includes_past_rounds,
        )


        company_totals.additional_properties = d
        return company_totals

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
