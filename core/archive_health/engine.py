"""
engine.py

Archive Health Engine

Coordinates health issue collection,
health scoring, and report generation
across all LegacyLens modules.

Modules submit HealthIssue objects.

The engine produces HealthReport
objects suitable for:

- Dashboards
- Exports
- Health Summaries
- Future Analytics
"""

from datetime import datetime

from core.models import HealthIssue
from core.models import HealthReport

from .issue_registry import IssueRegistry
from .score import ArchiveHealthScore
from .severity import Severity


class ArchiveHealthEngine:
    """
    Central Archive Health coordinator.
    """

    def __init__(self) -> None:

        self.registry = IssueRegistry()

    def add_issue(
        self,
        issue: HealthIssue
    ) -> None:
        """
        Register a single health issue.
        """

        self.registry.add(issue)

    def add_issues(
        self,
        issues: list[HealthIssue]
    ) -> None:
        """
        Register multiple health issues.
        """

        self.registry.add_many(issues)

    def clear(self) -> None:
        """
        Remove all registered issues.
        """

        self.registry.clear()

    def build_report(
        self,
        report_id: str,
        module: str,
        total_items: int = 0
    ) -> HealthReport:
        """
        Create a HealthReport from
        currently registered issues.
        """

        issues = self.registry.issues

        severity_counts = (
            self.registry.count_by_severity()
        )

        score = ArchiveHealthScore.calculate(
            issues
        )

        rating = ArchiveHealthScore.rating(
            score
        )

        report = HealthReport(
            report_id=report_id,
            module=module,
            generated_at=datetime.now(),
            score=score,
            healthy_count=max(
                total_items
                - len(issues),
                0
            ),
            warning_count=severity_counts.get(
                Severity.WARNING,
                0
            ),
            error_count=severity_counts.get(
                Severity.ERROR,
                0
            ),
            critical_count=severity_counts.get(
                Severity.CRITICAL,
                0
            ),
            total_items=total_items,
            issues=issues,
            summary=(
                f"Archive Health Score: "
                f"{score:.2f} ({rating})"
            )
        )

        return report