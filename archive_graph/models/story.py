from dataclasses import dataclass, field


@dataclass(slots=True)
class StoryNode:
    """
    Narrative constructed from photos, people,
    locations and events.
    """

    id: str

    title: str

    summary: str = ""

    status: str = "draft"

    confidence: float = 0.0

    metadata: dict = field(default_factory=dict)