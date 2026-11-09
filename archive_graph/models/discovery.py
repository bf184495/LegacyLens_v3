from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class DiscoveryNode:
    """
    Represents something interesting discovered
    by LegacyLens.

    Example:
    - Unknown person cluster
    - Possible family reunion
    - Metadata anomaly
    - Duplicate chain
    """

    id: str

    title: str

    discovery_type: str

    recommendation: str = ""

    severity: str = "medium"

    status: str = "open"

    confidence: float = 0.0

    created_at: datetime | None = None

    metadata: dict = field(default_factory=dict)