from __future__ import annotations

from archive_graph.models import (
    DiscoveryNode,
    Edge,
    PersonNode,
    PhotoNode,
    TaskNode,
)
from archive_graph.services.graph_service import GraphService


class GraphBuilder:
    """
    Converts LegacyLens outputs into
    Archive Graph objects.
    """

    def __init__(self, graph: GraphService):
        self.graph = graph

    # ---------------------------------------------------------
    # Photos
    # ---------------------------------------------------------

    def import_photos(
        self,
        photos: list[dict],
    ) -> list[PhotoNode]:

        created = []

        for row in photos:

            photo = PhotoNode(
                id=row.get("id", ""),
                filename=row.get("filename", ""),
                path=row.get("path", ""),
                category=row.get("category", "UNKNOWN"),
                confidence=float(
                    row.get("confidence", 1.0)
                ),
            )

            self.graph.add_node(photo)

            created.append(photo)

        return created

    # ---------------------------------------------------------
    # People
    # ---------------------------------------------------------

    def import_people(
        self,
        people: list[dict],
    ) -> list[PersonNode]:

        created = []

        for row in people:

            person = PersonNode(
                id=row.get("id", ""),
                display_name=row.get(
                    "display_name",
                    "Unknown Person",
                ),
                confidence=float(
                    row.get("confidence", 0.0)
                ),
            )

            self.graph.add_node(person)

            created.append(person)

        return created

    # ---------------------------------------------------------
    # Person ↔ Photo Links
    # ---------------------------------------------------------

    def link_person_to_photo(
        self,
        person_id: str,
        photo_id: str,
        confidence: float = 1.0,
    ) -> Edge:

        edge = Edge(
            id=f"{person_id}_{photo_id}",
            relationship_type="APPEARS_IN",
            source_id=person_id,
            target_id=photo_id,
            confidence=confidence,
        )

        self.graph.add_edge(edge)

        return edge

    # ---------------------------------------------------------
    # Discoveries
    # ---------------------------------------------------------

    def create_discovery(
        self,
        discovery_id: str,
        title: str,
        discovery_type: str,
        confidence: float,
    ) -> DiscoveryNode:

        discovery = DiscoveryNode(
            id=discovery_id,
            title=title,
            discovery_type=discovery_type,
            confidence=confidence,
        )

        self.graph.add_node(discovery)

        return discovery

    # ---------------------------------------------------------
    # Tasks
    # ---------------------------------------------------------

    def create_task(
        self,
        task_id: str,
        title: str,
        task_type: str,
        priority: str = "normal",
    ) -> TaskNode:

        task = TaskNode(
            id=task_id,
            title=title,
            task_type=task_type,
            priority=priority,
        )

        self.graph.add_node(task)

        return task

    # ---------------------------------------------------------
    # Discovery → Task
    # ---------------------------------------------------------

    def link_discovery_to_task(
        self,
        discovery_id: str,
        task_id: str,
    ) -> Edge:

        edge = Edge(
            id=f"{discovery_id}_{task_id}",
            relationship_type="DISCOVERY_GENERATED_TASK",
            source_id=discovery_id,
            target_id=task_id,
        )

        self.graph.add_edge(edge)

        return edge