from dataclasses import dataclass, field


@dataclass(slots=True)
class CollectionNode:
    """
    User-facing grouping of archive content.

    Not tied to folders. Collections may be:
    - Albums
    - Family branches
    - Vacations
    - Historical eras
    - User-created sets
    """

    id: str

    title: str

    description: str = ""

    collection_type: str = "CUSTOM"

    confidence: float = 1.0

    metadata: dict = field(default_factory=dict)