from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.portfolio_summary_envelope_data_attributes_position_counts import (
        PortfolioSummaryEnvelopeDataAttributesPositionCounts,
    )


T = TypeVar("T", bound="PortfolioSummaryEnvelopeDataAttributes")


@_attrs_define
class PortfolioSummaryEnvelopeDataAttributes:
    """
    Attributes:
        currency (str | Unset):  Example: usd.
        total_cost_basis_cents (int | Unset):
        total_current_value_cents (int | Unset):
        total_unrealized_gain_cents (int | Unset):
        total_realized_gain_cents (int | Unset):
        return_multiple (None | str | Unset):  Example: 1.3107.
        position_counts (PortfolioSummaryEnvelopeDataAttributesPositionCounts | Unset): Distinct offerings per status.
        as_of (datetime.datetime | None | Unset):
    """

    currency: str | Unset = UNSET
    total_cost_basis_cents: int | Unset = UNSET
    total_current_value_cents: int | Unset = UNSET
    total_unrealized_gain_cents: int | Unset = UNSET
    total_realized_gain_cents: int | Unset = UNSET
    return_multiple: None | str | Unset = UNSET
    position_counts: PortfolioSummaryEnvelopeDataAttributesPositionCounts | Unset = UNSET
    as_of: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        total_cost_basis_cents = self.total_cost_basis_cents

        total_current_value_cents = self.total_current_value_cents

        total_unrealized_gain_cents = self.total_unrealized_gain_cents

        total_realized_gain_cents = self.total_realized_gain_cents

        return_multiple: None | str | Unset
        if isinstance(self.return_multiple, Unset):
            return_multiple = UNSET
        else:
            return_multiple = self.return_multiple

        position_counts: dict[str, Any] | Unset = UNSET
        if not isinstance(self.position_counts, Unset):
            position_counts = self.position_counts.to_dict()

        as_of: None | str | Unset
        if isinstance(self.as_of, Unset):
            as_of = UNSET
        elif isinstance(self.as_of, datetime.datetime):
            as_of = self.as_of.isoformat()
        else:
            as_of = self.as_of

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if total_cost_basis_cents is not UNSET:
            field_dict["total_cost_basis_cents"] = total_cost_basis_cents
        if total_current_value_cents is not UNSET:
            field_dict["total_current_value_cents"] = total_current_value_cents
        if total_unrealized_gain_cents is not UNSET:
            field_dict["total_unrealized_gain_cents"] = total_unrealized_gain_cents
        if total_realized_gain_cents is not UNSET:
            field_dict["total_realized_gain_cents"] = total_realized_gain_cents
        if return_multiple is not UNSET:
            field_dict["return_multiple"] = return_multiple
        if position_counts is not UNSET:
            field_dict["position_counts"] = position_counts
        if as_of is not UNSET:
            field_dict["as_of"] = as_of

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.portfolio_summary_envelope_data_attributes_position_counts import (
            PortfolioSummaryEnvelopeDataAttributesPositionCounts,  # noqa: PLC0415
        )

        d = dict(src_dict)
        currency = d.pop("currency", UNSET)

        total_cost_basis_cents = d.pop("total_cost_basis_cents", UNSET)

        total_current_value_cents = d.pop("total_current_value_cents", UNSET)

        total_unrealized_gain_cents = d.pop("total_unrealized_gain_cents", UNSET)

        total_realized_gain_cents = d.pop("total_realized_gain_cents", UNSET)

        def _parse_return_multiple(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        return_multiple = _parse_return_multiple(d.pop("return_multiple", UNSET))

        _position_counts = d.pop("position_counts", UNSET)
        position_counts: PortfolioSummaryEnvelopeDataAttributesPositionCounts | Unset
        if isinstance(_position_counts, Unset):
            position_counts = UNSET
        else:
            position_counts = PortfolioSummaryEnvelopeDataAttributesPositionCounts.from_dict(_position_counts)

        def _parse_as_of(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                as_of_type_0 = datetime.datetime.fromisoformat(data)

                return as_of_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        as_of = _parse_as_of(d.pop("as_of", UNSET))

        portfolio_summary_envelope_data_attributes = cls(
            currency=currency,
            total_cost_basis_cents=total_cost_basis_cents,
            total_current_value_cents=total_current_value_cents,
            total_unrealized_gain_cents=total_unrealized_gain_cents,
            total_realized_gain_cents=total_realized_gain_cents,
            return_multiple=return_multiple,
            position_counts=position_counts,
            as_of=as_of,
        )

        portfolio_summary_envelope_data_attributes.additional_properties = d
        return portfolio_summary_envelope_data_attributes

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
