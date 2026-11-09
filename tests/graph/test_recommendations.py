from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import GraphBuilder
from archive_graph.services.graph_service import GraphService
from archive_graph.services.recommendation_service import (
    RecommendationService,
)

graph = GraphService()

builder = GraphBuilder(graph)

builder.create_task(
    task_id="task_001",
    title="Review Validation Queue",
    task_type="validation",
    priority="high",
)

builder.create_discovery(
    discovery_id="disc_001",
    title="Unknown Person Cluster",
    discovery_type="people",
    confidence=0.91,
)

recommendations = RecommendationService(graph)

print(
    recommendations.recommendation_summary()
)