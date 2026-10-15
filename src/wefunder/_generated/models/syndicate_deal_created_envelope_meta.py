from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.syndicate_deal_created_envelope_meta_target_company_type_0 import (
        SyndicateDealCreatedEnvelopeMetaTargetCompanyType0,
    )


T = TypeVar("T", bound="SyndicateDealCreatedEnvelopeMeta")


@_attrs_define
class SyndicateDealCreatedEnvelopeMeta:
    """
    Attributes:
        target_company (None | SyndicateDealCreatedEnvelopeMetaTargetCompanyType0 | Unset):
    """

    target_company: None | SyndicateDealCreatedEnvelopeMetaTargetCompanyType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.syndicate_deal_created_envelope_meta_target_company_type_0 import (
            SyndicateDealCreatedEnvelopeMetaTargetCompanyType0,  # noqa: PLC0415
        )

        target_company: dict[str, Any] | None | Unset
        if isinstance(self.target_company, Unset):
            target_company = UNSET
        elif isinstance(self.target_company, SyndicateDealCreatedEnvelopeMetaTargetCompanyType0):
            target_company = self.target_company.to_dict()
        else:
            target_company = self.target_company

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if target_company is not UNSET:
            field_dict["target_company"] = target_company

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.syndicate_deal_created_envelope_meta_target_company_type_0 import (
            SyndicateDealCreatedEnvelopeMetaTargetCompanyType0,  # noqa: PLC0415
        )

        d = dict(src_dict)

        def _parse_target_company(data: object) -> None | SyndicateDealCreatedEnvelopeMetaTargetCompanyType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_company_type_0 = SyndicateDealCreatedEnvelopeMetaTargetCompanyType0.from_dict(data)

                return target_company_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyndicateDealCreatedEnvelopeMetaTargetCompanyType0 | Unset, data)

        target_company = _parse_target_company(d.pop("target_company", UNSET))

        syndicate_deal_created_envelope_meta = cls(
            target_company=target_company,
        )

        syndicate_deal_created_envelope_meta.additional_properties = d
        return syndicate_deal_created_envelope_meta

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
