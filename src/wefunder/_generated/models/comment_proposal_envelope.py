from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comment_proposal_envelope_draft_type_0 import CommentProposalEnvelopeDraftType0
    from ..models.comment_proposal_envelope_proposal import CommentProposalEnvelopeProposal
    from ..models.comment_proposal_envelope_related_questions_item import CommentProposalEnvelopeRelatedQuestionsItem


T = TypeVar("T", bound="CommentProposalEnvelope")


@_attrs_define
class CommentProposalEnvelope:
    """What propose_comment returns — a dry run of comments.create plus the context an agent needs before minting.

    Attributes:
        proposal (CommentProposalEnvelopeProposal | Unset): The arguments, as normalized, to pass to
            write_comment_intent once the user confirms.
        allowed (bool | Unset):
        refusal (None | str | Unset): The handler's reason when `allowed` is false.
        draft (CommentProposalEnvelopeDraftType0 | None | Unset): The dry run (null when `allowed` is false). Same shape
            as IntentPreviewEnvelope's attributes.
        related_questions (list[CommentProposalEnvelopeRelatedQuestionsItem] | Unset):
        drafting_guidelines (str | Unset):
        next_step (str | Unset):
    """

    proposal: CommentProposalEnvelopeProposal | Unset = UNSET
    allowed: bool | Unset = UNSET
    refusal: None | str | Unset = UNSET
    draft: CommentProposalEnvelopeDraftType0 | None | Unset = UNSET
    related_questions: list[CommentProposalEnvelopeRelatedQuestionsItem] | Unset = UNSET
    drafting_guidelines: str | Unset = UNSET
    next_step: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.comment_proposal_envelope_draft_type_0 import CommentProposalEnvelopeDraftType0  # noqa: PLC0415

        proposal: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proposal, Unset):
            proposal = self.proposal.to_dict()

        allowed = self.allowed

        refusal: None | str | Unset
        if isinstance(self.refusal, Unset):
            refusal = UNSET
        else:
            refusal = self.refusal

        draft: dict[str, Any] | None | Unset
        if isinstance(self.draft, Unset):
            draft = UNSET
        elif isinstance(self.draft, CommentProposalEnvelopeDraftType0):
            draft = self.draft.to_dict()
        else:
            draft = self.draft

        related_questions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.related_questions, Unset):
            related_questions = []
            for related_questions_item_data in self.related_questions:
                related_questions_item = related_questions_item_data.to_dict()
                related_questions.append(related_questions_item)

        drafting_guidelines = self.drafting_guidelines

        next_step = self.next_step

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proposal is not UNSET:
            field_dict["proposal"] = proposal
        if allowed is not UNSET:
            field_dict["allowed"] = allowed
        if refusal is not UNSET:
            field_dict["refusal"] = refusal
        if draft is not UNSET:
            field_dict["draft"] = draft
        if related_questions is not UNSET:
            field_dict["related_questions"] = related_questions
        if drafting_guidelines is not UNSET:
            field_dict["drafting_guidelines"] = drafting_guidelines
        if next_step is not UNSET:
            field_dict["next_step"] = next_step

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.comment_proposal_envelope_draft_type_0 import CommentProposalEnvelopeDraftType0  # noqa: PLC0415
        from ..models.comment_proposal_envelope_proposal import CommentProposalEnvelopeProposal  # noqa: PLC0415
        from ..models.comment_proposal_envelope_related_questions_item import (
            CommentProposalEnvelopeRelatedQuestionsItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _proposal = d.pop("proposal", UNSET)
        proposal: CommentProposalEnvelopeProposal | Unset
        if isinstance(_proposal, Unset):
            proposal = UNSET
        else:
            proposal = CommentProposalEnvelopeProposal.from_dict(_proposal)

        allowed = d.pop("allowed", UNSET)

        def _parse_refusal(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        refusal = _parse_refusal(d.pop("refusal", UNSET))

        def _parse_draft(data: object) -> CommentProposalEnvelopeDraftType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                draft_type_0 = CommentProposalEnvelopeDraftType0.from_dict(data)

                return draft_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CommentProposalEnvelopeDraftType0 | None | Unset, data)

        draft = _parse_draft(d.pop("draft", UNSET))

        _related_questions = d.pop("related_questions", UNSET)
        related_questions: list[CommentProposalEnvelopeRelatedQuestionsItem] | Unset = UNSET
        if _related_questions is not UNSET:
            related_questions = []
            for related_questions_item_data in _related_questions:
                related_questions_item = CommentProposalEnvelopeRelatedQuestionsItem.from_dict(
                    related_questions_item_data
                )

                related_questions.append(related_questions_item)

        drafting_guidelines = d.pop("drafting_guidelines", UNSET)

        next_step = d.pop("next_step", UNSET)

        comment_proposal_envelope = cls(
            proposal=proposal,
            allowed=allowed,
            refusal=refusal,
            draft=draft,
            related_questions=related_questions,
            drafting_guidelines=drafting_guidelines,
            next_step=next_step,
        )

        comment_proposal_envelope.additional_properties = d
        return comment_proposal_envelope

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
