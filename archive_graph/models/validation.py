from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ValidationNode:
    """
    Records a validation activity
    performed by a user.
    """

    id: str

    action: str

    user: str

    timestamp: datetime | None = None

    confidence_before: float = 0.0

    confidence_after: float = 0.0

    notes: str = ""

    metadata: dict = field(default_factory=dict)