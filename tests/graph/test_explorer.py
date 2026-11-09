from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import (
    GraphBuilder,
)
from archive_graph.services.graph_service import (
    GraphService,
)
from archive_graph.views.explorer_view import (
    ExplorerView,
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

builder.import_people(
    [
        {
            "id": "person_001",
            "display_name": "Grandpa",
        }
    ]
)

builder.link_person_to_photo(
    "person_001",
    "photo_001"
)

view = ExplorerView(graph)

print(view.counts())

print()
print(view.people())

print()
print(view.photos())

print()
print(
    view.related_items(
        "person_001"
    )
)