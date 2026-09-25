from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.syndicate_statistics_attributes_members_by_role import SyndicateStatisticsAttributesMembersByRole





T = TypeVar("T", bound="SyndicateStatisticsAttributes")



@_attrs_define
class SyndicateStatisticsAttributes:
    """ 
        Attributes:
            total_members (int | Unset): Count of active members (excludes resigned and exiled, filters out soft-deleted and
                hellbanned users) Example: 45.
            members_by_role (SyndicateStatisticsAttributesMembersByRole | Unset): Member count grouped by role Example:
                {'manager': 3, 'member': 35, 'invitee': 5, 'creator': 1, 'applicant': 1}.
            total_deals (int | Unset): Total number of linked deals (all linked fundraises) Example: 3.
            live_deals (int | Unset): Number of currently live deals (open/oversubscribed/closing states) Example: 1.
            total_raised (str | Unset): Total amount raised across directory-selected deals (one per company), in cents.
                String to avoid floating-point precision issues.
                 Example: 10780000.
            total_investors (int | Unset): Count of distinct investors across directory-selected deals (one per company)
                Example: 6527.
            recent_activity_count (int | Unset): Count of audit events in the last 30 days for this syndicate Example: 4.
     """

    total_members: int | Unset = UNSET
    members_by_role: SyndicateStatisticsAttributesMembersByRole | Unset = UNSET
    total_deals: int | Unset = UNSET
    live_deals: int | Unset = UNSET
    total_raised: str | Unset = UNSET
    total_investors: int | Unset = UNSET
    recent_activity_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.syndicate_statistics_attributes_members_by_role import SyndicateStatisticsAttributesMembersByRole # noqa: PLC0415
        total_members = self.total_members

        members_by_role: dict[str, Any] | Unset = UNSET
        if not isinstance(self.members_by_role, Unset):
            members_by_role = self.members_by_role.to_dict()

        total_deals = self.total_deals

        live_deals = self.live_deals

        total_raised = self.total_raised

        total_investors = self.total_investors

        recent_activity_count = self.recent_activity_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_members is not UNSET:
            field_dict["total_members"] = total_members
        if members_by_role is not UNSET:
            field_dict["members_by_role"] = members_by_role
        if total_deals is not UNSET:
            field_dict["total_deals"] = total_deals
        if live_deals is not UNSET:
            field_dict["live_deals"] = live_deals
        if total_raised is not UNSET:
            field_dict["total_raised"] = total_raised
        if total_investors is not UNSET:
            field_dict["total_investors"] = total_investors
        if recent_activity_count is not UNSET:
            field_dict["recent_activity_count"] = recent_activity_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.syndicate_statistics_attributes_members_by_role import SyndicateStatisticsAttributesMembersByRole # noqa: PLC0415
        d = dict(src_dict)
        total_members = d.pop("total_members", UNSET)

        _members_by_role = d.pop("members_by_role", UNSET)
        members_by_role: SyndicateStatisticsAttributesMembersByRole | Unset
        if isinstance(_members_by_role,  Unset):
            members_by_role = UNSET
        else:
            members_by_role = SyndicateStatisticsAttributesMembersByRole.from_dict(_members_by_role)




        total_deals = d.pop("total_deals", UNSET)

        live_deals = d.pop("live_deals", UNSET)

        total_raised = d.pop("total_raised", UNSET)

        total_investors = d.pop("total_investors", UNSET)

        recent_activity_count = d.pop("recent_activity_count", UNSET)

        syndicate_statistics_attributes = cls(
            total_members=total_members,
            members_by_role=members_by_role,
            total_deals=total_deals,
            live_deals=live_deals,
            total_raised=total_raised,
            total_investors=total_investors,
            recent_activity_count=recent_activity_count,
        )


        syndicate_statistics_attributes.additional_properties = d
        return syndicate_statistics_attributes

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
