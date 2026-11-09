from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class EventNode:
    id: str

    title: str

    start_date: datetime | None = None
    end_date: datetime | None = None

    confidence: float = 0.0

    status: str = "inferred"

    summary: str = ""

    metadata: dict = field(default_factory=dict)