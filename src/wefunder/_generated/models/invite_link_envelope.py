from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invite_link import InviteLink
    from ..models.invite_link_envelope_meta import InviteLinkEnvelopeMeta


T = TypeVar("T", bound="InviteLinkEnvelope")


@_attrs_define
class InviteLinkEnvelope:
    """
    Attributes:
        data (InviteLink | Unset): A partner invite link. `id` is the link's `il_...` id (distinct from the URL
            access `token`, which lives only in `url`). Per-person (`reuse: false`)
            links carry the extra recipient + derived-status attributes below; reusable
            links omit them.
        meta (InviteLinkEnvelopeMeta | Unset):
    """

    data: InviteLink | Unset = UNSET
    meta: InviteLinkEnvelopeMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invite_link import InviteLink  # noqa: PLC0415
        from ..models.invite_link_envelope_meta import InviteLinkEnvelopeMeta  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: InviteLink | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = InviteLink.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: InviteLinkEnvelopeMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = InviteLinkEnvelopeMeta.from_dict(_meta)

        invite_link_envelope = cls(
            data=data,
            meta=meta,
        )

        invite_link_envelope.additional_properties = d
        return invite_link_envelope

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
