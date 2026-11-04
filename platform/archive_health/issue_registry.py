"""
issue_registry.py

Central registry for archive health findings.

Modules submit HealthIssue objects to the
IssueRegistry. The registry provides
filtering, querying, counting, and reporting
capabilities for the Archive Health system.

Used by:

- Photos
- Contacts
- Documents
- Email
- Calendar
- Knowledge

Future consumers:

- Archive Health Engine
- Dashboard
- Reporting
- Scoring
"""

from collections import defaultdict

from platform.models import HealthIssue


class IssueRegistry:
    """
    Central collection of HealthIssue objects.
    """

    def __init__(self) -> None:

        self._issues: list[HealthIssue] = []

    @property
    def issues(self) -> list[HealthIssue]:
        """
        Return all registered issues.
        """

        return list(self._issues)

    def add(self, issue: HealthIssue) -> None:
        """
        Add a health issue to the registry.
        """

        self._issues.append(issue)

    def add_many(
        self,
        issues: list[HealthIssue]
    ) -> None:
        """
        Add multiple health issues.
        """

        self._issues.extend(issues)

    def clear(self) -> None:
        """
        Remove all issues.
        """

        self._issues.clear()

    def count(self) -> int:
        """
        Return total issue count.
        """

        return len(self._issues)

    def by_module(
        self,
        module: str
    ) -> list[HealthIssue]:
        """
        Return issues for a module.
        """

        return [
            issue
            for issue in self._issues
            if issue.module == module
        ]

    def by_category(
        self,
        category: str
    ) -> list[HealthIssue]:
        """
        Return issues for a category.
        """

        return [
            issue
            for issue in self._issues
            if issue.category == category
        ]

    def by_severity(
        self,
        severity: str
    ) -> list[HealthIssue]:
        """
        Return issues matching severity.
        """

        return [
            issue
            for issue in self._issues
            if issue.severity == severity
        ]

    def unresolved(self) -> list[HealthIssue]:
        """
        Return unresolved issues.
        """

        return [
            issue
            for issue in self._issues
            if not issue.resolved
        ]

    def resolved(self) -> list[HealthIssue]:
        """
        Return resolved issues.
        """

        return [
            issue
            for issue in self._issues
            if issue.resolved
        ]

    def count_by_module(self) -> dict[str, int]:
        """
        Return issue counts per module.
        """

        counts = defaultdict(int)

        for issue in self._issues:
            counts[issue.module] += 1

        return dict(counts)

    def count_by_category(self) -> dict[str, int]:
        """
        Return issue counts per category.
        """

        counts = defaultdict(int)

        for issue in self._issues:
            counts[issue.category] += 1

        return dict(counts)

    def count_by_severity(self) -> dict[str, int]:
        """
        Return issue counts per severity.
        """

        counts = defaultdict(int)

        for issue in self._issues:
            counts[issue.severity] += 1

        return dict(counts)