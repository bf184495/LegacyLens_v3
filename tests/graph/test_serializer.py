from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import GraphBuilder
from archive_graph.services.graph_service import GraphService
from archive_graph.storage.graph_serializer import (
    GraphSerializer,
)

graph = GraphService()

builder = GraphBuilder(graph)

builder.import_photos(
    [
        {
            "id": "photo_001",
            "filename": "vacation.jpg",
            "path": "c:/photos/vacation.jpg",
        }
    ]
)

builder.create_task(
    task_id="task_001",
    title="Review Validation Queue",
    task_type="validation",
)

GraphSerializer.save(
    graph,
    "graph_test.json",
)

loaded_graph = GraphSerializer.load(
    "graph_test.json",
)

print("ORIGINAL:")
print(graph.summary())

print()

print("LOADED:")
print(loaded_graph.summary())