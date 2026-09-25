from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bulk_invite_link_envelope_errors_item import BulkInviteLinkEnvelopeErrorsItem
  from ..models.bulk_invite_link_envelope_meta import BulkInviteLinkEnvelopeMeta
  from ..models.invite_link import InviteLink





T = TypeVar("T", bound="BulkInviteLinkEnvelope")



@_attrs_define
class BulkInviteLinkEnvelope:
    """ 207 Multi-Status — created links in `data`, per-item failures in `errors`.

        Attributes:
            data (list[InviteLink] | Unset):
            errors (list[BulkInviteLinkEnvelopeErrorsItem] | Unset):
            meta (BulkInviteLinkEnvelopeMeta | Unset):
     """

    data: list[InviteLink] | Unset = UNSET
    errors: list[BulkInviteLinkEnvelopeErrorsItem] | Unset = UNSET
    meta: BulkInviteLinkEnvelopeMeta | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_invite_link_envelope_errors_item import BulkInviteLinkEnvelopeErrorsItem # noqa: PLC0415
        from ..models.bulk_invite_link_envelope_meta import BulkInviteLinkEnvelopeMeta # noqa: PLC0415
        from ..models.invite_link import InviteLink # noqa: PLC0415
        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)



        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        meta: dict[str, Any] | Unset = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if data is not UNSET:
            field_dict["data"] = data
        if errors is not UNSET:
            field_dict["errors"] = errors
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_invite_link_envelope_errors_item import BulkInviteLinkEnvelopeErrorsItem # noqa: PLC0415
        from ..models.bulk_invite_link_envelope_meta import BulkInviteLinkEnvelopeMeta # noqa: PLC0415
        from ..models.invite_link import InviteLink # noqa: PLC0415
        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[InviteLink] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:
                data_item = InviteLink.from_dict(data_item_data)



                data.append(data_item)


        _errors = d.pop("errors", UNSET)
        errors: list[BulkInviteLinkEnvelopeErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = BulkInviteLinkEnvelopeErrorsItem.from_dict(errors_item_data)



                errors.append(errors_item)


        _meta = d.pop("meta", UNSET)
        meta: BulkInviteLinkEnvelopeMeta | Unset
        if isinstance(_meta,  Unset):
            meta = UNSET
        else:
            meta = BulkInviteLinkEnvelopeMeta.from_dict(_meta)




        bulk_invite_link_envelope = cls(
            data=data,
            errors=errors,
            meta=meta,
        )


        bulk_invite_link_envelope.additional_properties = d
        return bulk_invite_link_envelope

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
