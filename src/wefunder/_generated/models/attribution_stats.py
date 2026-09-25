from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.attribution_stats_by_campaign_item import AttributionStatsByCampaignItem
  from ..models.attribution_stats_by_source_item import AttributionStatsBySourceItem
  from ..models.attribution_stats_period import AttributionStatsPeriod
  from ..models.attribution_stats_quality_breakdown import AttributionStatsQualityBreakdown
  from ..models.attribution_stats_totals import AttributionStatsTotals





T = TypeVar("T", bound="AttributionStats")



@_attrs_define
class AttributionStats:
    """ Aggregate attribution statistics for a campaign

        Attributes:
            campaign_id (int | Unset):  Example: 789.
            period (AttributionStatsPeriod | Unset):
            totals (AttributionStatsTotals | Unset):
            quality_breakdown (AttributionStatsQualityBreakdown | Unset): Attribution quality metrics
            by_source (list[AttributionStatsBySourceItem] | Unset): Breakdown by UTM source
            by_campaign (list[AttributionStatsByCampaignItem] | Unset): Breakdown by UTM campaign
     """

    campaign_id: int | Unset = UNSET
    period: AttributionStatsPeriod | Unset = UNSET
    totals: AttributionStatsTotals | Unset = UNSET
    quality_breakdown: AttributionStatsQualityBreakdown | Unset = UNSET
    by_source: list[AttributionStatsBySourceItem] | Unset = UNSET
    by_campaign: list[AttributionStatsByCampaignItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.attribution_stats_by_campaign_item import AttributionStatsByCampaignItem # noqa: PLC0415
        from ..models.attribution_stats_by_source_item import AttributionStatsBySourceItem # noqa: PLC0415
        from ..models.attribution_stats_period import AttributionStatsPeriod # noqa: PLC0415
        from ..models.attribution_stats_quality_breakdown import AttributionStatsQualityBreakdown # noqa: PLC0415
        from ..models.attribution_stats_totals import AttributionStatsTotals # noqa: PLC0415
        campaign_id = self.campaign_id

        period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.period, Unset):
            period = self.period.to_dict()

        totals: dict[str, Any] | Unset = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        quality_breakdown: dict[str, Any] | Unset = UNSET
        if not isinstance(self.quality_breakdown, Unset):
            quality_breakdown = self.quality_breakdown.to_dict()

        by_source: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_source, Unset):
            by_source = []
            for by_source_item_data in self.by_source:
                by_source_item = by_source_item_data.to_dict()
                by_source.append(by_source_item)



        by_campaign: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.by_campaign, Unset):
            by_campaign = []
            for by_campaign_item_data in self.by_campaign:
                by_campaign_item = by_campaign_item_data.to_dict()
                by_campaign.append(by_campaign_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if campaign_id is not UNSET:
            field_dict["campaign_id"] = campaign_id
        if period is not UNSET:
            field_dict["period"] = period
        if totals is not UNSET:
            field_dict["totals"] = totals
        if quality_breakdown is not UNSET:
            field_dict["quality_breakdown"] = quality_breakdown
        if by_source is not UNSET:
            field_dict["by_source"] = by_source
        if by_campaign is not UNSET:
            field_dict["by_campaign"] = by_campaign

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribution_stats_by_campaign_item import AttributionStatsByCampaignItem # noqa: PLC0415
        from ..models.attribution_stats_by_source_item import AttributionStatsBySourceItem # noqa: PLC0415
        from ..models.attribution_stats_period import AttributionStatsPeriod # noqa: PLC0415
        from ..models.attribution_stats_quality_breakdown import AttributionStatsQualityBreakdown # noqa: PLC0415
        from ..models.attribution_stats_totals import AttributionStatsTotals # noqa: PLC0415
        d = dict(src_dict)
        campaign_id = d.pop("campaign_id", UNSET)

        _period = d.pop("period", UNSET)
        period: AttributionStatsPeriod | Unset
        if isinstance(_period,  Unset):
            period = UNSET
        else:
            period = AttributionStatsPeriod.from_dict(_period)




        _totals = d.pop("totals", UNSET)
        totals: AttributionStatsTotals | Unset
        if isinstance(_totals,  Unset):
            totals = UNSET
        else:
            totals = AttributionStatsTotals.from_dict(_totals)




        _quality_breakdown = d.pop("quality_breakdown", UNSET)
        quality_breakdown: AttributionStatsQualityBreakdown | Unset
        if isinstance(_quality_breakdown,  Unset):
            quality_breakdown = UNSET
        else:
            quality_breakdown = AttributionStatsQualityBreakdown.from_dict(_quality_breakdown)




        _by_source = d.pop("by_source", UNSET)
        by_source: list[AttributionStatsBySourceItem] | Unset = UNSET
        if _by_source is not UNSET:
            by_source = []
            for by_source_item_data in _by_source:
                by_source_item = AttributionStatsBySourceItem.from_dict(by_source_item_data)



                by_source.append(by_source_item)


        _by_campaign = d.pop("by_campaign", UNSET)
        by_campaign: list[AttributionStatsByCampaignItem] | Unset = UNSET
        if _by_campaign is not UNSET:
            by_campaign = []
            for by_campaign_item_data in _by_campaign:
                by_campaign_item = AttributionStatsByCampaignItem.from_dict(by_campaign_item_data)



                by_campaign.append(by_campaign_item)


        attribution_stats = cls(
            campaign_id=campaign_id,
            period=period,
            totals=totals,
            quality_breakdown=quality_breakdown,
            by_source=by_source,
            by_campaign=by_campaign,
        )


        attribution_stats.additional_properties = d
        return attribution_stats

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
