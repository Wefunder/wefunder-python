from enum import StrEnum


class IntentPreviewEnvelopeDataType(StrEnum):
    INTENT_PREVIEW = "intent_preview"

    def __str__(self) -> str:
        return str(self.value)
