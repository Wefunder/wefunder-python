from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_referral_code_body_metadata import CreateReferralCodeBodyMetadata
    from ..models.referral_code_utm import ReferralCodeUtm


T = TypeVar("T", bound="CreateReferralCodeBody")


@_attrs_define
class CreateReferralCodeBody:
    """
    Attributes:
        label (str): Your name for the code, e.g. a campaign or newsletter issue. Example: October newsletter.
        company_id (str | Unset): Credit only investments in this company (`co_…`). Omit both `company_id` and
            `offering_id` for a code that credits any company. Fixed at creation.
             Example: co_7hQExampleCompany0001.
        offering_id (str | Unset): Credit only investments in this offering's company (`ofr_…`). The offering must
            be publicly visible. Fixed at creation.
             Example: ofr_7hQExampleOffering01.
        utm (ReferralCodeUtm | Unset): Optional UTM presets. On a visit that carries this code, each preset fills the
            matching
            `utm_*` field when the link leaves it blank; a value on the link always wins. Each value is
            at most 100 printable ASCII characters. `source` and `campaign` may not start with `wf_`.
        metadata (CreateReferralCodeBodyMetadata | Unset): Free-form metadata for your own use, at most 4 KB.
    """

    label: str
    company_id: str | Unset = UNSET
    offering_id: str | Unset = UNSET
    utm: ReferralCodeUtm | Unset = UNSET
    metadata: CreateReferralCodeBodyMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        company_id = self.company_id

        offering_id = self.offering_id

        utm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.utm, Unset):
            utm = self.utm.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if company_id is not UNSET:
            field_dict["company_id"] = company_id
        if offering_id is not UNSET:
            field_dict["offering_id"] = offering_id
        if utm is not UNSET:
            field_dict["utm"] = utm
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_referral_code_body_metadata import CreateReferralCodeBodyMetadata  # noqa: PLC0415
        from ..models.referral_code_utm import ReferralCodeUtm  # noqa: PLC0415

        d = dict(src_dict)
        label = d.pop("label")

        company_id = d.pop("company_id", UNSET)

        offering_id = d.pop("offering_id", UNSET)

        _utm = d.pop("utm", UNSET)
        utm: ReferralCodeUtm | Unset
        if isinstance(_utm, Unset):
            utm = UNSET
        else:
            utm = ReferralCodeUtm.from_dict(_utm)

        _metadata = d.pop("metadata", UNSET)
        metadata: CreateReferralCodeBodyMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateReferralCodeBodyMetadata.from_dict(_metadata)

        create_referral_code_body = cls(
            label=label,
            company_id=company_id,
            offering_id=offering_id,
            utm=utm,
            metadata=metadata,
        )

        create_referral_code_body.additional_properties = d
        return create_referral_code_body

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
