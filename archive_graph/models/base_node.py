from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class BaseNode:
    id: str

    created_at: datetime | None = None
    updated_at: datetime | None = None

    confidence: float = 1.0

    metadata: dict = field(default_factory=dict)