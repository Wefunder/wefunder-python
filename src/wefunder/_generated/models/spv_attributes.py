from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.spv_attributes_status import SpvAttributesStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spv_attributes_metadata import SpvAttributesMetadata
    from ..models.spv_attributes_target_company import SpvAttributesTargetCompany
    from ..models.spv_metrics import SpvMetrics
    from ..models.spv_terms import SpvTerms


T = TypeVar("T", bound="SpvAttributes")


@_attrs_define
class SpvAttributes:
    """
    Attributes:
        name (str | Unset):  Example: Acme Series A SPV.
        status (SpvAttributesStatus | Unset):  Example: open.
        series_name (str | Unset):  Example: Acme Series A SPV, a series of Wefunder LLC.
        invest_url (None | str | Unset):  Example: https://wefunder.com/invest/spv_abc123.
        target_company (SpvAttributesTargetCompany | Unset):
        terms (SpvTerms | Unset): Investment terms for an SPV.
        metrics (SpvMetrics | Unset):
        metadata (SpvAttributesMetadata | Unset):
        created_at (datetime.datetime | Unset):  Example: 2025-01-15T10:00:00Z.
        opened_at (datetime.datetime | None | Unset):
        closing_at (datetime.datetime | None | Unset):
        closed_at (datetime.datetime | None | Unset):
    """

    name: str | Unset = UNSET
    status: SpvAttributesStatus | Unset = UNSET
    series_name: str | Unset = UNSET
    invest_url: None | str | Unset = UNSET
    target_company: SpvAttributesTargetCompany | Unset = UNSET
    terms: SpvTerms | Unset = UNSET
    metrics: SpvMetrics | Unset = UNSET
    metadata: SpvAttributesMetadata | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    opened_at: datetime.datetime | None | Unset = UNSET
    closing_at: datetime.datetime | None | Unset = UNSET
    closed_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        series_name = self.series_name

        invest_url: None | str | Unset
        if isinstance(self.invest_url, Unset):
            invest_url = UNSET
        else:
            invest_url = self.invest_url

        target_company: dict[str, Any] | Unset = UNSET
        if not isinstance(self.target_company, Unset):
            target_company = self.target_company.to_dict()

        terms: dict[str, Any] | Unset = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics, Unset):
            metrics = self.metrics.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        opened_at: None | str | Unset
        if isinstance(self.opened_at, Unset):
            opened_at = UNSET
        elif isinstance(self.opened_at, datetime.datetime):
            opened_at = self.opened_at.isoformat()
        else:
            opened_at = self.opened_at

        closing_at: None | str | Unset
        if isinstance(self.closing_at, Unset):
            closing_at = UNSET
        elif isinstance(self.closing_at, datetime.datetime):
            closing_at = self.closing_at.isoformat()
        else:
            closing_at = self.closing_at

        closed_at: None | str | Unset
        if isinstance(self.closed_at, Unset):
            closed_at = UNSET
        elif isinstance(self.closed_at, datetime.datetime):
            closed_at = self.closed_at.isoformat()
        else:
            closed_at = self.closed_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status
        if series_name is not UNSET:
            field_dict["series_name"] = series_name
        if invest_url is not UNSET:
            field_dict["invest_url"] = invest_url
        if target_company is not UNSET:
            field_dict["target_company"] = target_company
        if terms is not UNSET:
            field_dict["terms"] = terms
        if metrics is not UNSET:
            field_dict["metrics"] = metrics
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if opened_at is not UNSET:
            field_dict["opened_at"] = opened_at
        if closing_at is not UNSET:
            field_dict["closing_at"] = closing_at
        if closed_at is not UNSET:
            field_dict["closed_at"] = closed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.spv_attributes_metadata import SpvAttributesMetadata  # noqa: PLC0415
        from ..models.spv_attributes_target_company import SpvAttributesTargetCompany  # noqa: PLC0415
        from ..models.spv_metrics import SpvMetrics  # noqa: PLC0415
        from ..models.spv_terms import SpvTerms  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: SpvAttributesStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SpvAttributesStatus(_status)

        series_name = d.pop("series_name", UNSET)

        def _parse_invest_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        invest_url = _parse_invest_url(d.pop("invest_url", UNSET))

        _target_company = d.pop("target_company", UNSET)
        target_company: SpvAttributesTargetCompany | Unset
        if isinstance(_target_company, Unset):
            target_company = UNSET
        else:
            target_company = SpvAttributesTargetCompany.from_dict(_target_company)

        _terms = d.pop("terms", UNSET)
        terms: SpvTerms | Unset
        if isinstance(_terms, Unset):
            terms = UNSET
        else:
            terms = SpvTerms.from_dict(_terms)

        _metrics = d.pop("metrics", UNSET)
        metrics: SpvMetrics | Unset
        if isinstance(_metrics, Unset):
            metrics = UNSET
        else:
            metrics = SpvMetrics.from_dict(_metrics)

        _metadata = d.pop("metadata", UNSET)
        metadata: SpvAttributesMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = SpvAttributesMetadata.from_dict(_metadata)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        def _parse_opened_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                opened_at_type_0 = datetime.datetime.fromisoformat(data)

                return opened_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        opened_at = _parse_opened_at(d.pop("opened_at", UNSET))

        def _parse_closing_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closing_at_type_0 = datetime.datetime.fromisoformat(data)

                return closing_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closing_at = _parse_closing_at(d.pop("closing_at", UNSET))

        def _parse_closed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                closed_at_type_0 = datetime.datetime.fromisoformat(data)

                return closed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        closed_at = _parse_closed_at(d.pop("closed_at", UNSET))

        spv_attributes = cls(
            name=name,
            status=status,
            series_name=series_name,
            invest_url=invest_url,
            target_company=target_company,
            terms=terms,
            metrics=metrics,
            metadata=metadata,
            created_at=created_at,
            opened_at=opened_at,
            closing_at=closing_at,
            closed_at=closed_at,
        )

        spv_attributes.additional_properties = d
        return spv_attributes

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
