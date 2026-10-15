from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.referral_code_attributes_metadata import ReferralCodeAttributesMetadata
    from ..models.referral_code_attributes_target_type_0 import ReferralCodeAttributesTargetType0
    from ..models.referral_code_utm import ReferralCodeUtm
    from ..models.referral_code_visits import ReferralCodeVisits


T = TypeVar("T", bound="ReferralCodeAttributes")


@_attrs_define
class ReferralCodeAttributes:
    """
    Attributes:
        label (str | Unset):  Example: October newsletter.
        active (bool | Unset): A paused code is ignored on arrival; it still credits cookies set while it was active.
        target (None | ReferralCodeAttributesTargetType0 | Unset): The company or offering this code credits, or null
            for any company. If the target
            no longer exists, `id` is null and `unavailable` is true: the code credits nothing.
        utm (ReferralCodeUtm | Unset): Optional UTM presets. On a visit that carries this code, each preset fills the
            matching
            `utm_*` field when the link leaves it blank; a value on the link always wins. Each value is
            at most 100 printable ASCII characters. `source` and `campaign` may not start with `wf_`.
        metadata (ReferralCodeAttributesMetadata | Unset):
        link_parameter (str | Unset): The query parameter to append to any wefunder.com link. Example:
            wfr=ref_8f3ExampleReferral0000.
        stats (ReferralCodeVisits | Unset):
        created_at (datetime.datetime | Unset):  Example: 2026-10-13T17:30:00Z.
        updated_at (datetime.datetime | Unset):  Example: 2026-10-13T17:30:00Z.
    """

    label: str | Unset = UNSET
    active: bool | Unset = UNSET
    target: None | ReferralCodeAttributesTargetType0 | Unset = UNSET
    utm: ReferralCodeUtm | Unset = UNSET
    metadata: ReferralCodeAttributesMetadata | Unset = UNSET
    link_parameter: str | Unset = UNSET
    stats: ReferralCodeVisits | Unset = UNSET
    created_at: datetime.datetime | Unset = UNSET
    updated_at: datetime.datetime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.referral_code_attributes_target_type_0 import ReferralCodeAttributesTargetType0  # noqa: PLC0415

        label = self.label

        active = self.active

        target: dict[str, Any] | None | Unset
        if isinstance(self.target, Unset):
            target = UNSET
        elif isinstance(self.target, ReferralCodeAttributesTargetType0):
            target = self.target.to_dict()
        else:
            target = self.target

        utm: dict[str, Any] | Unset = UNSET
        if not isinstance(self.utm, Unset):
            utm = self.utm.to_dict()

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        link_parameter = self.link_parameter

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        created_at: str | Unset = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: str | Unset = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if active is not UNSET:
            field_dict["active"] = active
        if target is not UNSET:
            field_dict["target"] = target
        if utm is not UNSET:
            field_dict["utm"] = utm
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if link_parameter is not UNSET:
            field_dict["link_parameter"] = link_parameter
        if stats is not UNSET:
            field_dict["stats"] = stats
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.referral_code_attributes_metadata import ReferralCodeAttributesMetadata  # noqa: PLC0415
        from ..models.referral_code_attributes_target_type_0 import ReferralCodeAttributesTargetType0  # noqa: PLC0415
        from ..models.referral_code_utm import ReferralCodeUtm  # noqa: PLC0415
        from ..models.referral_code_visits import ReferralCodeVisits  # noqa: PLC0415

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        active = d.pop("active", UNSET)

        def _parse_target(data: object) -> None | ReferralCodeAttributesTargetType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                target_type_0 = ReferralCodeAttributesTargetType0.from_dict(data)

                return target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ReferralCodeAttributesTargetType0 | Unset, data)

        target = _parse_target(d.pop("target", UNSET))

        _utm = d.pop("utm", UNSET)
        utm: ReferralCodeUtm | Unset
        if isinstance(_utm, Unset):
            utm = UNSET
        else:
            utm = ReferralCodeUtm.from_dict(_utm)

        _metadata = d.pop("metadata", UNSET)
        metadata: ReferralCodeAttributesMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ReferralCodeAttributesMetadata.from_dict(_metadata)

        link_parameter = d.pop("link_parameter", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: ReferralCodeVisits | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = ReferralCodeVisits.from_dict(_stats)

        _created_at = d.pop("created_at", UNSET)
        created_at: datetime.datetime | Unset
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = datetime.datetime.fromisoformat(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: datetime.datetime | Unset
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = datetime.datetime.fromisoformat(_updated_at)

        referral_code_attributes = cls(
            label=label,
            active=active,
            target=target,
            utm=utm,
            metadata=metadata,
            link_parameter=link_parameter,
            stats=stats,
            created_at=created_at,
            updated_at=updated_at,
        )

        referral_code_attributes.additional_properties = d
        return referral_code_attributes

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
