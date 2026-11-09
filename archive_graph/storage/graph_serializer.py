from __future__ import annotations

import json
from dataclasses import asdict, is_dataclass
from pathlib import Path

from archive_graph.models import (
    CollectionNode,
    DiscoveryNode,
    DuplicateGroupNode,
    Edge,
    EventNode,
    LocationNode,
    PersonNode,
    PhotoNode,
    StoryNode,
    TaskNode,
    ValidationNode,
)
from archive_graph.services.graph_service import GraphService


NODE_TYPES = {
    "PhotoNode": PhotoNode,
    "PersonNode": PersonNode,
    "EventNode": EventNode,
    "LocationNode": LocationNode,
    "CollectionNode": CollectionNode,
    "StoryNode": StoryNode,
    "DiscoveryNode": DiscoveryNode,
    "TaskNode": TaskNode,
    "ValidationNode": ValidationNode,
    "DuplicateGroupNode": DuplicateGroupNode,
}


class GraphSerializer:
    """
    Serializes and deserializes GraphService
    instances to/from JSON.
    """

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    @staticmethod
    def graph_to_dict(
        graph: GraphService,
    ) -> dict:

        nodes = []

        for node in graph.all_nodes():

            if not is_dataclass(node):
                continue

            nodes.append(
                {
                    "node_type": node.__class__.__name__,
                    "data": asdict(node),
                }
            )

        edges = []

        for edge in graph.all_edges():

            edges.append(
                {
                    "edge_type": edge.__class__.__name__,
                    "data": asdict(edge),
                }
            )

        return {
            "version": "1.0",
            "nodes": nodes,
            "edges": edges,
        }

    @staticmethod
    def save(
        graph: GraphService,
        file_path: str | Path,
    ) -> Path:

        data = GraphSerializer.graph_to_dict(
            graph
        )

        file_path = Path(file_path)

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(
                data,
                f,
                indent=4,
                default=str,
            )

        return file_path

    # ---------------------------------------------------------
    # Import
    # ---------------------------------------------------------

    @staticmethod
    def load(
        file_path: str | Path,
    ) -> GraphService:

        file_path = Path(file_path)

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as f:

            data = json.load(f)

        graph = GraphService()

        # --------------------
        # Nodes
        # --------------------

        for item in data.get(
            "nodes",
            [],
        ):

            node_type = item["node_type"]

            node_class = NODE_TYPES.get(
                node_type
            )

            if node_class is None:
                continue

            node = node_class(
                **item["data"]
            )

            graph.add_node(node)

        # --------------------
        # Edges
        # --------------------

        for item in data.get(
            "edges",
            [],
        ):

            edge = Edge(
                **item["data"]
            )

            graph.add_edge(edge)

        return graph