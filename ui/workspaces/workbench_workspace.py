# ui/workspaces/workbench_workspace.py

from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from archive_graph.storage.graph_repository import (
    GraphRepository,
)

from archive_graph.views.workbench_view import (
    WorkbenchView,
)


class WorkbenchWorkspace(QWidget):

    def __init__(self):
        super().__init__()

        self.repo = GraphRepository()

        self.graph = self.repo.load()

        self.view = WorkbenchView(
            self.graph
        )

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        summary = self.view.summary()

        layout.addWidget(
            QLabel("Workbench")
        )

        layout.addWidget(
            QLabel(
                f"Photos: "
                f"{summary['photos']}"
            )
        )

        layout.addWidget(
            QLabel(
                f"Tasks: "
                f"{summary['tasks']}"
            )
        )

        layout.addWidget(
            QLabel(
                f"Discoveries: "
                f"{summary['discoveries']}"
            )
        )