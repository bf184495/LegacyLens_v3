"""
archive_item.py

Core archive object used throughout LegacyLens V3.

Every module-specific record ultimately derives from the
ArchiveItem concept.

Examples:

- Photo
- Contact
- Document
- Email
- Calendar Event

ArchiveItem provides common metadata used across all
modules.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class ArchiveItem:
    """
    Base archive object.

    Represents any item stored, imported,
    analyzed, or referenced within the
    LegacyLens ecosystem.
    """

    item_id: str

    module: str

    title: str

    source_path: str = ""

    created_at: datetime | None = None

    modified_at: datetime | None = None

    tags: list[str] = field(
        default_factory=list
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    notes: str = ""

    archived: bool = False

    favorite: bool = False
