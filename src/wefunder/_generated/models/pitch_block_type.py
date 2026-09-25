from enum import StrEnum

class PitchBlockType(StrEnum):
    FOOTNOTE = "footnote"
    HEADING = "heading"
    IMAGE = "image"
    LIST = "list"
    PARAGRAPH = "paragraph"
    VIDEO = "video"

    def __str__(self) -> str:
        return str(self.value)
