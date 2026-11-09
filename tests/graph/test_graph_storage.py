from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import GraphBuilder
from archive_graph.services.graph_service import GraphService

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

print(graph.summary())