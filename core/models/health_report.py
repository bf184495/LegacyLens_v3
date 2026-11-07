"""
health_report.py

Shared archive health report model.

HealthReport aggregates HealthIssue objects and
provides summary statistics for a module, scan,
or entire archive.

Used by:

- Archive Health Engine
- Dashboard
- Reporting
- Scoring
- Module Analysis
"""

from dataclasses import dataclass, field
from datetime import datetime

from .health_issue import HealthIssue


@dataclass(slots=True)
class HealthReport:
    """
    Aggregated health assessment results.
    """

    report_id: str

    module: str

    generated_at: datetime

    score: float = 100.0

    healthy_count: int = 0

    warning_count: int = 0

    error_count: int = 0

    critical_count: int = 0

    total_items: int = 0

    issues: list[HealthIssue] = field(
        default_factory=list
    )

    summary: str = ""

    recommendations: list[str] = field(
        default_factory=list
    )