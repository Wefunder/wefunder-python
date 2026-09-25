from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.spv import Spv
    from ..models.spv_cancel_intent_envelope_meta import SpvCancelIntentEnvelopeMeta


T = TypeVar("T", bound="SpvCancelIntentEnvelope")


@_attrs_define
class SpvCancelIntentEnvelope:
    """The SPV plus the pending cancel intent an advisor approves to abort the raise and refund investors.

    Attributes:
        data (Spv | Unset):
        meta (SpvCancelIntentEnvelopeMeta | Unset):
    """

    data: Spv | Unset = UNSET
    meta: SpvCancelIntentEnvelopeMeta | Unset = UNSET
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
        from ..models.spv import Spv  # noqa: PLC0415
        from ..models.spv_cancel_intent_envelope_meta import SpvCancelIntentEnvelopeMeta  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: Spv | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = Spv.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: SpvCancelIntentEnvelopeMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = SpvCancelIntentEnvelopeMeta.from_dict(_meta)

        spv_cancel_intent_envelope = cls(
            data=data,
            meta=meta,
        )

        spv_cancel_intent_envelope.additional_properties = d
        return spv_cancel_intent_envelope

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
