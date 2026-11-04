"""
main_window.py

Primary application window for LegacyLens V3.
"""

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)

from ui.home.home_view import HomeView

from platform.module_registry import (
    ModuleRegistry,
    ModuleManifest,
)

from ui.workspaces import (
    PhotosWorkspace,
    ContactsWorkspace,
    ArchiveHealthWorkspace,
)


class MainWindow(QMainWindow):
    """
    Main LegacyLens window.
    """

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "LegacyLens V3"
        )

        self.resize(
            1200,
            800
        )

        self.registry = self._build_registry()

        self.stack = QStackedWidget()

        self.home_view = HomeView(
            self.registry
        )

        self.home_view.module_selected.connect(
            self.open_workspace
        )

        self.photos_workspace = (
            PhotosWorkspace()
        )

        self.contacts_workspace = (
            ContactsWorkspace()
        )

        self.archive_health_workspace = (
            ArchiveHealthWorkspace()
        )

        self.photos_workspace.home_requested.connect(
            self.show_home
        )

        self.contacts_workspace.home_requested.connect(
            self.show_home
        )

        self.archive_health_workspace.home_requested.connect(
            self.show_home
        )

        self.stack.addWidget(
            self.home_view
        )

        self.stack.addWidget(
            self.photos_workspace
        )

        self.stack.addWidget(
            self.contacts_workspace
        )

        self.stack.addWidget(
            self.archive_health_workspace
        )

        self.setCentralWidget(
            self.stack
        )

        self.show_home()

        self.statusBar().showMessage(
            "LegacyLens V3 Ready"
        )

    def _build_registry(
        self,
    ) -> ModuleRegistry:

        registry = ModuleRegistry()

        registry.register(
            ModuleManifest(
                module_id="photos",
                name="Photos",
                version="0.1.0",
                description="Photo tools",
                entry_point="modules.photos",
            )
        )

        registry.register(
            ModuleManifest(
                module_id="contacts",
                name="Contacts",
                version="0.1.0",
                description="Contact tools",
                entry_point="modules.contacts",
            )
        )

        registry.register(
            ModuleManifest(
                module_id="archive_health",
                name="Archive Health",
                version="0.1.0",
                description="Health tools",
                entry_point="platform.archive_health",
            )
        )

        return registry

    def show_home(
        self,
    ) -> None:

        self.stack.setCurrentWidget(
            self.home_view
        )

        self.statusBar().showMessage(
            "Home"
        )

    def open_workspace(
        self,
        module_id: str,
    ) -> None:

        if module_id == "photos":

            self.stack.setCurrentWidget(
                self.photos_workspace
            )

        elif module_id == "contacts":

            self.stack.setCurrentWidget(
                self.contacts_workspace
            )

        elif module_id == "archive_health":

            self.stack.setCurrentWidget(
                self.archive_health_workspace
            )

        else:

            self.statusBar().showMessage(
                f"Unknown workspace: {module_id}"
            )

            return

        self.statusBar().showMessage(
            f"Opened {module_id}"
        )