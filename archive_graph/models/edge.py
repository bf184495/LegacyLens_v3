from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Edge:
    """
    Represents a relationship between two graph nodes.
    """

    id: str
    relationship_type: str

    source_id: str
    target_id: str

    confidence: float = 1.0

    metadata: dict[str, Any] = field(default_factory=dict)