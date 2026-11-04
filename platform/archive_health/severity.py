"""
severity.py

Archive Health severity definitions.

This module provides standardized severity levels
used across all LegacyLens modules.

Examples:

- Missing EXIF
- Duplicate Contact
- Corrupt Document
- Broken Email Export

All health findings should use these values.
"""

from enum import StrEnum


class Severity(StrEnum):
    """
    Standardized health issue severity levels.
    """

    INFO = "info"

    WARNING = "warning"

    ERROR = "error"

    CRITICAL = "critical"