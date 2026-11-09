from __future__ import annotations

from collections import defaultdict
from typing import Any


class GraphService:
    """
    Central Archive Graph engine.

    Stores nodes and edges and provides
    traversal/query operations.
    """

    def __init__(self) -> None:
        self._nodes: dict[str, Any] = {}

        self._edges: list[Any] = []

        self._outbound: dict[str, list[Any]] = defaultdict(list)
        self._inbound: dict[str, list[Any]] = defaultdict(list)

    # ---------------------------------------------------------
    # Node Operations
    # ---------------------------------------------------------

    def add_node(self, node: Any) -> None:
        self._nodes[node.id] = node

    def add_nodes(self, nodes: list[Any]) -> None:
        for node in nodes:
            self.add_node(node)

    def get_node(self, node_id: str) -> Any | None:
        return self._nodes.get(node_id)

    def has_node(self, node_id: str) -> bool:
        return node_id in self._nodes

    def remove_node(self, node_id: str) -> None:
        if node_id not in self._nodes:
            return

        del self._nodes[node_id]

        self._outbound.pop(node_id, None)
        self._inbound.pop(node_id, None)

        self._edges = [
            edge
            for edge in self._edges
            if edge.source_id != node_id
            and edge.target_id != node_id
        ]

    def all_nodes(self) -> list[Any]:
        return list(self._nodes.values())

    # ---------------------------------------------------------
    # Edge Operations
    # ---------------------------------------------------------

    def add_edge(self, edge: Any) -> None:
        self._edges.append(edge)

        self._outbound[edge.source_id].append(edge)
        self._inbound[edge.target_id].append(edge)

    def add_edges(self, edges: list[Any]) -> None:
        for edge in edges:
            self.add_edge(edge)

    def all_edges(self) -> list[Any]:
        return list(self._edges)

    # ---------------------------------------------------------
    # Relationship Queries
    # ---------------------------------------------------------

    def outbound_edges(self, node_id: str) -> list[Any]:
        return self._outbound.get(node_id, [])

    def inbound_edges(self, node_id: str) -> list[Any]:
        return self._inbound.get(node_id, [])

    def related_nodes(self, node_id: str) -> list[Any]:
        related = []

        for edge in self.outbound_edges(node_id):
            node = self.get_node(edge.target_id)

            if node:
                related.append(node)

        return related

    def related_by_type(
        self,
        node_id: str,
        relationship_type: str,
    ) -> list[Any]:
        results = []

        for edge in self.outbound_edges(node_id):

            if edge.relationship_type != relationship_type:
                continue

            node = self.get_node(edge.target_id)

            if node:
                results.append(node)

        return results

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def nodes_by_type(self, node_type: str) -> list[Any]:
        return [
            node
            for node in self._nodes.values()
            if node.__class__.__name__.startswith(node_type)
        ]

    def find(
        self,
        predicate,
    ) -> list[Any]:
        return [
            node
            for node in self._nodes.values()
            if predicate(node)
        ]

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    @property
    def node_count(self) -> int:
        return len(self._nodes)

    @property
    def edge_count(self) -> int:
        return len(self._edges)

    # ---------------------------------------------------------
    # Diagnostics
    # ---------------------------------------------------------

    def summary(self) -> dict:
        return {
            "nodes": self.node_count,
            "edges": self.edge_count,
            "types": {
                node.__class__.__name__
                for node in self._nodes.values()
            },
        }