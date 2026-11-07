"""
relationship.py

Shared relationship model for LegacyLens V3.

Relationships connect records across modules
and form the foundation of the future
Relationship Engine and Knowledge Engine.

Examples:

Photo -> Person

Person -> Email

Email -> Calendar Event

Document -> Contact

Contact -> Contact
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Relationship:
    """
    Represents a connection between two
    archive entities.
    """

    relationship_id: str

    source_item_id: str

    target_item_id: str

    relationship_type: str

    source_module: str

    target_module: str

    confidence: float = 1.0

    description: str = ""

    created_at: datetime | None = None

    verified: bool = False