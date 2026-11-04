"""
LegacyLens V3 Workspaces
"""

from .base_workspace import BaseWorkspace
from .photos_workspace import PhotosWorkspace
from .contacts_workspace import ContactsWorkspace
from .archive_health_workspace import (
    ArchiveHealthWorkspace,
)

__all__ = [
    "BaseWorkspace",
    "PhotosWorkspace",
    "ContactsWorkspace",
    "ArchiveHealthWorkspace",
]
