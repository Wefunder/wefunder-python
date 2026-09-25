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





T = TypeVar("T", bound="SyndicateDealFinalizeIntentEnvelopeMeta")



@_attrs_define
class SyndicateDealFinalizeIntentEnvelopeMeta:
    """ 
        Attributes:
            finalize_deal_intent (IntentReview | Unset): Lightweight handle to a pending intent a permitted human must
                approve for the action to take effect. The full intent is not readable through this API; the review_url is the
                approval link. Returned under `meta.<action>_intent` by the endpoints that server-mint an intent (partner SPV
                close/cancel, syndicate deal close/finalize).
     """

    finalize_deal_intent: IntentReview | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.intent_review import IntentReview # noqa: PLC0415
        finalize_deal_intent: dict[str, Any] | Unset = UNSET
        if not isinstance(self.finalize_deal_intent, Unset):
            finalize_deal_intent = self.finalize_deal_intent.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if finalize_deal_intent is not UNSET:
            field_dict["finalize_deal_intent"] = finalize_deal_intent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.intent_review import IntentReview # noqa: PLC0415
        d = dict(src_dict)
        _finalize_deal_intent = d.pop("finalize_deal_intent", UNSET)
        finalize_deal_intent: IntentReview | Unset
        if isinstance(_finalize_deal_intent,  Unset):
            finalize_deal_intent = UNSET
        else:
            finalize_deal_intent = IntentReview.from_dict(_finalize_deal_intent)




        syndicate_deal_finalize_intent_envelope_meta = cls(
            finalize_deal_intent=finalize_deal_intent,
        )


        syndicate_deal_finalize_intent_envelope_meta.additional_properties = d
        return syndicate_deal_finalize_intent_envelope_meta

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
