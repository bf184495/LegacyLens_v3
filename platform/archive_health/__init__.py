"""
LegacyLens V3 Archive Health Package

This package provides shared archive health
functionality used across all LegacyLens modules.

Modules should generally import from this package
rather than individual implementation files.

Example:

    from platform.archive_health import (
        Severity,
    )
"""

from .severity import Severity


__all__ = [
    "Severity",
]