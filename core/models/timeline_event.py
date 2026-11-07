"""
timeline_event.py

Shared timeline event model for LegacyLens V3.

TimelineEvent provides a unified way to represent
events across all modules.

Examples:

- Photo captured
- Contact created
- Email sent
- Meeting attended
- Document authored

Timeline events will ultimately power:

- Archive timelines
- Life histories
- Historical narratives
- Knowledge engine outputs
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class TimelineEvent:
    """
    Represents a significant event within
    a digital archive.
    """

    event_id: str

    title: str

    timestamp: datetime

    source_module: str

    event_type: str

    description: str = ""

    item_id: str = ""

    source_path: str = ""

    confidence: float = 1.0

    tags: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )
