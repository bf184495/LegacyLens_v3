"""
LegacyLens V3 Platform Models

This package contains the shared data models used
throughout the LegacyLens platform.

Modules should import models from this package
instead of importing individual model files
directly whenever practical.

Example:

    from platform.models import (
        ArchiveItem,
        HealthIssue,
        HealthReport,
    )
"""

from .archive_item import ArchiveItem
from .health_issue import HealthIssue
from .health_report import HealthReport
from .relationship import Relationship
from .module_info import ModuleInfo
from .timeline_event import TimelineEvent
from .scan_result import ScanResult


__all__ = [
    "ArchiveItem",
    "HealthIssue",
    "HealthReport",
    "Relationship",
    "ModuleInfo",
    "TimelineEvent",
    "ScanResult",
]