"""
ui/workspaces/explorer_workspace.py

Archive Graph Explorer

Provides graph traversal and node inspection.
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QGroupBox,
    QHBoxLayout,
    QListWidget,
    QListWidgetItem,
    QTextEdit,
    QVBoxLayout,
)

from .base_workspace import BaseWorkspace

from archive_graph.storage.graph_repository import (
    GraphRepository,
)


class ExplorerWorkspace(
    BaseWorkspace
):
    """
    Graph traversal workspace.
    """

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Explorer",
            parent,
        )

        self.repo = GraphRepository()
        self.graph = self.repo.load()

        self.current_node = None

        self._build_explorer_ui()

    def _build_explorer_ui(
        self,
    ) -> None:

        root_layout = self.layout()

        #
        # Container widget allows us to safely
        # insert our own horizontal layout below
        # the BaseWorkspace header/title area.
        #
        container = QWidget()

        main_layout = QHBoxLayout(
            container
        )

        root_layout.addWidget(
            container
        )

        #
        # ==================================================
        # Node Browser
        # ==================================================
        #

        nodes_group = QGroupBox(
            "Graph Nodes"
        )

        nodes_layout = QVBoxLayout()

        self.node_list = QListWidget()

        nodes_layout.addWidget(
            self.node_list
        )

        nodes_group.setLayout(
            nodes_layout
        )

        #
        # ==================================================
        # Node Details
        # ==================================================
        #

        details_group = QGroupBox(
            "Node Details"
        )

        details_layout = QVBoxLayout()

        self.details_view = QTextEdit()
        self.details_view.setReadOnly(
            True
        )

        details_layout.addWidget(
            self.details_view
        )

        details_group.setLayout(
            details_layout
        )

        #
        # ==================================================
        # Relationships
        # ==================================================
        #

        relationships_group = QGroupBox(
            "Relationships"
        )

        relationships_layout = QVBoxLayout()

        self.relationship_list = QListWidget()

        relationships_layout.addWidget(
            self.relationship_list
        )

        relationships_group.setLayout(
            relationships_layout
        )

        #
        # Add groups to layout
        #

        main_layout.addWidget(
            nodes_group,
            2,
        )

        main_layout.addWidget(
            details_group,
            3,
        )

        main_layout.addWidget(
            relationships_group,
            2,
        )

        #
        # Load data
        #

        self.populate_nodes()

        self.node_list.itemClicked.connect(
            self.display_node
        )

    #
    # ==================================================
    # Node Browser
    # ==================================================
    #

    def populate_nodes(
        self,
    ) -> None:

        self.node_list.clear()

        try:

            nodes = sorted(
                self.graph.all_nodes(),
                key=lambda n: getattr(
                    n,
                    "id",
                    "",
                ),
            )

        except Exception as ex:

            self.node_list.addItem(
                f"Error loading nodes: {ex}"
            )

            return

        for node in nodes:

            label = (
                f"{node.__class__.__name__}: "
                f"{getattr(node, 'id', '')}"
            )

            item = QListWidgetItem(
                label
            )

            item.setData(
                Qt.ItemDataRole.UserRole,
                node,
            )

            self.node_list.addItem(
                item
            )

    #
    # ==================================================
    # Node Inspector
    # ==================================================
    #

    def display_node(
        self,
        item,
    ) -> None:

        node = item.data(
            Qt.ItemDataRole.UserRole
        )

        self.current_node = node

        self._show_details(
            node
        )

        self._show_relationships(
            node
        )

    def _show_details(
        self,
        node,
    ) -> None:

        lines = [
            f"Type: {node.__class__.__name__}"
        ]

        for key, value in vars(
            node
        ).items():

            lines.append(
                f"{key}: {value}"
            )

        self.details_view.setText(
            "\n".join(lines)
        )

    #
    # ==================================================
    # Relationship Inspector
    # ==================================================
    #

    def _show_relationships(
        self,
        node,
    ) -> None:

        self.relationship_list.clear()

        node_id = getattr(
            node,
            "id",
            None,
        )

        if node_id is None:

            self.relationship_list.addItem(
                "Node has no ID."
            )

            return

        #
        # Graph compatibility layer
        #

        if not hasattr(
            self.graph,
            "edges",
        ):

            self.relationship_list.addItem(
                "Graph does not expose edges."
            )

            return

        edges = getattr(
            self.graph,
            "edges",
            [],
        )

        relationship_count = 0

        for edge in edges:

            source = getattr(
                edge,
                "source_id",
                None,
            )

            target = getattr(
                edge,
                "target_id",
                None,
            )

            relationship = getattr(
                edge,
                "relationship",
                "related_to",
            )

            if (
                source == node_id
                or target == node_id
            ):

                relationship_count += 1

                self.relationship_list.addItem(
                    (
                        f"{relationship}: "
                        f"{source} → {target}"
                    )
                )

        if relationship_count == 0:

            self.relationship_list.addItem(
                "No relationships found."
            )