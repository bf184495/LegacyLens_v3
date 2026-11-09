from __future__ import annotations

from archive_graph.models import (
    CollectionNode,
    DiscoveryNode,
    EventNode,
    PersonNode,
    PhotoNode,
    StoryNode,
)
from archive_graph.services.graph_service import GraphService


class ExplorerView:
    """
    Provides explorer-oriented access to Archive Graph data.

    Supports browsing by:

    - Photos
    - People
    - Events
    - Collections
    - Stories
    - Discoveries
    """

    def __init__(self, graph: GraphService):
        self.graph = graph

    # ---------------------------------------------------------
    # Photos
    # ---------------------------------------------------------

    def photos(self) -> list[PhotoNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, PhotoNode)
        ]

    # ---------------------------------------------------------
    # People
    # ---------------------------------------------------------

    def people(self) -> list[PersonNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, PersonNode)
        ]

    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------

    def events(self) -> list[EventNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, EventNode)
        ]

    # ---------------------------------------------------------
    # Collections
    # ---------------------------------------------------------

    def collections(self) -> list[CollectionNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, CollectionNode)
        ]

    # ---------------------------------------------------------
    # Stories
    # ---------------------------------------------------------

    def stories(self) -> list[StoryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, StoryNode)
        ]

    # ---------------------------------------------------------
    # Discoveries
    # ---------------------------------------------------------

    def discoveries(self) -> list[DiscoveryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, DiscoveryNode)
        ]

    # ---------------------------------------------------------
    # Counts
    # ---------------------------------------------------------

    def counts(self) -> dict:
        return {
            "photos": len(self.photos()),
            "people": len(self.people()),
            "events": len(self.events()),
            "collections": len(self.collections()),
            "stories": len(self.stories()),
            "discoveries": len(self.discoveries()),
        }

    # ---------------------------------------------------------
    # Related Content
    # ---------------------------------------------------------

    def related_items(
        self,
        node_id: str,
    ) -> list:

        return self.graph.related_nodes(
            node_id
        )

    # ---------------------------------------------------------
    # Explorer Summary
    # ---------------------------------------------------------

    def summary(self) -> dict:

        return {
            "counts": self.counts(),

            "photos": self.photos(),

            "people": self.people(),

            "events": self.events(),

            "collections": self.collections(),

            "stories": self.stories(),

            "discoveries": self.discoveries(),
        }