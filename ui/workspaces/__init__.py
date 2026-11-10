"""
LegacyLens V3 Workspaces
"""

from .base_workspace import BaseWorkspace
from .photos_workspace import PhotosWorkspace
from .contacts_workspace import ContactsWorkspace
from .archive_health_workspace import ArchiveHealthWorkspace
from .workbench_workspace import WorkbenchWorkspace
from .explorer_workspace import ExplorerWorkspace
from .timeline_workspace import TimelineWorkspace


__all__ = [
    "BaseWorkspace",
    "PhotosWorkspace",
    "ContactsWorkspace",
    "ArchiveHealthWorkspace",
    "WorkbenchWorkspace",
    "ExplorerWorkspace"
]
