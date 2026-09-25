from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.anonymized_attribution_attribution_quality_score import AnonymizedAttributionAttributionQualityScore
from ..models.anonymized_attribution_attribution_time_to_invest_bucket import (
    AnonymizedAttributionAttributionTimeToInvestBucket,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="AnonymizedAttributionAttribution")


@_attrs_define
class AnonymizedAttributionAttribution:
    """UTM attribution data

    Attributes:
        utm_source (str | Unset):  Example: GoogleAds.
        utm_campaign (str | Unset):  Example: winter_2025.
        utm_medium (None | str | Unset):  Example: cpc.
        utm_content (None | str | Unset):  Example: video_ad_v2.
        clicked_at (datetime.datetime | Unset): When the UTM link was clicked Example: 2025-02-15T14:15:00Z.
        time_to_invest_bucket (AnonymizedAttributionAttributionTimeToInvestBucket | Unset): Time from click to
            investment Example: direct.
        quality_score (AnonymizedAttributionAttributionQualityScore | Unset): Attribution quality assessment Example:
            high.
        competing_sources (int | Unset): Number of other UTM sources in the attribution window Example: 0.
    """

    utm_source: str | Unset = UNSET
    utm_campaign: str | Unset = UNSET
    utm_medium: None | str | Unset = UNSET
    utm_content: None | str | Unset = UNSET
    clicked_at: datetime.datetime | Unset = UNSET
    time_to_invest_bucket: AnonymizedAttributionAttributionTimeToInvestBucket | Unset = UNSET
    quality_score: AnonymizedAttributionAttributionQualityScore | Unset = UNSET
    competing_sources: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        utm_source = self.utm_source

        utm_campaign = self.utm_campaign

        utm_medium: None | str | Unset
        if isinstance(self.utm_medium, Unset):
            utm_medium = UNSET
        else:
            utm_medium = self.utm_medium

        utm_content: None | str | Unset
        if isinstance(self.utm_content, Unset):
            utm_content = UNSET
        else:
            utm_content = self.utm_content

        clicked_at: str | Unset = UNSET
        if not isinstance(self.clicked_at, Unset):
            clicked_at = self.clicked_at.isoformat()

        time_to_invest_bucket: str | Unset = UNSET
        if not isinstance(self.time_to_invest_bucket, Unset):
            time_to_invest_bucket = self.time_to_invest_bucket.value

        quality_score: str | Unset = UNSET
        if not isinstance(self.quality_score, Unset):
            quality_score = self.quality_score.value

        competing_sources = self.competing_sources

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if utm_source is not UNSET:
            field_dict["utm_source"] = utm_source
        if utm_campaign is not UNSET:
            field_dict["utm_campaign"] = utm_campaign
        if utm_medium is not UNSET:
            field_dict["utm_medium"] = utm_medium
        if utm_content is not UNSET:
            field_dict["utm_content"] = utm_content
        if clicked_at is not UNSET:
            field_dict["clicked_at"] = clicked_at
        if time_to_invest_bucket is not UNSET:
            field_dict["time_to_invest_bucket"] = time_to_invest_bucket
        if quality_score is not UNSET:
            field_dict["quality_score"] = quality_score
        if competing_sources is not UNSET:
            field_dict["competing_sources"] = competing_sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        utm_source = d.pop("utm_source", UNSET)

        utm_campaign = d.pop("utm_campaign", UNSET)

        def _parse_utm_medium(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_medium = _parse_utm_medium(d.pop("utm_medium", UNSET))

        def _parse_utm_content(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        utm_content = _parse_utm_content(d.pop("utm_content", UNSET))

        _clicked_at = d.pop("clicked_at", UNSET)
        clicked_at: datetime.datetime | Unset
        if isinstance(_clicked_at, Unset):
            clicked_at = UNSET
        else:
            clicked_at = datetime.datetime.fromisoformat(_clicked_at)

        _time_to_invest_bucket = d.pop("time_to_invest_bucket", UNSET)
        time_to_invest_bucket: AnonymizedAttributionAttributionTimeToInvestBucket | Unset
        if isinstance(_time_to_invest_bucket, Unset):
            time_to_invest_bucket = UNSET
        else:
            time_to_invest_bucket = AnonymizedAttributionAttributionTimeToInvestBucket(_time_to_invest_bucket)

        _quality_score = d.pop("quality_score", UNSET)
        quality_score: AnonymizedAttributionAttributionQualityScore | Unset
        if isinstance(_quality_score, Unset):
            quality_score = UNSET
        else:
            quality_score = AnonymizedAttributionAttributionQualityScore(_quality_score)

        competing_sources = d.pop("competing_sources", UNSET)

        anonymized_attribution_attribution = cls(
            utm_source=utm_source,
            utm_campaign=utm_campaign,
            utm_medium=utm_medium,
            utm_content=utm_content,
            clicked_at=clicked_at,
            time_to_invest_bucket=time_to_invest_bucket,
            quality_score=quality_score,
            competing_sources=competing_sources,
        )

        anonymized_attribution_attribution.additional_properties = d
        return anonymized_attribution_attribution

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
