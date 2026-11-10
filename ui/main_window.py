"""
main_window.py

Primary application window for LegacyLens V3.
"""

from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
)

from ui.home.home_view import HomeView

from core.module_registry import (
    ModuleRegistry,
    ModuleManifest,
)

from ui.workspaces import (
    PhotosWorkspace,
    ContactsWorkspace,
    ArchiveHealthWorkspace,
    WorkbenchWorkspace,
    ExplorerWorkspace,
    TimelineWorkspace,
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

        #
        # Create views
        #

        self.home_view = HomeView(
            self.registry
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

        self.workbench_workspace = (
            WorkbenchWorkspace()
        )

        self.explorer_workspace = (
            ExplorerWorkspace()
        )

        self.timeline_workspace = (
            TimelineWorkspace()
        )

        #
        # Wire signals
        #

        self.home_view.module_selected.connect(
            self.open_workspace
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

        #
        # Populate stack
        #

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

        self.stack.addWidget(
            self.workbench_workspace
        )

        self.stack.addWidget(
            self.explorer_workspace
        )

        self.stack.addWidget(
            self.timeline_workspace
        )

        self.setCentralWidget(
            self.stack
        )

        #
        # Menu Bar
        #

        self._build_menu_bar()

        self.show_home()

        self.statusBar().showMessage(
            "LegacyLens V3 Ready"
        )

    def _build_registry(
        self
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

        registry.register(
            ModuleManifest(
                module_id="workbench",
                name="Workbench",
                version="0.1.0",
                description="Archive Graph Workbench",
                entry_point="archive_graph.workbench",
            )
        )

        registry.register(
            ModuleManifest(
                module_id="explorer",
                name="Explorer",
                version="0.1.0",
                description="Archive Graph Explorer",
                entry_point="archive_graph.explorer",
            )
        )

        registry.register(
            ModuleManifest(
                module_id="timeline",
                name="Timeline",
                version="0.1.0",
                description="Archive Graph Timeline",
                entry_point="archive_graph.timeline",
            )
        )

        return registry

    def _build_menu_bar(
        self
    ) -> None:
        """
        Build the application menu bar.
        """

        menu_bar = self.menuBar()

        #
        # File Menu
        #

        file_menu = menu_bar.addMenu(
            "&File"
        )

        home_action = QAction(
            "Home",
            self
        )

        home_action.triggered.connect(
            self.show_home
        )

        exit_action = QAction(
            "Exit",
            self
        )

        exit_action.triggered.connect(
            self.close
        )

        file_menu.addAction(
            home_action
        )

        file_menu.addSeparator()

        file_menu.addAction(
            exit_action
        )

        #
        # Modules Menu
        #

        modules_menu = menu_bar.addMenu(
            "&Modules"
        )

        photos_action = QAction(
            "Photos",
            self
        )

        photos_action.triggered.connect(
            lambda: self.open_workspace(
                "photos"
            )
        )

        contacts_action = QAction(
            "Contacts",
            self
        )

        contacts_action.triggered.connect(
            lambda: self.open_workspace(
                "contacts"
            )
        )

        health_action = QAction(
            "Archive Health",
            self
        )

        health_action.triggered.connect(
            lambda: self.open_workspace(
                "archive_health"
            )
        )

        workbench_action = QAction(
            "Workbench",
            self
        )

        workbench_action.triggered.connect(
            lambda: self.open_workspace(
                "workbench"
            )
        )

        explorer_action = QAction(
            "Explorer",
            self
        )

        explorer_action.triggered.connect(
            lambda: self.open_workspace(
                "explorer"
            )
        )

        timeline_action = QAction(
            "Timeline",
            self
        )

        timeline_action.triggered.connect(
            lambda: self.open_workspace(
                "timeline"
            )
        )

        modules_menu.addAction(
            photos_action
        )

        modules_menu.addAction(
            contacts_action
        )

        modules_menu.addAction(
            health_action
        )

        modules_menu.addAction(
            workbench_action
        )

        modules_menu.addAction(
            explorer_action
        )

        modules_menu.addAction(
            timeline_action
        )

        #
        # Tools Menu
        #

        tools_menu = menu_bar.addMenu(
            "&Tools"
        )

        settings_action = QAction(
            "Settings",
            self
        )

        tools_menu.addAction(
            settings_action
        )

        #
        # Help Menu
        #

        help_menu = menu_bar.addMenu(
            "&Help"
        )

        about_action = QAction(
            "About",
            self
        )

        help_menu.addAction(
            about_action
        )

    def show_home(
        self
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

        elif module_id == "workbench":

            self.stack.setCurrentWidget(
                self.workbench_workspace
            )

        elif module_id == "explorer":

            self.stack.setCurrentWidget(
                self.explorer_workspace
            )

        elif module_id == "timeline":

            self.stack.setCurrentWidget(
                self.timeline_workspace
            )

        else:

            self.statusBar().showMessage(
                f"Unknown workspace: {module_id}"
            )

            return

        self.statusBar().showMessage(
            f"Opened {module_id}"
        )