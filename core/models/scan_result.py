"""
scan_result.py

Shared scan result model for LegacyLens V3.

ScanResult represents the outcome of a module scan,
analysis operation, import process, or inventory run.

Examples:

- Photo archive scan
- Contact import
- Email inventory
- Document analysis
- Calendar processing

Used by:

- Platform Dashboard
- Reporting Engine
- Archive Health Engine
- Progress Tracking
- Future Activity History
"""

from dataclasses import dataclass, field
from datetime import datetime

from .health_issue import HealthIssue


@dataclass(slots=True)
class ScanResult:
    """
    Represents the result of a completed scan.
    """

    scan_id: str

    module: str

    started_at: datetime

    completed_at: datetime | None = None

    success: bool = True

    source_path: str = ""

    total_items: int = 0

    processed_items: int = 0

    skipped_items: int = 0

    healthy_items: int = 0

    warning_items: int = 0

    error_items: int = 0

    health_issues: list[HealthIssue] = field(
        default_factory=list
    )

    messages: list[str] = field(
        default_factory=list
    )

    elapsed_seconds: float = 0.0