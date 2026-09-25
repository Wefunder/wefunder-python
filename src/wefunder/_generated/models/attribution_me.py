from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.attribution_campaign_access import AttributionCampaignAccess
  from ..models.attribution_partner_type_0 import AttributionPartnerType0
  from ..models.attribution_user import AttributionUser





T = TypeVar("T", bound="AttributionMe")



@_attrs_define
class AttributionMe:
    """ 
        Attributes:
            user (AttributionUser | Unset):
            partner (AttributionPartnerType0 | None | Unset):
            campaigns (list[AttributionCampaignAccess] | Unset):
     """

    user: AttributionUser | Unset = UNSET
    partner: AttributionPartnerType0 | None | Unset = UNSET
    campaigns: list[AttributionCampaignAccess] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.attribution_campaign_access import AttributionCampaignAccess # noqa: PLC0415
        from ..models.attribution_partner_type_0 import AttributionPartnerType0 # noqa: PLC0415
        from ..models.attribution_user import AttributionUser # noqa: PLC0415
        user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()

        partner: dict[str, Any] | None | Unset
        if isinstance(self.partner, Unset):
            partner = UNSET
        elif isinstance(self.partner, AttributionPartnerType0):
            partner = self.partner.to_dict()
        else:
            partner = self.partner

        campaigns: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.campaigns, Unset):
            campaigns = []
            for campaigns_item_data in self.campaigns:
                campaigns_item = campaigns_item_data.to_dict()
                campaigns.append(campaigns_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if user is not UNSET:
            field_dict["user"] = user
        if partner is not UNSET:
            field_dict["partner"] = partner
        if campaigns is not UNSET:
            field_dict["campaigns"] = campaigns

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.attribution_campaign_access import AttributionCampaignAccess # noqa: PLC0415
        from ..models.attribution_partner_type_0 import AttributionPartnerType0 # noqa: PLC0415
        from ..models.attribution_user import AttributionUser # noqa: PLC0415
        d = dict(src_dict)
        _user = d.pop("user", UNSET)
        user: AttributionUser | Unset
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = AttributionUser.from_dict(_user)




        def _parse_partner(data: object) -> AttributionPartnerType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_attribution_partner_type_0 = AttributionPartnerType0.from_dict(data)



                return componentsschemas_attribution_partner_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AttributionPartnerType0 | None | Unset, data)

        partner = _parse_partner(d.pop("partner", UNSET))


        _campaigns = d.pop("campaigns", UNSET)
        campaigns: list[AttributionCampaignAccess] | Unset = UNSET
        if _campaigns is not UNSET:
            campaigns = []
            for campaigns_item_data in _campaigns:
                campaigns_item = AttributionCampaignAccess.from_dict(campaigns_item_data)



                campaigns.append(campaigns_item)


        attribution_me = cls(
            user=user,
            partner=partner,
            campaigns=campaigns,
        )


        attribution_me.additional_properties = d
        return attribution_me

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
