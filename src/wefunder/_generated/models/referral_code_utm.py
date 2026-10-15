from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferralCodeUtm")


@_attrs_define
class ReferralCodeUtm:
    """Optional UTM presets. On a visit that carries this code, each preset fills the matching
    `utm_*` field when the link leaves it blank; a value on the link always wins. Each value is
    at most 100 printable ASCII characters. `source` and `campaign` may not start with `wf_`.

        Attributes:
            source (str | Unset):  Example: acme_newsletter.
            medium (str | Unset):  Example: email.
            campaign (str | Unset):  Example: october.
            content (str | Unset):  Example: header_link.
            term (str | Unset):  Example: seed_round.
    """

    source: str | Unset = UNSET
    medium: str | Unset = UNSET
    campaign: str | Unset = UNSET
    content: str | Unset = UNSET
    term: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source = self.source

        medium = self.medium

        campaign = self.campaign

        content = self.content

        term = self.term

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source is not UNSET:
            field_dict["source"] = source
        if medium is not UNSET:
            field_dict["medium"] = medium
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if content is not UNSET:
            field_dict["content"] = content
        if term is not UNSET:
            field_dict["term"] = term

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        source = d.pop("source", UNSET)

        medium = d.pop("medium", UNSET)

        campaign = d.pop("campaign", UNSET)

        content = d.pop("content", UNSET)

        term = d.pop("term", UNSET)

        referral_code_utm = cls(
            source=source,
            medium=medium,
            campaign=campaign,
            content=content,
            term=term,
        )

        referral_code_utm.additional_properties = d
        return referral_code_utm

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
