from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.intent_review import IntentReview


T = TypeVar("T", bound="SpvCloseIntentEnvelopeMeta")


@_attrs_define
class SpvCloseIntentEnvelopeMeta:
    """
    Attributes:
        disburse_intent (IntentReview | Unset): Lightweight handle to a pending intent a permitted human must approve
            for the action to take effect. The full intent is not readable through this API; the review_url is the approval
            link. Returned under `meta.<action>_intent` by the endpoints that server-mint an intent (partner SPV
            close/cancel, syndicate deal close/finalize).
    """

    disburse_intent: IntentReview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        disburse_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.disburse_intent, Unset):
            disburse_intent = self.disburse_intent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disburse_intent is not UNSET:
            field_dict["disburse_intent"] = disburse_intent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.intent_review import IntentReview  # noqa: PLC0415

        d = dict(src_dict)
        _disburse_intent = d.pop("disburse_intent", UNSET)
        disburse_intent: IntentReview | Unset
        if isinstance(_disburse_intent, Unset):
            disburse_intent = UNSET
        else:
            disburse_intent = IntentReview.from_dict(_disburse_intent)

        spv_close_intent_envelope_meta = cls(
            disburse_intent=disburse_intent,
        )

        spv_close_intent_envelope_meta.additional_properties = d
        return spv_close_intent_envelope_meta

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
