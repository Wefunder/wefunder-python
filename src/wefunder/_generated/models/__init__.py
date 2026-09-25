"""Contains all the data models used in inputs/outputs"""

from .anonymized_attribution import AnonymizedAttribution
from .anonymized_attribution_amount_tier import AnonymizedAttributionAmountTier
from .anonymized_attribution_attribution import AnonymizedAttributionAttribution
from .anonymized_attribution_attribution_quality_score import AnonymizedAttributionAttributionQualityScore
from .anonymized_attribution_attribution_time_to_invest_bucket import AnonymizedAttributionAttributionTimeToInvestBucket
from .anonymized_attribution_status import AnonymizedAttributionStatus
from .anonymized_attribution_status_bucket import AnonymizedAttributionStatusBucket
from .attributed_investment_list_envelope import AttributedInvestmentListEnvelope
from .attributed_investment_list_envelope_meta import AttributedInvestmentListEnvelopeMeta
from .attributed_investment_list_envelope_meta_detail_level import AttributedInvestmentListEnvelopeMetaDetailLevel
from .attribution_campaign_access import AttributionCampaignAccess
from .attribution_campaign_summary import AttributionCampaignSummary
from .attribution_campaign_summary_list_envelope import AttributionCampaignSummaryListEnvelope
from .attribution_me import AttributionMe
from .attribution_me_envelope import AttributionMeEnvelope
from .attribution_partner_type_0 import AttributionPartnerType0
from .attribution_partner_type_0_status import AttributionPartnerType0Status
from .attribution_stats import AttributionStats
from .attribution_stats_by_campaign_item import AttributionStatsByCampaignItem
from .attribution_stats_by_source_item import AttributionStatsBySourceItem
from .attribution_stats_envelope import AttributionStatsEnvelope
from .attribution_stats_period import AttributionStatsPeriod
from .attribution_stats_quality_breakdown import AttributionStatsQualityBreakdown
from .attribution_stats_totals import AttributionStatsTotals
from .attribution_user import AttributionUser
from .audit_event import AuditEvent
from .audit_event_attributes import AuditEventAttributes
from .audit_event_attributes_new_values_type_0 import AuditEventAttributesNewValuesType0
from .audit_event_attributes_old_values_type_0 import AuditEventAttributesOldValuesType0
from .audit_event_attributes_status import AuditEventAttributesStatus
from .audit_event_list_envelope import AuditEventListEnvelope
from .bulk_invite_link_create_input import BulkInviteLinkCreateInput
from .bulk_invite_link_envelope import BulkInviteLinkEnvelope
from .bulk_invite_link_envelope_errors_item import BulkInviteLinkEnvelopeErrorsItem
from .bulk_invite_link_envelope_meta import BulkInviteLinkEnvelopeMeta
from .campaign import Campaign
from .campaign_attributes import CampaignAttributes
from .campaign_list_envelope import CampaignListEnvelope
from .comment_proposal_envelope import CommentProposalEnvelope
from .comment_proposal_envelope_draft_type_0 import CommentProposalEnvelopeDraftType0
from .comment_proposal_envelope_draft_type_0_params import CommentProposalEnvelopeDraftType0Params
from .comment_proposal_envelope_proposal import CommentProposalEnvelopeProposal
from .comment_proposal_envelope_proposal_target_type import CommentProposalEnvelopeProposalTargetType
from .comment_proposal_envelope_related_questions_item import CommentProposalEnvelopeRelatedQuestionsItem
from .company import Company
from .company_attributes import CompanyAttributes
from .company_attributes_location import CompanyAttributesLocation
from .company_disclosures import CompanyDisclosures
from .company_disclosures_attributes import CompanyDisclosuresAttributes
from .company_disclosures_attributes_business import CompanyDisclosuresAttributesBusiness
from .company_disclosures_attributes_capital_structure_type_0_item import (
    CompanyDisclosuresAttributesCapitalStructureType0Item,
)
from .company_disclosures_attributes_current_position import CompanyDisclosuresAttributesCurrentPosition
from .company_disclosures_attributes_filing import CompanyDisclosuresAttributesFiling
from .company_disclosures_attributes_financial_statements import CompanyDisclosuresAttributesFinancialStatements
from .company_disclosures_attributes_outstanding_debts_type_0 import CompanyDisclosuresAttributesOutstandingDebtsType0
from .company_disclosures_attributes_outstanding_debts_type_0_items_item import (
    CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem,
)
from .company_disclosures_attributes_outstanding_notes_type_0_item import (
    CompanyDisclosuresAttributesOutstandingNotesType0Item,
)
from .company_disclosures_attributes_prior_offerings_type_0_item import (
    CompanyDisclosuresAttributesPriorOfferingsType0Item,
)
from .company_disclosures_attributes_ratios_type_0 import CompanyDisclosuresAttributesRatiosType0
from .company_disclosures_attributes_related_parties_type_0 import CompanyDisclosuresAttributesRelatedPartiesType0
from .company_disclosures_attributes_related_parties_type_0_parties_item import (
    CompanyDisclosuresAttributesRelatedPartiesType0PartiesItem,
)
from .company_disclosures_attributes_use_of_funds_type_0_item import CompanyDisclosuresAttributesUseOfFundsType0Item
from .company_disclosures_attributes_voting_power_type_0_item import CompanyDisclosuresAttributesVotingPowerType0Item
from .company_disclosures_envelope import CompanyDisclosuresEnvelope
from .company_disclosures_type import CompanyDisclosuresType
from .company_envelope import CompanyEnvelope
from .company_pitch import CompanyPitch
from .company_pitch_attributes import CompanyPitchAttributes
from .company_pitch_attributes_authored_by import CompanyPitchAttributesAuthoredBy
from .company_pitch_attributes_perks_type_0 import CompanyPitchAttributesPerksType0
from .company_pitch_attributes_story import CompanyPitchAttributesStory
from .company_pitch_envelope import CompanyPitchEnvelope
from .company_pitch_type import CompanyPitchType
from .company_question import CompanyQuestion
from .company_question_attributes import CompanyQuestionAttributes
from .company_question_attributes_answers_item import CompanyQuestionAttributesAnswersItem
from .company_question_attributes_match import CompanyQuestionAttributesMatch
from .company_question_list_envelope import CompanyQuestionListEnvelope
from .company_question_list_envelope_meta import CompanyQuestionListEnvelopeMeta
from .company_question_person import CompanyQuestionPerson
from .company_question_type import CompanyQuestionType
from .company_search_result import CompanySearchResult
from .company_search_result_attributes import CompanySearchResultAttributes
from .company_search_result_list_envelope import CompanySearchResultListEnvelope
from .company_search_result_list_envelope_meta import CompanySearchResultListEnvelopeMeta
from .company_search_result_type import CompanySearchResultType
from .company_totals import CompanyTotals
from .company_update import CompanyUpdate
from .company_update_attributes import CompanyUpdateAttributes
from .company_update_attributes_author_type_0 import CompanyUpdateAttributesAuthorType0
from .company_update_attributes_visibility_type_1 import CompanyUpdateAttributesVisibilityType1
from .company_update_attributes_visibility_type_2_type_1 import CompanyUpdateAttributesVisibilityType2Type1
from .company_update_attributes_visibility_type_3_type_1 import CompanyUpdateAttributesVisibilityType3Type1
from .company_update_envelope import CompanyUpdateEnvelope
from .company_update_list_envelope import CompanyUpdateListEnvelope
from .company_update_list_envelope_meta import CompanyUpdateListEnvelopeMeta
from .company_update_type import CompanyUpdateType
from .connected_app import ConnectedApp
from .connected_app_attributes import ConnectedAppAttributes
from .connected_app_list_envelope import ConnectedAppListEnvelope
from .connected_app_revocation import ConnectedAppRevocation
from .connected_app_revocation_envelope import ConnectedAppRevocationEnvelope
from .convertible_note_security import ConvertibleNoteSecurity
from .convertible_note_security_terms import ConvertibleNoteSecurityTerms
from .convertible_note_security_type import ConvertibleNoteSecurityType
from .create_installation_body import CreateInstallationBody
from .create_installation_body_target_type import CreateInstallationBodyTargetType
from .create_installation_token_body import CreateInstallationTokenBody
from .create_intent_body import CreateIntentBody
from .create_intent_body_action_name import CreateIntentBodyActionName
from .create_intent_body_params import CreateIntentBodyParams
from .create_partner_invite_body import CreatePartnerInviteBody
from .create_partner_invite_body_direction import CreatePartnerInviteBodyDirection
from .create_webhook_endpoint_body import CreateWebhookEndpointBody
from .create_webhook_endpoint_body_events_item import CreateWebhookEndpointBodyEventsItem
from .create_webhook_endpoint_body_mode import CreateWebhookEndpointBodyMode
from .create_webhook_subscription_body import CreateWebhookSubscriptionBody
from .create_webhook_subscription_body_events_item import CreateWebhookSubscriptionBodyEventsItem
from .current_raise import CurrentRaise
from .deal_investor import DealInvestor
from .deal_investor_attributes import DealInvestorAttributes
from .deal_investor_attributes_status import DealInvestorAttributesStatus
from .deal_investor_list_envelope import DealInvestorListEnvelope
from .deal_investor_list_envelope_meta import DealInvestorListEnvelopeMeta
from .debt_security import DebtSecurity
from .debt_security_terms import DebtSecurityTerms
from .debt_security_type import DebtSecurityType
from .delete_webhook_endpoint_response_200 import DeleteWebhookEndpointResponse200
from .delete_webhook_endpoint_response_200_data import DeleteWebhookEndpointResponse200Data
from .disclosure_document import DisclosureDocument
from .disclosure_person import DisclosurePerson
from .eligible_target_list_envelope import EligibleTargetListEnvelope
from .eligible_target_list_envelope_data_item import EligibleTargetListEnvelopeDataItem
from .eligible_target_list_envelope_data_item_type import EligibleTargetListEnvelopeDataItemType
from .eligible_target_list_envelope_meta import EligibleTargetListEnvelopeMeta
from .equity_security import EquitySecurity
from .equity_security_terms import EquitySecurityTerms
from .equity_security_terms_share_class_type_1 import EquitySecurityTermsShareClassType1
from .equity_security_terms_share_class_type_2_type_1 import EquitySecurityTermsShareClassType2Type1
from .equity_security_terms_share_class_type_3_type_1 import EquitySecurityTermsShareClassType3Type1
from .equity_security_type import EquitySecurityType
from .error import Error
from .error_error import ErrorError
from .error_error_details import ErrorErrorDetails
from .exemption import Exemption
from .exemption_family import ExemptionFamily
from .fiscal_year_financials import FiscalYearFinancials
from .follow_state_envelope import FollowStateEnvelope
from .follow_state_envelope_data import FollowStateEnvelopeData
from .follow_state_envelope_data_attributes import FollowStateEnvelopeDataAttributes
from .follow_state_envelope_data_type import FollowStateEnvelopeDataType
from .followed_company import FollowedCompany
from .followed_company_attributes import FollowedCompanyAttributes
from .followed_company_list_envelope import FollowedCompanyListEnvelope
from .followed_company_type import FollowedCompanyType
from .full_attribution import FullAttribution
from .full_attribution_attribution import FullAttributionAttribution
from .full_attribution_attribution_quality_score import FullAttributionAttributionQualityScore
from .full_attribution_attribution_time_to_invest_bucket import FullAttributionAttributionTimeToInvestBucket
from .full_attribution_investor import FullAttributionInvestor
from .full_attribution_status import FullAttributionStatus
from .full_attribution_status_bucket import FullAttributionStatusBucket
from .fund_security import FundSecurity
from .fund_security_terms import FundSecurityTerms
from .fund_security_type import FundSecurityType
from .get_company_disclosures_sections_item import GetCompanyDisclosuresSectionsItem
from .get_company_pitch_sections_item import GetCompanyPitchSectionsItem
from .get_portfolio_status import GetPortfolioStatus
from .get_syndicate_portfolio_status import GetSyndicatePortfolioStatus
from .installation import Installation
from .installation_attributes import InstallationAttributes
from .installation_attributes_status import InstallationAttributesStatus
from .installation_attributes_target import InstallationAttributesTarget
from .installation_attributes_target_type import InstallationAttributesTargetType
from .installation_envelope import InstallationEnvelope
from .installation_envelope_meta import InstallationEnvelopeMeta
from .installation_list_envelope import InstallationListEnvelope
from .installation_list_envelope_meta import InstallationListEnvelopeMeta
from .installation_token_envelope import InstallationTokenEnvelope
from .installation_token_envelope_meta import InstallationTokenEnvelopeMeta
from .installation_token_envelope_token import InstallationTokenEnvelopeToken
from .intent import Intent
from .intent_attributes import IntentAttributes
from .intent_attributes_execution_result_type_0 import IntentAttributesExecutionResultType0
from .intent_attributes_status import IntentAttributesStatus
from .intent_envelope import IntentEnvelope
from .intent_list_envelope import IntentListEnvelope
from .intent_preview_envelope import IntentPreviewEnvelope
from .intent_preview_envelope_data import IntentPreviewEnvelopeData
from .intent_preview_envelope_data_attributes import IntentPreviewEnvelopeDataAttributes
from .intent_preview_envelope_data_attributes_params import IntentPreviewEnvelopeDataAttributesParams
from .intent_preview_envelope_data_type import IntentPreviewEnvelopeDataType
from .intent_review import IntentReview
from .investment_change_list_envelope import InvestmentChangeListEnvelope
from .investment_change_list_envelope_meta import InvestmentChangeListEnvelopeMeta
from .investment_change_list_envelope_meta_mode import InvestmentChangeListEnvelopeMetaMode
from .investment_delta_record import InvestmentDeltaRecord
from .investment_delta_record_amounts import InvestmentDeltaRecordAmounts
from .investment_delta_record_blockers_item import InvestmentDeltaRecordBlockersItem
from .investment_delta_record_contracts_item import InvestmentDeltaRecordContractsItem
from .investment_delta_record_investor import InvestmentDeltaRecordInvestor
from .investment_delta_record_investor_address import InvestmentDeltaRecordInvestorAddress
from .investment_delta_record_reason import InvestmentDeltaRecordReason
from .investment_delta_record_status import InvestmentDeltaRecordStatus
from .investment_envelope import InvestmentEnvelope
from .investment_envelope_meta import InvestmentEnvelopeMeta
from .investment_envelope_meta_source import InvestmentEnvelopeMetaSource
from .investment_list_envelope import InvestmentListEnvelope
from .investment_list_envelope_meta import InvestmentListEnvelopeMeta
from .investment_list_envelope_meta_mode import InvestmentListEnvelopeMetaMode
from .investment_session import InvestmentSession
from .investment_session_attributes import InvestmentSessionAttributes
from .investment_session_attributes_events_item import InvestmentSessionAttributesEventsItem
from .investment_session_attributes_funding_status import InvestmentSessionAttributesFundingStatus
from .investment_session_attributes_kyc_status import InvestmentSessionAttributesKycStatus
from .investment_session_attributes_metadata import InvestmentSessionAttributesMetadata
from .investment_session_attributes_status import InvestmentSessionAttributesStatus
from .investment_session_create_input import InvestmentSessionCreateInput
from .investment_session_create_input_metadata_type_0 import InvestmentSessionCreateInputMetadataType0
from .investment_session_envelope import InvestmentSessionEnvelope
from .investment_session_envelope_meta import InvestmentSessionEnvelopeMeta
from .investment_session_list_envelope import InvestmentSessionListEnvelope
from .investment_session_list_envelope_meta import InvestmentSessionListEnvelopeMeta
from .investor import Investor
from .investor_attributes import InvestorAttributes
from .investor_envelope import InvestorEnvelope
from .investor_list_envelope import InvestorListEnvelope
from .invite_link import InviteLink
from .invite_link_attributes import InviteLinkAttributes
from .invite_link_attributes_events_item import InviteLinkAttributesEventsItem
from .invite_link_attributes_status import InviteLinkAttributesStatus
from .invite_link_create_input import InviteLinkCreateInput
from .invite_link_envelope import InviteLinkEnvelope
from .invite_link_envelope_meta import InviteLinkEnvelopeMeta
from .invite_link_list_envelope import InviteLinkListEnvelope
from .invite_link_list_envelope_meta import InviteLinkListEnvelopeMeta
from .invite_link_update_input import InviteLinkUpdateInput
from .invite_syndicate_member_body import InviteSyndicateMemberBody
from .invite_syndicate_member_body_syndicate_permission import InviteSyndicateMemberBodySyndicatePermission
from .list_activity_status import ListActivityStatus
from .list_attributed_investments_detail_level import ListAttributedInvestmentsDetailLevel
from .list_company_questions_sort import ListCompanyQuestionsSort
from .list_eligible_install_targets_target_type import ListEligibleInstallTargetsTargetType
from .list_intents_status import ListIntentsStatus
from .list_investments_status import ListInvestmentsStatus
from .list_offerings_business_model_item import ListOfferingsBusinessModelItem
from .list_offerings_exemption import ListOfferingsExemption
from .list_offerings_industry_item import ListOfferingsIndustryItem
from .list_offerings_security import ListOfferingsSecurity
from .list_offerings_sort import ListOfferingsSort
from .list_portfolio_positions_status import ListPortfolioPositionsStatus
from .list_syndicate_members_accredited import ListSyndicateMembersAccredited
from .list_syndicate_members_has_invested import ListSyndicateMembersHasInvested
from .list_syndicate_members_permission import ListSyndicateMembersPermission
from .list_syndicate_members_sort import ListSyndicateMembersSort
from .list_syndicate_portfolio_positions_status import ListSyndicatePortfolioPositionsStatus
from .marketing_partner import MarketingPartner
from .marketing_partner_envelope import MarketingPartnerEnvelope
from .marketing_partner_status import MarketingPartnerStatus
from .member_investment import MemberInvestment
from .member_investment_attributes import MemberInvestmentAttributes
from .member_investment_attributes_status import MemberInvestmentAttributesStatus
from .member_investment_list_envelope import MemberInvestmentListEnvelope
from .member_investment_list_envelope_meta import MemberInvestmentListEnvelopeMeta
from .my_company import MyCompany
from .my_company_attributes import MyCompanyAttributes
from .my_company_list_envelope import MyCompanyListEnvelope
from .my_company_list_envelope_meta import MyCompanyListEnvelopeMeta
from .my_company_type import MyCompanyType
from .offering import Offering
from .offering_attributes import OfferingAttributes
from .offering_attributes_intended_security_type_0 import OfferingAttributesIntendedSecurityType0
from .offering_attributes_intended_security_type_0_type import OfferingAttributesIntendedSecurityType0Type
from .offering_attributes_status import OfferingAttributesStatus
from .offering_envelope import OfferingEnvelope
from .offering_list_envelope import OfferingListEnvelope
from .offering_list_envelope_meta import OfferingListEnvelopeMeta
from .offering_list_envelope_meta_filters import OfferingListEnvelopeMetaFilters
from .offering_stats_envelope import OfferingStatsEnvelope
from .offering_stats_envelope_data import OfferingStatsEnvelopeData
from .offering_stats_envelope_data_by_status import OfferingStatsEnvelopeDataByStatus
from .offering_stats_envelope_data_by_status_additional_property import (
    OfferingStatsEnvelopeDataByStatusAdditionalProperty,
)
from .offering_stats_envelope_data_total import OfferingStatsEnvelopeDataTotal
from .offering_stats_envelope_meta import OfferingStatsEnvelopeMeta
from .offering_stats_envelope_meta_source import OfferingStatsEnvelopeMetaSource
from .offering_warnings_item import OfferingWarningsItem
from .offering_warnings_item_code import OfferingWarningsItemCode
from .other_security import OtherSecurity
from .other_security_terms import OtherSecurityTerms
from .other_security_type import OtherSecurityType
from .pagination_meta import PaginationMeta
from .partner_investment import PartnerInvestment
from .partner_investment_attributes import PartnerInvestmentAttributes
from .partner_investment_attributes_accreditation_type_0 import PartnerInvestmentAttributesAccreditationType0
from .partner_investment_attributes_accreditation_type_0_status import (
    PartnerInvestmentAttributesAccreditationType0Status,
)
from .partner_investment_attributes_accreditation_type_0_type import PartnerInvestmentAttributesAccreditationType0Type
from .partner_investment_attributes_status import PartnerInvestmentAttributesStatus
from .partner_investment_envelope import PartnerInvestmentEnvelope
from .partner_investment_list_envelope import PartnerInvestmentListEnvelope
from .partner_investor import PartnerInvestor
from .partner_investor_attributes import PartnerInvestorAttributes
from .partner_investor_list_envelope import PartnerInvestorListEnvelope
from .partner_invite import PartnerInvite
from .partner_invite_direction import PartnerInviteDirection
from .partner_invite_envelope import PartnerInviteEnvelope
from .partner_invite_list_envelope import PartnerInviteListEnvelope
from .partner_invite_status import PartnerInviteStatus
from .partner_webhook_event import PartnerWebhookEvent
from .partner_webhook_event_data import PartnerWebhookEventData
from .partner_webhook_event_envelope import PartnerWebhookEventEnvelope
from .partner_webhook_subscription import PartnerWebhookSubscription
from .partner_webhook_subscription_attributes import PartnerWebhookSubscriptionAttributes
from .partner_webhook_subscription_create_input import PartnerWebhookSubscriptionCreateInput
from .partner_webhook_subscription_envelope import PartnerWebhookSubscriptionEnvelope
from .partner_webhook_subscription_list_envelope import PartnerWebhookSubscriptionListEnvelope
from .partner_webhook_subscription_with_secret import PartnerWebhookSubscriptionWithSecret
from .partner_webhook_subscription_with_secret_attributes import PartnerWebhookSubscriptionWithSecretAttributes
from .partner_webhook_subscription_with_secret_envelope import PartnerWebhookSubscriptionWithSecretEnvelope
from .past_round import PastRound
from .past_round_source import PastRoundSource
from .perk_tier import PerkTier
from .pitch_block import PitchBlock
from .pitch_block_links_item import PitchBlockLinksItem
from .pitch_block_type import PitchBlockType
from .portfolio_company_ref import PortfolioCompanyRef
from .portfolio_holding import PortfolioHolding
from .portfolio_holding_status import PortfolioHoldingStatus
from .portfolio_position import PortfolioPosition
from .portfolio_position_attributes import PortfolioPositionAttributes
from .portfolio_position_attributes_asset_type import PortfolioPositionAttributesAssetType
from .portfolio_position_attributes_exit_reason import PortfolioPositionAttributesExitReason
from .portfolio_position_attributes_status import PortfolioPositionAttributesStatus
from .portfolio_position_list_envelope import PortfolioPositionListEnvelope
from .portfolio_position_list_envelope_meta import PortfolioPositionListEnvelopeMeta
from .portfolio_position_type import PortfolioPositionType
from .portfolio_security import PortfolioSecurity
from .portfolio_security_owner_type_0 import PortfolioSecurityOwnerType0
from .portfolio_security_owner_type_0_kind import PortfolioSecurityOwnerType0Kind
from .portfolio_security_terms import PortfolioSecurityTerms
from .portfolio_summary_envelope import PortfolioSummaryEnvelope
from .portfolio_summary_envelope_data import PortfolioSummaryEnvelopeData
from .portfolio_summary_envelope_data_attributes import PortfolioSummaryEnvelopeDataAttributes
from .portfolio_summary_envelope_data_attributes_position_counts import (
    PortfolioSummaryEnvelopeDataAttributesPositionCounts,
)
from .preview_intent_body import PreviewIntentBody
from .preview_intent_body_params import PreviewIntentBodyParams
from .register_as_partner_body import RegisterAsPartnerBody
from .reorder_syndicate_members_body import ReorderSyndicateMembersBody
from .revenue_share_security import RevenueShareSecurity
from .revenue_share_security_terms import RevenueShareSecurityTerms
from .revenue_share_security_terms_revenue_basis_type_1 import RevenueShareSecurityTermsRevenueBasisType1
from .revenue_share_security_terms_revenue_basis_type_2_type_1 import RevenueShareSecurityTermsRevenueBasisType2Type1
from .revenue_share_security_terms_revenue_basis_type_3_type_1 import RevenueShareSecurityTermsRevenueBasisType3Type1
from .revenue_share_security_type import RevenueShareSecurityType
from .safe_security import SafeSecurity
from .safe_security_terms import SafeSecurityTerms
from .safe_security_type import SafeSecurityType
from .security_summary import SecuritySummary
from .security_summary_type import SecuritySummaryType
from .spv import Spv
from .spv_attributes import SpvAttributes
from .spv_attributes_metadata import SpvAttributesMetadata
from .spv_attributes_status import SpvAttributesStatus
from .spv_attributes_target_company import SpvAttributesTargetCompany
from .spv_cancel_intent_envelope import SpvCancelIntentEnvelope
from .spv_cancel_intent_envelope_meta import SpvCancelIntentEnvelopeMeta
from .spv_close_intent_envelope import SpvCloseIntentEnvelope
from .spv_close_intent_envelope_meta import SpvCloseIntentEnvelopeMeta
from .spv_create_input import SpvCreateInput
from .spv_create_input_metadata import SpvCreateInputMetadata
from .spv_envelope import SpvEnvelope
from .spv_list_envelope import SpvListEnvelope
from .spv_metrics import SpvMetrics
from .spv_settings import SpvSettings
from .spv_settings_accreditation_type import SpvSettingsAccreditationType
from .spv_status import SpvStatus
from .spv_status_attributes import SpvStatusAttributes
from .spv_status_attributes_status import SpvStatusAttributesStatus
from .spv_status_envelope import SpvStatusEnvelope
from .spv_status_envelope_meta import SpvStatusEnvelopeMeta
from .spv_terms import SpvTerms
from .spv_terms_safe_type import SpvTermsSafeType
from .spv_terms_structure import SpvTermsStructure
from .spv_with_meta_envelope import SpvWithMetaEnvelope
from .spv_with_meta_envelope_meta import SpvWithMetaEnvelopeMeta
from .syndicate import Syndicate
from .syndicate_attributes import SyndicateAttributes
from .syndicate_deal import SyndicateDeal
from .syndicate_deal_attributes import SyndicateDealAttributes
from .syndicate_deal_attributes_status import SyndicateDealAttributesStatus
from .syndicate_deal_close_intent_envelope import SyndicateDealCloseIntentEnvelope
from .syndicate_deal_close_intent_envelope_meta import SyndicateDealCloseIntentEnvelopeMeta
from .syndicate_deal_detail_envelope import SyndicateDealDetailEnvelope
from .syndicate_deal_envelope import SyndicateDealEnvelope
from .syndicate_deal_finalize_intent_envelope import SyndicateDealFinalizeIntentEnvelope
from .syndicate_deal_finalize_intent_envelope_meta import SyndicateDealFinalizeIntentEnvelopeMeta
from .syndicate_deal_list_envelope import SyndicateDealListEnvelope
from .syndicate_deal_list_envelope_meta import SyndicateDealListEnvelopeMeta
from .syndicate_detail_envelope import SyndicateDetailEnvelope
from .syndicate_list_envelope import SyndicateListEnvelope
from .syndicate_member import SyndicateMember
from .syndicate_member_attributes import SyndicateMemberAttributes
from .syndicate_member_attributes_syndicate_permission import SyndicateMemberAttributesSyndicatePermission
from .syndicate_member_envelope import SyndicateMemberEnvelope
from .syndicate_member_list_envelope import SyndicateMemberListEnvelope
from .syndicate_portfolio_summary_envelope import SyndicatePortfolioSummaryEnvelope
from .syndicate_portfolio_summary_envelope_data import SyndicatePortfolioSummaryEnvelopeData
from .syndicate_portfolio_summary_envelope_data_attributes import SyndicatePortfolioSummaryEnvelopeDataAttributes
from .syndicate_portfolio_summary_envelope_data_attributes_deal_counts import (
    SyndicatePortfolioSummaryEnvelopeDataAttributesDealCounts,
)
from .syndicate_statistics import SyndicateStatistics
from .syndicate_statistics_attributes import SyndicateStatisticsAttributes
from .syndicate_statistics_attributes_members_by_role import SyndicateStatisticsAttributesMembersByRole
from .syndicate_statistics_envelope import SyndicateStatisticsEnvelope
from .tag_ref import TagRef
from .target_company_input import TargetCompanyInput
from .test_webhook_endpoint_body import TestWebhookEndpointBody
from .test_webhook_endpoint_body_event import TestWebhookEndpointBodyEvent
from .update_syndicate_body import UpdateSyndicateBody
from .update_syndicate_body_syndicate import UpdateSyndicateBodySyndicate
from .update_syndicate_member_body import UpdateSyndicateMemberBody
from .update_syndicate_member_body_member import UpdateSyndicateMemberBodyMember
from .update_webhook_endpoint_body import UpdateWebhookEndpointBody
from .update_webhook_endpoint_body_events_item import UpdateWebhookEndpointBodyEventsItem
from .user import User
from .user_attributes import UserAttributes
from .user_envelope import UserEnvelope
from .validation_error import ValidationError
from .validation_error_error import ValidationErrorError
from .validation_error_error_details_item import ValidationErrorErrorDetailsItem
from .webhook_delivery import WebhookDelivery
from .webhook_delivery_status import WebhookDeliveryStatus
from .webhook_endpoint import WebhookEndpoint
from .webhook_endpoint_attributes import WebhookEndpointAttributes
from .webhook_endpoint_attributes_mode import WebhookEndpointAttributesMode
from .webhook_endpoint_envelope import WebhookEndpointEnvelope
from .webhook_endpoint_envelope_meta import WebhookEndpointEnvelopeMeta
from .webhook_endpoint_list_envelope import WebhookEndpointListEnvelope
from .webhook_endpoint_list_envelope_meta import WebhookEndpointListEnvelopeMeta
from .webhook_endpoint_test_result_envelope import WebhookEndpointTestResultEnvelope
from .webhook_endpoint_test_result_envelope_data import WebhookEndpointTestResultEnvelopeData
from .webhook_endpoint_test_result_envelope_data_error_type_1 import WebhookEndpointTestResultEnvelopeDataErrorType1
from .webhook_endpoint_test_result_envelope_data_error_type_2_type_1 import (
    WebhookEndpointTestResultEnvelopeDataErrorType2Type1,
)
from .webhook_endpoint_test_result_envelope_data_error_type_3_type_1 import (
    WebhookEndpointTestResultEnvelopeDataErrorType3Type1,
)
from .webhook_endpoint_test_result_envelope_data_payload import WebhookEndpointTestResultEnvelopeDataPayload
from .webhook_endpoint_test_result_envelope_meta import WebhookEndpointTestResultEnvelopeMeta
from .webhook_subscription import WebhookSubscription
from .webhook_subscription_envelope import WebhookSubscriptionEnvelope
from .webhook_subscription_events_item import WebhookSubscriptionEventsItem
from .webhook_subscription_list_envelope import WebhookSubscriptionListEnvelope
from .webhook_subscription_list_envelope_meta import WebhookSubscriptionListEnvelopeMeta
from .webhook_subscription_with_recent_deliveries_envelope import WebhookSubscriptionWithRecentDeliveriesEnvelope
from .webhook_subscription_with_recent_deliveries_envelope_data import (
    WebhookSubscriptionWithRecentDeliveriesEnvelopeData,
)
from .webhook_subscription_with_secret_2_envelope import WebhookSubscriptionWithSecret2Envelope
from .webhook_subscription_with_secret_2_envelope_data import WebhookSubscriptionWithSecret2EnvelopeData
from .webhook_subscription_with_secret_envelope import WebhookSubscriptionWithSecretEnvelope
from .webhook_subscription_with_secret_envelope_data import WebhookSubscriptionWithSecretEnvelopeData
from .webhook_test_result import WebhookTestResult
from .webhook_test_result_envelope import WebhookTestResultEnvelope
from .webhook_test_result_payload_preview import WebhookTestResultPayloadPreview
from .wefunder_round import WefunderRound
from .wefunder_round_status import WefunderRoundStatus

__all__ = (
    "AnonymizedAttribution",
    "AnonymizedAttributionAmountTier",
    "AnonymizedAttributionAttribution",
    "AnonymizedAttributionAttributionQualityScore",
    "AnonymizedAttributionAttributionTimeToInvestBucket",
    "AnonymizedAttributionStatus",
    "AnonymizedAttributionStatusBucket",
    "AttributedInvestmentListEnvelope",
    "AttributedInvestmentListEnvelopeMeta",
    "AttributedInvestmentListEnvelopeMetaDetailLevel",
    "AttributionCampaignAccess",
    "AttributionCampaignSummary",
    "AttributionCampaignSummaryListEnvelope",
    "AttributionMe",
    "AttributionMeEnvelope",
    "AttributionPartnerType0",
    "AttributionPartnerType0Status",
    "AttributionStats",
    "AttributionStatsByCampaignItem",
    "AttributionStatsBySourceItem",
    "AttributionStatsEnvelope",
    "AttributionStatsPeriod",
    "AttributionStatsQualityBreakdown",
    "AttributionStatsTotals",
    "AttributionUser",
    "AuditEvent",
    "AuditEventAttributes",
    "AuditEventAttributesNewValuesType0",
    "AuditEventAttributesOldValuesType0",
    "AuditEventAttributesStatus",
    "AuditEventListEnvelope",
    "BulkInviteLinkCreateInput",
    "BulkInviteLinkEnvelope",
    "BulkInviteLinkEnvelopeErrorsItem",
    "BulkInviteLinkEnvelopeMeta",
    "Campaign",
    "CampaignAttributes",
    "CampaignListEnvelope",
    "CommentProposalEnvelope",
    "CommentProposalEnvelopeDraftType0",
    "CommentProposalEnvelopeDraftType0Params",
    "CommentProposalEnvelopeProposal",
    "CommentProposalEnvelopeProposalTargetType",
    "CommentProposalEnvelopeRelatedQuestionsItem",
    "Company",
    "CompanyAttributes",
    "CompanyAttributesLocation",
    "CompanyDisclosures",
    "CompanyDisclosuresAttributes",
    "CompanyDisclosuresAttributesBusiness",
    "CompanyDisclosuresAttributesCapitalStructureType0Item",
    "CompanyDisclosuresAttributesCurrentPosition",
    "CompanyDisclosuresAttributesFiling",
    "CompanyDisclosuresAttributesFinancialStatements",
    "CompanyDisclosuresAttributesOutstandingDebtsType0",
    "CompanyDisclosuresAttributesOutstandingDebtsType0ItemsItem",
    "CompanyDisclosuresAttributesOutstandingNotesType0Item",
    "CompanyDisclosuresAttributesPriorOfferingsType0Item",
    "CompanyDisclosuresAttributesRatiosType0",
    "CompanyDisclosuresAttributesRelatedPartiesType0",
    "CompanyDisclosuresAttributesRelatedPartiesType0PartiesItem",
    "CompanyDisclosuresAttributesUseOfFundsType0Item",
    "CompanyDisclosuresAttributesVotingPowerType0Item",
    "CompanyDisclosuresEnvelope",
    "CompanyDisclosuresType",
    "CompanyEnvelope",
    "CompanyPitch",
    "CompanyPitchAttributes",
    "CompanyPitchAttributesAuthoredBy",
    "CompanyPitchAttributesPerksType0",
    "CompanyPitchAttributesStory",
    "CompanyPitchEnvelope",
    "CompanyPitchType",
    "CompanyQuestion",
    "CompanyQuestionAttributes",
    "CompanyQuestionAttributesAnswersItem",
    "CompanyQuestionAttributesMatch",
    "CompanyQuestionListEnvelope",
    "CompanyQuestionListEnvelopeMeta",
    "CompanyQuestionPerson",
    "CompanyQuestionType",
    "CompanySearchResult",
    "CompanySearchResultAttributes",
    "CompanySearchResultListEnvelope",
    "CompanySearchResultListEnvelopeMeta",
    "CompanySearchResultType",
    "CompanyTotals",
    "CompanyUpdate",
    "CompanyUpdateAttributes",
    "CompanyUpdateAttributesAuthorType0",
    "CompanyUpdateAttributesVisibilityType1",
    "CompanyUpdateAttributesVisibilityType2Type1",
    "CompanyUpdateAttributesVisibilityType3Type1",
    "CompanyUpdateEnvelope",
    "CompanyUpdateListEnvelope",
    "CompanyUpdateListEnvelopeMeta",
    "CompanyUpdateType",
    "ConnectedApp",
    "ConnectedAppAttributes",
    "ConnectedAppListEnvelope",
    "ConnectedAppRevocation",
    "ConnectedAppRevocationEnvelope",
    "ConvertibleNoteSecurity",
    "ConvertibleNoteSecurityTerms",
    "ConvertibleNoteSecurityType",
    "CreateInstallationBody",
    "CreateInstallationBodyTargetType",
    "CreateInstallationTokenBody",
    "CreateIntentBody",
    "CreateIntentBodyActionName",
    "CreateIntentBodyParams",
    "CreatePartnerInviteBody",
    "CreatePartnerInviteBodyDirection",
    "CreateWebhookEndpointBody",
    "CreateWebhookEndpointBodyEventsItem",
    "CreateWebhookEndpointBodyMode",
    "CreateWebhookSubscriptionBody",
    "CreateWebhookSubscriptionBodyEventsItem",
    "CurrentRaise",
    "DealInvestor",
    "DealInvestorAttributes",
    "DealInvestorAttributesStatus",
    "DealInvestorListEnvelope",
    "DealInvestorListEnvelopeMeta",
    "DebtSecurity",
    "DebtSecurityTerms",
    "DebtSecurityType",
    "DeleteWebhookEndpointResponse200",
    "DeleteWebhookEndpointResponse200Data",
    "DisclosureDocument",
    "DisclosurePerson",
    "EligibleTargetListEnvelope",
    "EligibleTargetListEnvelopeDataItem",
    "EligibleTargetListEnvelopeDataItemType",
    "EligibleTargetListEnvelopeMeta",
    "EquitySecurity",
    "EquitySecurityTerms",
    "EquitySecurityTermsShareClassType1",
    "EquitySecurityTermsShareClassType2Type1",
    "EquitySecurityTermsShareClassType3Type1",
    "EquitySecurityType",
    "Error",
    "ErrorError",
    "ErrorErrorDetails",
    "Exemption",
    "ExemptionFamily",
    "FiscalYearFinancials",
    "FollowedCompany",
    "FollowedCompanyAttributes",
    "FollowedCompanyListEnvelope",
    "FollowedCompanyType",
    "FollowStateEnvelope",
    "FollowStateEnvelopeData",
    "FollowStateEnvelopeDataAttributes",
    "FollowStateEnvelopeDataType",
    "FullAttribution",
    "FullAttributionAttribution",
    "FullAttributionAttributionQualityScore",
    "FullAttributionAttributionTimeToInvestBucket",
    "FullAttributionInvestor",
    "FullAttributionStatus",
    "FullAttributionStatusBucket",
    "FundSecurity",
    "FundSecurityTerms",
    "FundSecurityType",
    "GetCompanyDisclosuresSectionsItem",
    "GetCompanyPitchSectionsItem",
    "GetPortfolioStatus",
    "GetSyndicatePortfolioStatus",
    "Installation",
    "InstallationAttributes",
    "InstallationAttributesStatus",
    "InstallationAttributesTarget",
    "InstallationAttributesTargetType",
    "InstallationEnvelope",
    "InstallationEnvelopeMeta",
    "InstallationListEnvelope",
    "InstallationListEnvelopeMeta",
    "InstallationTokenEnvelope",
    "InstallationTokenEnvelopeMeta",
    "InstallationTokenEnvelopeToken",
    "Intent",
    "IntentAttributes",
    "IntentAttributesExecutionResultType0",
    "IntentAttributesStatus",
    "IntentEnvelope",
    "IntentListEnvelope",
    "IntentPreviewEnvelope",
    "IntentPreviewEnvelopeData",
    "IntentPreviewEnvelopeDataAttributes",
    "IntentPreviewEnvelopeDataAttributesParams",
    "IntentPreviewEnvelopeDataType",
    "IntentReview",
    "InvestmentChangeListEnvelope",
    "InvestmentChangeListEnvelopeMeta",
    "InvestmentChangeListEnvelopeMetaMode",
    "InvestmentDeltaRecord",
    "InvestmentDeltaRecordAmounts",
    "InvestmentDeltaRecordBlockersItem",
    "InvestmentDeltaRecordContractsItem",
    "InvestmentDeltaRecordInvestor",
    "InvestmentDeltaRecordInvestorAddress",
    "InvestmentDeltaRecordReason",
    "InvestmentDeltaRecordStatus",
    "InvestmentEnvelope",
    "InvestmentEnvelopeMeta",
    "InvestmentEnvelopeMetaSource",
    "InvestmentListEnvelope",
    "InvestmentListEnvelopeMeta",
    "InvestmentListEnvelopeMetaMode",
    "InvestmentSession",
    "InvestmentSessionAttributes",
    "InvestmentSessionAttributesEventsItem",
    "InvestmentSessionAttributesFundingStatus",
    "InvestmentSessionAttributesKycStatus",
    "InvestmentSessionAttributesMetadata",
    "InvestmentSessionAttributesStatus",
    "InvestmentSessionCreateInput",
    "InvestmentSessionCreateInputMetadataType0",
    "InvestmentSessionEnvelope",
    "InvestmentSessionEnvelopeMeta",
    "InvestmentSessionListEnvelope",
    "InvestmentSessionListEnvelopeMeta",
    "Investor",
    "InvestorAttributes",
    "InvestorEnvelope",
    "InvestorListEnvelope",
    "InviteLink",
    "InviteLinkAttributes",
    "InviteLinkAttributesEventsItem",
    "InviteLinkAttributesStatus",
    "InviteLinkCreateInput",
    "InviteLinkEnvelope",
    "InviteLinkEnvelopeMeta",
    "InviteLinkListEnvelope",
    "InviteLinkListEnvelopeMeta",
    "InviteLinkUpdateInput",
    "InviteSyndicateMemberBody",
    "InviteSyndicateMemberBodySyndicatePermission",
    "ListActivityStatus",
    "ListAttributedInvestmentsDetailLevel",
    "ListCompanyQuestionsSort",
    "ListEligibleInstallTargetsTargetType",
    "ListIntentsStatus",
    "ListInvestmentsStatus",
    "ListOfferingsBusinessModelItem",
    "ListOfferingsExemption",
    "ListOfferingsIndustryItem",
    "ListOfferingsSecurity",
    "ListOfferingsSort",
    "ListPortfolioPositionsStatus",
    "ListSyndicateMembersAccredited",
    "ListSyndicateMembersHasInvested",
    "ListSyndicateMembersPermission",
    "ListSyndicateMembersSort",
    "ListSyndicatePortfolioPositionsStatus",
    "MarketingPartner",
    "MarketingPartnerEnvelope",
    "MarketingPartnerStatus",
    "MemberInvestment",
    "MemberInvestmentAttributes",
    "MemberInvestmentAttributesStatus",
    "MemberInvestmentListEnvelope",
    "MemberInvestmentListEnvelopeMeta",
    "MyCompany",
    "MyCompanyAttributes",
    "MyCompanyListEnvelope",
    "MyCompanyListEnvelopeMeta",
    "MyCompanyType",
    "Offering",
    "OfferingAttributes",
    "OfferingAttributesIntendedSecurityType0",
    "OfferingAttributesIntendedSecurityType0Type",
    "OfferingAttributesStatus",
    "OfferingEnvelope",
    "OfferingListEnvelope",
    "OfferingListEnvelopeMeta",
    "OfferingListEnvelopeMetaFilters",
    "OfferingStatsEnvelope",
    "OfferingStatsEnvelopeData",
    "OfferingStatsEnvelopeDataByStatus",
    "OfferingStatsEnvelopeDataByStatusAdditionalProperty",
    "OfferingStatsEnvelopeDataTotal",
    "OfferingStatsEnvelopeMeta",
    "OfferingStatsEnvelopeMetaSource",
    "OfferingWarningsItem",
    "OfferingWarningsItemCode",
    "OtherSecurity",
    "OtherSecurityTerms",
    "OtherSecurityType",
    "PaginationMeta",
    "PartnerInvestment",
    "PartnerInvestmentAttributes",
    "PartnerInvestmentAttributesAccreditationType0",
    "PartnerInvestmentAttributesAccreditationType0Status",
    "PartnerInvestmentAttributesAccreditationType0Type",
    "PartnerInvestmentAttributesStatus",
    "PartnerInvestmentEnvelope",
    "PartnerInvestmentListEnvelope",
    "PartnerInvestor",
    "PartnerInvestorAttributes",
    "PartnerInvestorListEnvelope",
    "PartnerInvite",
    "PartnerInviteDirection",
    "PartnerInviteEnvelope",
    "PartnerInviteListEnvelope",
    "PartnerInviteStatus",
    "PartnerWebhookEvent",
    "PartnerWebhookEventData",
    "PartnerWebhookEventEnvelope",
    "PartnerWebhookSubscription",
    "PartnerWebhookSubscriptionAttributes",
    "PartnerWebhookSubscriptionCreateInput",
    "PartnerWebhookSubscriptionEnvelope",
    "PartnerWebhookSubscriptionListEnvelope",
    "PartnerWebhookSubscriptionWithSecret",
    "PartnerWebhookSubscriptionWithSecretAttributes",
    "PartnerWebhookSubscriptionWithSecretEnvelope",
    "PastRound",
    "PastRoundSource",
    "PerkTier",
    "PitchBlock",
    "PitchBlockLinksItem",
    "PitchBlockType",
    "PortfolioCompanyRef",
    "PortfolioHolding",
    "PortfolioHoldingStatus",
    "PortfolioPosition",
    "PortfolioPositionAttributes",
    "PortfolioPositionAttributesAssetType",
    "PortfolioPositionAttributesExitReason",
    "PortfolioPositionAttributesStatus",
    "PortfolioPositionListEnvelope",
    "PortfolioPositionListEnvelopeMeta",
    "PortfolioPositionType",
    "PortfolioSecurity",
    "PortfolioSecurityOwnerType0",
    "PortfolioSecurityOwnerType0Kind",
    "PortfolioSecurityTerms",
    "PortfolioSummaryEnvelope",
    "PortfolioSummaryEnvelopeData",
    "PortfolioSummaryEnvelopeDataAttributes",
    "PortfolioSummaryEnvelopeDataAttributesPositionCounts",
    "PreviewIntentBody",
    "PreviewIntentBodyParams",
    "RegisterAsPartnerBody",
    "ReorderSyndicateMembersBody",
    "RevenueShareSecurity",
    "RevenueShareSecurityTerms",
    "RevenueShareSecurityTermsRevenueBasisType1",
    "RevenueShareSecurityTermsRevenueBasisType2Type1",
    "RevenueShareSecurityTermsRevenueBasisType3Type1",
    "RevenueShareSecurityType",
    "SafeSecurity",
    "SafeSecurityTerms",
    "SafeSecurityType",
    "SecuritySummary",
    "SecuritySummaryType",
    "Spv",
    "SpvAttributes",
    "SpvAttributesMetadata",
    "SpvAttributesStatus",
    "SpvAttributesTargetCompany",
    "SpvCancelIntentEnvelope",
    "SpvCancelIntentEnvelopeMeta",
    "SpvCloseIntentEnvelope",
    "SpvCloseIntentEnvelopeMeta",
    "SpvCreateInput",
    "SpvCreateInputMetadata",
    "SpvEnvelope",
    "SpvListEnvelope",
    "SpvMetrics",
    "SpvSettings",
    "SpvSettingsAccreditationType",
    "SpvStatus",
    "SpvStatusAttributes",
    "SpvStatusAttributesStatus",
    "SpvStatusEnvelope",
    "SpvStatusEnvelopeMeta",
    "SpvTerms",
    "SpvTermsSafeType",
    "SpvTermsStructure",
    "SpvWithMetaEnvelope",
    "SpvWithMetaEnvelopeMeta",
    "Syndicate",
    "SyndicateAttributes",
    "SyndicateDeal",
    "SyndicateDealAttributes",
    "SyndicateDealAttributesStatus",
    "SyndicateDealCloseIntentEnvelope",
    "SyndicateDealCloseIntentEnvelopeMeta",
    "SyndicateDealDetailEnvelope",
    "SyndicateDealEnvelope",
    "SyndicateDealFinalizeIntentEnvelope",
    "SyndicateDealFinalizeIntentEnvelopeMeta",
    "SyndicateDealListEnvelope",
    "SyndicateDealListEnvelopeMeta",
    "SyndicateDetailEnvelope",
    "SyndicateListEnvelope",
    "SyndicateMember",
    "SyndicateMemberAttributes",
    "SyndicateMemberAttributesSyndicatePermission",
    "SyndicateMemberEnvelope",
    "SyndicateMemberListEnvelope",
    "SyndicatePortfolioSummaryEnvelope",
    "SyndicatePortfolioSummaryEnvelopeData",
    "SyndicatePortfolioSummaryEnvelopeDataAttributes",
    "SyndicatePortfolioSummaryEnvelopeDataAttributesDealCounts",
    "SyndicateStatistics",
    "SyndicateStatisticsAttributes",
    "SyndicateStatisticsAttributesMembersByRole",
    "SyndicateStatisticsEnvelope",
    "TagRef",
    "TargetCompanyInput",
    "TestWebhookEndpointBody",
    "TestWebhookEndpointBodyEvent",
    "UpdateSyndicateBody",
    "UpdateSyndicateBodySyndicate",
    "UpdateSyndicateMemberBody",
    "UpdateSyndicateMemberBodyMember",
    "UpdateWebhookEndpointBody",
    "UpdateWebhookEndpointBodyEventsItem",
    "User",
    "UserAttributes",
    "UserEnvelope",
    "ValidationError",
    "ValidationErrorError",
    "ValidationErrorErrorDetailsItem",
    "WebhookDelivery",
    "WebhookDeliveryStatus",
    "WebhookEndpoint",
    "WebhookEndpointAttributes",
    "WebhookEndpointAttributesMode",
    "WebhookEndpointEnvelope",
    "WebhookEndpointEnvelopeMeta",
    "WebhookEndpointListEnvelope",
    "WebhookEndpointListEnvelopeMeta",
    "WebhookEndpointTestResultEnvelope",
    "WebhookEndpointTestResultEnvelopeData",
    "WebhookEndpointTestResultEnvelopeDataErrorType1",
    "WebhookEndpointTestResultEnvelopeDataErrorType2Type1",
    "WebhookEndpointTestResultEnvelopeDataErrorType3Type1",
    "WebhookEndpointTestResultEnvelopeDataPayload",
    "WebhookEndpointTestResultEnvelopeMeta",
    "WebhookSubscription",
    "WebhookSubscriptionEnvelope",
    "WebhookSubscriptionEventsItem",
    "WebhookSubscriptionListEnvelope",
    "WebhookSubscriptionListEnvelopeMeta",
    "WebhookSubscriptionWithRecentDeliveriesEnvelope",
    "WebhookSubscriptionWithRecentDeliveriesEnvelopeData",
    "WebhookSubscriptionWithSecret2Envelope",
    "WebhookSubscriptionWithSecret2EnvelopeData",
    "WebhookSubscriptionWithSecretEnvelope",
    "WebhookSubscriptionWithSecretEnvelopeData",
    "WebhookTestResult",
    "WebhookTestResultEnvelope",
    "WebhookTestResultPayloadPreview",
    "WefunderRound",
    "WefunderRoundStatus",
)
