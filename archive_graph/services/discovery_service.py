from __future__ import annotations

from archive_graph.models import (
    DiscoveryNode,
    DuplicateGroupNode,
    PersonNode,
    PhotoNode,
)
from archive_graph.services.graph_service import GraphService


class DiscoveryService:
    """
    Provides discovery and insight views
    from Archive Graph content.

    Future versions may derive discoveries
    automatically from graph analysis.

    Current version operates on existing
    DiscoveryNodes and related entities.
    """

    def __init__(self, graph: GraphService):
        self.graph = graph

    # ---------------------------------------------------------
    # Discovery Access
    # ---------------------------------------------------------

    def all_discoveries(self) -> list[DiscoveryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, DiscoveryNode)
        ]

    def open_discoveries(self) -> list[DiscoveryNode]:
        return [
            discovery
            for discovery in self.all_discoveries()
            if discovery.status == "open"
        ]

    # ---------------------------------------------------------
    # Confidence Ranking
    # ---------------------------------------------------------

    def highest_confidence_discoveries(
        self,
        limit: int = 5,
    ) -> list[DiscoveryNode]:

        discoveries = sorted(
            self.open_discoveries(),
            key=lambda d: d.confidence,
            reverse=True,
        )

        return discoveries[:limit]

    # ---------------------------------------------------------
    # Discovery Types
    # ---------------------------------------------------------

    def discoveries_by_type(
        self,
        discovery_type: str,
    ) -> list[DiscoveryNode]:

        return [
            discovery
            for discovery in self.all_discoveries()
            if discovery.discovery_type == discovery_type
        ]

    # ---------------------------------------------------------
    # Archive Insights
    # ---------------------------------------------------------

    def archive_insights(self) -> list[dict]:

        insights = []

        photos = [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, PhotoNode)
        ]

        people = [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, PersonNode)
        ]

        duplicates = [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, DuplicateGroupNode)
        ]

        insights.append(
            {
                "type": "photo_count",
                "title": "Photos in Archive",
                "value": len(photos),
            }
        )

        insights.append(
            {
                "type": "people_count",
                "title": "People Identified",
                "value": len(people),
            }
        )

        insights.append(
            {
                "type": "duplicate_groups",
                "title": "Duplicate Groups",
                "value": len(duplicates),
            }
        )

        insights.append(
            {
                "type": "discoveries",
                "title": "Open Discoveries",
                "value": len(self.open_discoveries()),
            }
        )

        return insights

    # ---------------------------------------------------------
    # Workbench Feed
    # ---------------------------------------------------------

    def discovery_feed(self) -> list[dict]:

        feed = []

        for discovery in self.highest_confidence_discoveries():

            feed.append(
                {
                    "id": discovery.id,
                    "title": discovery.title,
                    "type": discovery.discovery_type,
                    "confidence": discovery.confidence,
                    "status": discovery.status,
                }
            )

        return feed

    # ---------------------------------------------------------
    # Dashboard Package
    # ---------------------------------------------------------

    def discovery_summary(self) -> dict:

        return {
            "total_discoveries":
                len(self.all_discoveries()),

            "open_discoveries":
                len(self.open_discoveries()),

            "top_discoveries":
                self.discovery_feed(),

            "archive_insights":
                self.archive_insights(),
        }