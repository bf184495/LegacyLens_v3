from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import GraphBuilder
from archive_graph.services.graph_service import GraphService
from archive_graph.views.workbench_view import WorkbenchView

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

builder.create_discovery(
    discovery_id="disc_001",
    title="Unknown Person Cluster",
    discovery_type="person_cluster",
    confidence=0.89,
)

builder.create_task(
    task_id="task_001",
    title="Review Cluster",
    task_type="people_review",
)

view = WorkbenchView(graph)

print(view.summary())
print()
print(view.workbench_cards())