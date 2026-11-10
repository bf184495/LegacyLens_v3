from __future__ import annotations

from archive_graph.services.graph_service import GraphService

from archive_graph.models import (
    CollectionNode,
    DiscoveryNode,
    EventNode,
    LocationNode,
    PersonNode,
    PhotoNode,
    StoryNode,
    TaskNode,
)


class WorkbenchView:
    """
    Curator-focused dashboard view.

    The UI should consume this class instead of
    directly interrogating the graph.
    """

    def __init__(
        self,
        graph: GraphService,
    ):
        self.graph = graph

    # ---------------------------------------------------------
    # Generic Helpers
    # ---------------------------------------------------------

    def all_nodes(self):
        return list(
            self.graph.all_nodes()
        )

    # ---------------------------------------------------------
    # Photos
    # ---------------------------------------------------------

    def all_photos(
        self,
    ) -> list[PhotoNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                PhotoNode,
            )
        ]

    def photo_count(
        self,
    ) -> int:
        return len(
            self.all_photos()
        )

    def featured_photos(
        self,
        limit: int = 12,
    ) -> list[PhotoNode]:
        return self.all_photos()[:limit]

    # ---------------------------------------------------------
    # People
    # ---------------------------------------------------------

    def all_people(
        self,
    ) -> list[PersonNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                PersonNode,
            )
        ]

    def people_count(
        self,
    ) -> int:
        return len(
            self.all_people()
        )

    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------

    def all_events(
        self,
    ) -> list[EventNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                EventNode,
            )
        ]

    def event_count(
        self,
    ) -> int:
        return len(
            self.all_events()
        )

    # ---------------------------------------------------------
    # Locations
    # ---------------------------------------------------------

    def all_locations(
        self,
    ) -> list[LocationNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                LocationNode,
            )
        ]

    def location_count(
        self,
    ) -> int:
        return len(
            self.all_locations()
        )

    # ---------------------------------------------------------
    # Stories
    # ---------------------------------------------------------

    def all_stories(
        self,
    ) -> list[StoryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                StoryNode,
            )
        ]

    def story_count(
        self,
    ) -> int:
        return len(
            self.all_stories()
        )

    # ---------------------------------------------------------
    # Collections
    # ---------------------------------------------------------

    def all_collections(
        self,
    ) -> list[CollectionNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                CollectionNode,
            )
        ]

    def collection_count(
        self,
    ) -> int:
        return len(
            self.all_collections()
        )

    # ---------------------------------------------------------
    # Tasks
    # ---------------------------------------------------------

    def active_tasks(
        self,
    ) -> list[TaskNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                TaskNode,
            )
            and getattr(
                node,
                "status",
                "",
            )
            == "open"
        ]

    def task_count(
        self,
    ) -> int:
        return len(
            self.active_tasks()
        )

    # ---------------------------------------------------------
    # Discoveries
    # ---------------------------------------------------------

    def open_discoveries(
        self,
    ) -> list[DiscoveryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(
                node,
                DiscoveryNode,
            )
            and getattr(
                node,
                "status",
                "",
            )
            == "open"
        ]

    def discovery_count(
        self,
    ) -> int:
        return len(
            self.open_discoveries()
        )

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def graph_statistics(
        self,
    ) -> dict:
        return {
            "photos": self.photo_count(),
            "people": self.people_count(),
            "events": self.event_count(),
            "locations": self.location_count(),
            "collections": self.collection_count(),
            "stories": self.story_count(),
            "tasks": self.task_count(),
            "discoveries": self.discovery_count(),
            "nodes": self.graph.node_count,
            "edges": self.graph.edge_count,
        }

    def summary(
        self,
    ) -> dict:
        return self.graph_statistics()

    # ---------------------------------------------------------
    # Health Metrics
    # ---------------------------------------------------------

    def archive_health(
        self,
    ) -> dict:

        stats = self.graph_statistics()

        node_count = stats["nodes"]
        edge_count = stats["edges"]

        ratio = (
            edge_count / node_count
            if node_count > 0
            else 0
        )

        return {
            "nodes": node_count,
            "edges": edge_count,
            "connectivity_ratio": round(
                ratio,
                2,
            ),
        }

    # ---------------------------------------------------------
    # Workbench Cards
    # ---------------------------------------------------------

    def workbench_cards(
        self,
    ) -> dict:
        return {
            "summary": self.graph_statistics(),
            "active_tasks": self.active_tasks(),
            "open_discoveries": self.open_discoveries(),
            "featured_photos": self.featured_photos(),
            "graph_health": self.archive_health(),
        }