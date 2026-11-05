"""
manifest.py

Module manifest definitions for LegacyLens V3.

A ModuleManifest describes a module and
provides the metadata required by:

- Module Registry
- Home Screen
- Navigation
- Future Plugin System
- Module Loader

Every LegacyLens module should expose
exactly one manifest.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ModuleManifest:
    """
    Defines a LegacyLens module.
    """

    module_id: str

    name: str

    version: str

    description: str

    entry_point: str

    enabled: bool = True

    visible: bool = True

    category: str = "core"

    icon: str = ""

    dependencies: list[str] = field(
        default_factory=list
    )

    tags: list[str] = field(
        default_factory=list
    )