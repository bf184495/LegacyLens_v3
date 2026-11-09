from __future__ import annotations

from archive_graph.services.graph_service import GraphService

from archive_graph.models import (
    DiscoveryNode,
    PhotoNode,
    TaskNode,
)


class WorkbenchView:
    """
    Provides curator-focused views of graph data.

    The UI should consume this class instead of
    talking directly to GraphService.
    """

    def __init__(self, graph: GraphService):
        self.graph = graph

    # ---------------------------------------------------------
    # Tasks
    # ---------------------------------------------------------

    def active_tasks(self) -> list[TaskNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, TaskNode)
            and node.status == "open"
        ]

    def task_count(self) -> int:
        return len(self.active_tasks())

    # ---------------------------------------------------------
    # Discoveries
    # ---------------------------------------------------------

    def open_discoveries(self) -> list[DiscoveryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, DiscoveryNode)
            and node.status == "open"
        ]

    def discovery_count(self) -> int:
        return len(self.open_discoveries())

    # ---------------------------------------------------------
    # Photos
    # ---------------------------------------------------------

    def all_photos(self) -> list[PhotoNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, PhotoNode)
        ]

    def photo_count(self) -> int:
        return len(self.all_photos())

    def featured_photos(
        self,
        limit: int = 12,
    ) -> list[PhotoNode]:
        return self.all_photos()[:limit]

    # ---------------------------------------------------------
    # Dashboard Summary
    # ---------------------------------------------------------

    def summary(self) -> dict:
        return {
            "photos": self.photo_count(),
            "tasks": self.task_count(),
            "discoveries": self.discovery_count(),
            "nodes": self.graph.node_count,
            "edges": self.graph.edge_count,
        }

    # ---------------------------------------------------------
    # Workbench Cards
    # ---------------------------------------------------------

    def workbench_cards(self) -> dict:

        return {
            "active_tasks": self.active_tasks(),

            "open_discoveries": self.open_discoveries(),

            "featured_photos": self.featured_photos(),

            "summary": self.summary(),
        }