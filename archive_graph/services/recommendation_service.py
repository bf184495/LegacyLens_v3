from __future__ import annotations

from archive_graph.models import (
    DiscoveryNode,
    TaskNode,
)
from archive_graph.services.graph_service import GraphService


class RecommendationService:
    """
    Generates curator-focused recommendations
    from Archive Graph content.

    Future versions may incorporate scoring,
    ML ranking, confidence weighting,
    archive health data,
    and historical user behavior.
    """

    def __init__(self, graph: GraphService):
        self.graph = graph

    # ---------------------------------------------------------
    # Task Recommendations
    # ---------------------------------------------------------

    def open_tasks(self) -> list[TaskNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, TaskNode)
            and node.status == "open"
        ]

    def highest_priority_task(self) -> TaskNode | None:

        priority_order = {
            "critical": 4,
            "high": 3,
            "normal": 2,
            "low": 1,
        }

        tasks = self.open_tasks()

        if not tasks:
            return None

        return max(
            tasks,
            key=lambda task: priority_order.get(
                task.priority.lower(),
                0,
            ),
        )

    # ---------------------------------------------------------
    # Discovery Recommendations
    # ---------------------------------------------------------

    def open_discoveries(self) -> list[DiscoveryNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, DiscoveryNode)
            and node.status == "open"
        ]

    def highest_confidence_discovery(
        self,
    ) -> DiscoveryNode | None:

        discoveries = self.open_discoveries()

        if not discoveries:
            return None

        return max(
            discoveries,
            key=lambda discovery: discovery.confidence,
        )

    # ---------------------------------------------------------
    # Next Action
    # ---------------------------------------------------------

    def suggested_next_action(self) -> dict:

        task = self.highest_priority_task()

        if task:

            return {
                "type": "task",
                "title": task.title,
                "priority": task.priority,
                "message": (
                    f"Recommended next task: "
                    f"{task.title}"
                ),
            }

        discovery = self.highest_confidence_discovery()

        if discovery:

            return {
                "type": "discovery",
                "title": discovery.title,
                "confidence": discovery.confidence,
                "message": (
                    f"Investigation recommended: "
                    f"{discovery.title}"
                ),
            }

        return {
            "type": "idle",
            "title": "No Recommendations",
            "message": (
                "No pending tasks or discoveries."
            ),
        }

    # ---------------------------------------------------------
    # Full Recommendation Package
    # ---------------------------------------------------------

    def recommendation_summary(self) -> dict:

        return {
            "next_action":
                self.suggested_next_action(),

            "open_tasks":
                len(self.open_tasks()),

            "open_discoveries":
                len(self.open_discoveries()),
        }