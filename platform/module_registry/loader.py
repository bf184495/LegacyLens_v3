"""
loader.py

Module loading services for LegacyLens V3.

The ModuleLoader is responsible for loading
registered modules from their manifest
entry points.

Future responsibilities:

- Dynamic module loading
- Plugin loading
- Dependency validation
- Startup orchestration

Current responsibilities:

- Resolve registered modules
- Import entry point modules
- Provide basic module loading
"""

from importlib import import_module

from .manifest import ModuleManifest
from .registry import ModuleRegistry


class ModuleLoader:
    """
    Loads LegacyLens modules from
    registered manifests.
    """

    def __init__(
        self,
        registry: ModuleRegistry
    ) -> None:

        self.registry = registry

    def load(
        self,
        module_id: str
    ):
        """
        Load a module from its manifest.

        Returns:
            Imported Python module

        Raises:
            ValueError
            ImportError
        """

        manifest = self.registry.get(
            module_id
        )

        if manifest is None:

            raise ValueError(
                f"Unknown module: {module_id}"
            )

        return import_module(
            manifest.entry_point
        )

    def load_all_enabled(self) -> dict:
        """
        Load all enabled modules.

        Returns:
            Dictionary of loaded modules.
        """

        loaded_modules = {}

        for manifest in self.registry.enabled_modules():

            try:

                loaded_modules[
                    manifest.module_id
                ] = import_module(
                    manifest.entry_point
                )

            except ImportError as exc:

                print(
                    f"Failed to load "
                    f"{manifest.module_id}: "
                    f"{exc}"
                )

        return loaded_modules

    def validate_dependencies(
        self,
        manifest: ModuleManifest
    ) -> bool:
        """
        Verify dependencies exist within
        the registry.

        Returns:
            True if dependencies are valid.
        """

        for dependency in manifest.dependencies:

            if not self.registry.exists(
                dependency
            ):

                return False

        return True