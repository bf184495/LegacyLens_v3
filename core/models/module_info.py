"""
module_info.py

Shared module definition model.

ModuleInfo describes a LegacyLens module and
provides metadata used by:

- Home Screen
- Module Registry
- Navigation
- Status Monitoring
- Future Plugin Architecture

Examples:

Photos
Contacts
Documents
Email
Calendar
Knowledge
Archive Health
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class ModuleInfo:
    """
    Defines a LegacyLens module.
    """

    module_id: str

    name: str

    version: str

    description: str

    enabled: bool = True

    visible: bool = True

    icon: str = ""

    category: str = "core"

    entry_point: str = ""

    dependencies: list[str] = field(
        default_factory=list
    )

    tags: list[str] = field(
        default_factory=list
    )