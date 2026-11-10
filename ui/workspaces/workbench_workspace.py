"""
ui/workspaces/workbench_workspace.py

Archive Graph Workbench Dashboard
"""

from PySide6.QtWidgets import (
    QLabel,
    QGroupBox,
    QVBoxLayout,
    QHBoxLayout,
    QListWidget,
    QScrollArea,
    QWidget,
)

from .base_workspace import BaseWorkspace

from archive_graph.storage.graph_repository import (
    GraphRepository,
)

from archive_graph.views.workbench_view import (
    WorkbenchView,
)


class WorkbenchWorkspace(
    BaseWorkspace
):
    """
    Archive Graph Curator Dashboard.
    """

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Workbench",
            parent,
        )

        self.repo = GraphRepository()
        self.graph = self.repo.load()

        self.view = WorkbenchView(
            self.graph
        )

        self._build_dashboard()

    def _build_dashboard(self) -> None:

        #
        # BaseWorkspace already created a layout.
        #
        root_layout = self.layout()

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()
        container_layout = QVBoxLayout(
            container
        )

        scroll.setWidget(
            container
        )

        root_layout.addWidget(
            scroll
        )

        stats = (
            self.view.graph_statistics()
        )

        #
        # =====================================================
        # Archive Summary
        # =====================================================
        #

        summary_group = QGroupBox(
            "Archive Summary"
        )

        summary_layout = QHBoxLayout()

        summary_cards = [
            ("Photos", stats["photos"]),
            ("People", stats["people"]),
            ("Events", stats["events"]),
            ("Locations", stats["locations"]),
            (
                "Collections",
                stats["collections"],
            ),
            ("Stories", stats["stories"]),
            ("Tasks", stats["tasks"]),
            (
                "Discoveries",
                stats["discoveries"],
            ),
        ]

        for title, value in summary_cards:

            card = QLabel(
                f"{title}\n\n{value}"
            )

            card.setStyleSheet(
                """
                QLabel {
                    border: 1px solid #666;
                    border-radius: 6px;
                    padding: 10px;
                    font-weight: bold;
                    min-width: 100px;
                }
                """
            )

            summary_layout.addWidget(
                card
            )

        summary_group.setLayout(
            summary_layout
        )

        container_layout.addWidget(
            summary_group
        )

        #
        # =====================================================
        # Active Tasks
        # =====================================================
        #

        task_group = QGroupBox(
            "Active Tasks"
        )

        task_layout = QVBoxLayout()

        task_list = QListWidget()

        for task in (
            self.view.active_tasks()
        ):
            title = getattr(
                task,
                "title",
                task.id,
            )

            task_list.addItem(
                str(title)
            )

        task_layout.addWidget(
            task_list
        )

        task_group.setLayout(
            task_layout
        )

        container_layout.addWidget(
            task_group
        )

        #
        # =====================================================
        # Open Discoveries
        # =====================================================
        #

        discoveries_group = (
            QGroupBox(
                "Open Discoveries"
            )
        )

        discoveries_layout = (
            QVBoxLayout()
        )

        discoveries_list = (
            QListWidget()
        )

        for discovery in (
            self.view.open_discoveries()
        ):

            title = getattr(
                discovery,
                "title",
                discovery.id,
            )

            discoveries_list.addItem(
                str(title)
            )

        discoveries_layout.addWidget(
            discoveries_list
        )

        discoveries_group.setLayout(
            discoveries_layout
        )

        container_layout.addWidget(
            discoveries_group
        )

        #
        # =====================================================
        # Featured Photos
        # =====================================================
        #

        photos_group = QGroupBox(
            "Featured Photos"
        )

        photos_layout = QVBoxLayout()

        photos_list = QListWidget()

        for photo in (
            self.view.featured_photos()
        ):

            photo_name = getattr(
                photo,
                "filename",
                photo.id,
            )

            photos_list.addItem(
                str(photo_name)
            )

        photos_layout.addWidget(
            photos_list
        )

        photos_group.setLayout(
            photos_layout
        )

        container_layout.addWidget(
            photos_group
        )

        #
        # =====================================================
        # Graph Health
        # =====================================================
        #

        graph_health = (
            self.view.archive_health()
        )

        health_group = QGroupBox(
            "Graph Health"
        )

        health_layout = QVBoxLayout()

        health_layout.addWidget(
            QLabel(
                f"Total Nodes: "
                f"{graph_health['nodes']}"
            )
        )

        health_layout.addWidget(
            QLabel(
                f"Total Relationships: "
                f"{graph_health['edges']}"
            )
        )

        health_layout.addWidget(
            QLabel(
                "Connectivity Ratio: "
                f"{graph_health['connectivity_ratio']}"
            )
        )

        health_group.setLayout(
            health_layout
        )

        container_layout.addWidget(
            health_group
        )

        #
        # =====================================================
        # Workbench Insights
        # =====================================================
        #

        insights_group = QGroupBox(
            "Archive Insights"
        )

        insights_layout = (
            QVBoxLayout()
        )

        insights_layout.addWidget(
            QLabel(
                f"Photos in Archive: "
                f"{stats['photos']}"
            )
        )

        insights_layout.addWidget(
            QLabel(
                f"People Identified: "
                f"{stats['people']}"
            )
        )

        insights_layout.addWidget(
            QLabel(
                f"Stories Created: "
                f"{stats['stories']}"
            )
        )

        insights_layout.addWidget(
            QLabel(
                f"Collections: "
                f"{stats['collections']}"
            )
        )

        insights_group.setLayout(
            insights_layout
        )

        container_layout.addWidget(
            insights_group
        )

        container_layout.addStretch()