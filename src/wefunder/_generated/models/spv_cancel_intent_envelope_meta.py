from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.intent_review import IntentReview





T = TypeVar("T", bound="SpvCancelIntentEnvelopeMeta")



@_attrs_define
class SpvCancelIntentEnvelopeMeta:
    """ 
        Attributes:
            cancel_intent (IntentReview | Unset): Lightweight handle to a pending intent a permitted human must approve for
                the action to take effect. The full intent is not readable through this API; the review_url is the approval
                link. Returned under `meta.<action>_intent` by the endpoints that server-mint an intent (partner SPV
                close/cancel, syndicate deal close/finalize).
     """

    cancel_intent: IntentReview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.intent_review import IntentReview # noqa: PLC0415
        cancel_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cancel_intent, Unset):
            cancel_intent = self.cancel_intent.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cancel_intent is not UNSET:
            field_dict["cancel_intent"] = cancel_intent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.intent_review import IntentReview # noqa: PLC0415
        d = dict(src_dict)
        _cancel_intent = d.pop("cancel_intent", UNSET)
        cancel_intent: IntentReview | Unset
        if isinstance(_cancel_intent,  Unset):
            cancel_intent = UNSET
        else:
            cancel_intent = IntentReview.from_dict(_cancel_intent)




        spv_cancel_intent_envelope_meta = cls(
            cancel_intent=cancel_intent,
        )


        spv_cancel_intent_envelope_meta.additional_properties = d
        return spv_cancel_intent_envelope_meta

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
