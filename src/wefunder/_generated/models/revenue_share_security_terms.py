from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.revenue_share_security_terms_revenue_basis_type_1 import RevenueShareSecurityTermsRevenueBasisType1
from ..models.revenue_share_security_terms_revenue_basis_type_2_type_1 import (
    RevenueShareSecurityTermsRevenueBasisType2Type1,
)
from ..models.revenue_share_security_terms_revenue_basis_type_3_type_1 import (
    RevenueShareSecurityTermsRevenueBasisType3Type1,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RevenueShareSecurityTerms")


@_attrs_define
class RevenueShareSecurityTerms:
    """
    Attributes:
        revenue_share_percent (None | str | Unset): Share of revenue paid to investors each period, as a percentage.
            Example: 10.
        repayment_cap_multiple (None | str | Unset): Payments stop once investors have received this multiple of their
            investment. Example: 1.5.
        payment_period (None | str | Unset):  Example: quarterly.
        revenue_basis (None | RevenueShareSecurityTermsRevenueBasisType1 |
            RevenueShareSecurityTermsRevenueBasisType2Type1 | RevenueShareSecurityTermsRevenueBasisType3Type1 | Unset):
        secured (bool | Unset):
        guarantor (None | str | Unset):
    """

    revenue_share_percent: None | str | Unset = UNSET
    repayment_cap_multiple: None | str | Unset = UNSET
    payment_period: None | str | Unset = UNSET
    revenue_basis: (
        None
        | RevenueShareSecurityTermsRevenueBasisType1
        | RevenueShareSecurityTermsRevenueBasisType2Type1
        | RevenueShareSecurityTermsRevenueBasisType3Type1
        | Unset
    ) = UNSET
    secured: bool | Unset = UNSET
    guarantor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        revenue_share_percent: None | str | Unset
        if isinstance(self.revenue_share_percent, Unset):
            revenue_share_percent = UNSET
        else:
            revenue_share_percent = self.revenue_share_percent

        repayment_cap_multiple: None | str | Unset
        if isinstance(self.repayment_cap_multiple, Unset):
            repayment_cap_multiple = UNSET
        else:
            repayment_cap_multiple = self.repayment_cap_multiple

        payment_period: None | str | Unset
        if isinstance(self.payment_period, Unset):
            payment_period = UNSET
        else:
            payment_period = self.payment_period

        revenue_basis: None | str | Unset
        if isinstance(self.revenue_basis, Unset):
            revenue_basis = UNSET
        elif (
            isinstance(self.revenue_basis, RevenueShareSecurityTermsRevenueBasisType1)
            or isinstance(self.revenue_basis, RevenueShareSecurityTermsRevenueBasisType2Type1)
            or isinstance(self.revenue_basis, RevenueShareSecurityTermsRevenueBasisType3Type1)
        ):
            revenue_basis = self.revenue_basis.value
        else:
            revenue_basis = self.revenue_basis

        secured = self.secured

        guarantor: None | str | Unset
        if isinstance(self.guarantor, Unset):
            guarantor = UNSET
        else:
            guarantor = self.guarantor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revenue_share_percent is not UNSET:
            field_dict["revenue_share_percent"] = revenue_share_percent
        if repayment_cap_multiple is not UNSET:
            field_dict["repayment_cap_multiple"] = repayment_cap_multiple
        if payment_period is not UNSET:
            field_dict["payment_period"] = payment_period
        if revenue_basis is not UNSET:
            field_dict["revenue_basis"] = revenue_basis
        if secured is not UNSET:
            field_dict["secured"] = secured
        if guarantor is not UNSET:
            field_dict["guarantor"] = guarantor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_revenue_share_percent(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        revenue_share_percent = _parse_revenue_share_percent(d.pop("revenue_share_percent", UNSET))

        def _parse_repayment_cap_multiple(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        repayment_cap_multiple = _parse_repayment_cap_multiple(d.pop("repayment_cap_multiple", UNSET))

        def _parse_payment_period(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        payment_period = _parse_payment_period(d.pop("payment_period", UNSET))

        def _parse_revenue_basis(
            data: object,
        ) -> (
            None
            | RevenueShareSecurityTermsRevenueBasisType1
            | RevenueShareSecurityTermsRevenueBasisType2Type1
            | RevenueShareSecurityTermsRevenueBasisType3Type1
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revenue_basis_type_1 = RevenueShareSecurityTermsRevenueBasisType1(data)

                return revenue_basis_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revenue_basis_type_2_type_1 = RevenueShareSecurityTermsRevenueBasisType2Type1(data)

                return revenue_basis_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                revenue_basis_type_3_type_1 = RevenueShareSecurityTermsRevenueBasisType3Type1(data)

                return revenue_basis_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                None
                | RevenueShareSecurityTermsRevenueBasisType1
                | RevenueShareSecurityTermsRevenueBasisType2Type1
                | RevenueShareSecurityTermsRevenueBasisType3Type1
                | Unset,
                data,
            )

        revenue_basis = _parse_revenue_basis(d.pop("revenue_basis", UNSET))

        secured = d.pop("secured", UNSET)

        def _parse_guarantor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guarantor = _parse_guarantor(d.pop("guarantor", UNSET))

        revenue_share_security_terms = cls(
            revenue_share_percent=revenue_share_percent,
            repayment_cap_multiple=repayment_cap_multiple,
            payment_period=payment_period,
            revenue_basis=revenue_basis,
            secured=secured,
            guarantor=guarantor,
        )

        revenue_share_security_terms.additional_properties = d
        return revenue_share_security_terms

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
