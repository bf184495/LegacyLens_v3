"""
registry.py

Module Registry for LegacyLens V3.

The ModuleRegistry maintains a collection of
ModuleManifest objects and provides querying
and lookup services for the platform.

Used by:

- Home Screen
- Module Loader
- Navigation System
- Future Plugin Architecture
"""

from typing import Dict

from .manifest import ModuleManifest


class ModuleRegistry:
    """
    Central registry of available modules.
    """

    def __init__(self) -> None:

        self._modules: Dict[
            str,
            ModuleManifest
        ] = {}

    def register(
        self,
        manifest: ModuleManifest
    ) -> None:
        """
        Register a module.
        """

        if manifest.module_id in self._modules:

            raise ValueError(
                f"Module already registered: "
                f"{manifest.module_id}"
            )

        self._modules[
            manifest.module_id
        ] = manifest

    def unregister(
        self,
        module_id: str
    ) -> None:
        """
        Remove a module from the registry.
        """

        self._modules.pop(
            module_id,
            None
        )

    def get(
        self,
        module_id: str
    ) -> ModuleManifest | None:
        """
        Retrieve a specific module.
        """

        return self._modules.get(
            module_id
        )

    def exists(
        self,
        module_id: str
    ) -> bool:
        """
        Determine whether a module exists.
        """

        return module_id in self._modules

    def all_modules(
        self
    ) -> list[ModuleManifest]:
        """
        Return all registered modules.
        """

        return sorted(
            self._modules.values(),
            key=lambda m: m.name
        )

    def enabled_modules(
        self
    ) -> list[ModuleManifest]:
        """
        Return enabled modules.
        """

        return sorted(
            (
                m
                for m in self._modules.values()
                if m.enabled
            ),
            key=lambda m: m.name
        )

    def visible_modules(
        self
    ) -> list[ModuleManifest]:
        """
        Return modules shown in the UI.
        """

        return sorted(
            (
                m
                for m in self._modules.values()
                if m.visible
            ),
            key=lambda m: m.name
        )

    def count(self) -> int:
        """
        Return registered module count.
        """

        return len(
            self._modules
        )

    def clear(self) -> None:
        """
        Remove all registered modules.
        """

        self._modules.clear()