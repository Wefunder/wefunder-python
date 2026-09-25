from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.investment_session import InvestmentSession
    from ..models.investment_session_envelope_meta import InvestmentSessionEnvelopeMeta


T = TypeVar("T", bound="InvestmentSessionEnvelope")


@_attrs_define
class InvestmentSessionEnvelope:
    """
    Attributes:
        data (InvestmentSession | Unset):
        meta (InvestmentSessionEnvelopeMeta | Unset):
    """

    data: InvestmentSession | Unset = UNSET
    meta: InvestmentSessionEnvelopeMeta | Unset = UNSET
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
        from ..models.investment_session import InvestmentSession  # noqa: PLC0415
        from ..models.investment_session_envelope_meta import InvestmentSessionEnvelopeMeta  # noqa: PLC0415

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: InvestmentSession | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = InvestmentSession.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: InvestmentSessionEnvelopeMeta | Unset
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = InvestmentSessionEnvelopeMeta.from_dict(_meta)

        investment_session_envelope = cls(
            data=data,
            meta=meta,
        )

        investment_session_envelope.additional_properties = d
        return investment_session_envelope

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
