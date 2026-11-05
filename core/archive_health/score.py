"""
score.py

Archive Health scoring utilities.

This module converts HealthIssue collections into
numeric health scores suitable for:

- Dashboards
- Reports
- Module Summaries
- Archive Summaries

Scoring Range:

100 = Perfect

0 = Severely Degraded
"""

from core.models import HealthIssue
from .severity import Severity


class ArchiveHealthScore:
    """
    Calculates Archive Health scores from
    registered health issues.
    """

    INFO_PENALTY = 0.25

    WARNING_PENALTY = 1.00

    ERROR_PENALTY = 5.00

    CRITICAL_PENALTY = 10.00

    @classmethod
    def calculate(
        cls,
        issues: list[HealthIssue]
    ) -> float:
        """
        Calculate an archive health score.

        Returns a value between 0 and 100.
        """

        score = 100.0

        for issue in issues:

            if issue.severity == Severity.INFO:
                score -= cls.INFO_PENALTY

            elif issue.severity == Severity.WARNING:
                score -= cls.WARNING_PENALTY

            elif issue.severity == Severity.ERROR:
                score -= cls.ERROR_PENALTY

            elif issue.severity == Severity.CRITICAL:
                score -= cls.CRITICAL_PENALTY

        return max(score, 0.0)

    @classmethod
    def rating(
        cls,
        score: float
    ) -> str:
        """
        Convert a numeric score into
        a human-readable rating.
        """

        if score >= 90:
            return "Excellent"

        if score >= 80:
            return "Good"

        if score >= 70:
            return "Fair"

        if score >= 60:
            return "Poor"

        return "Critical"