"""
LegacyLens V3 Module Registry

Provides:

- ModuleManifest
- ModuleRegistry
- ModuleLoader
"""

from .manifest import ModuleManifest
from .registry import ModuleRegistry
from .loader import ModuleLoader


__all__ = [
    "ModuleManifest",
    "ModuleRegistry",
    "ModuleLoader",
]