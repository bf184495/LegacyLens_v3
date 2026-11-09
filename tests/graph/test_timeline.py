from pathlib import Path
import sys
from datetime import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.models.photo import PhotoNode
from archive_graph.models.event import EventNode

from archive_graph.services.graph_service import (
    GraphService,
)

from archive_graph.views.timeline_view import (
    TimelineView,
)

graph = GraphService()

graph.add_node(
    PhotoNode(
        id="photo_001",
        filename="christmas.jpg",
        path="c:/photos/christmas.jpg",
        capture_date=datetime(1985, 12, 25),
    )
)

graph.add_node(
    PhotoNode(
        id="photo_002",
        filename="vacation.jpg",
        path="c:/photos/vacation.jpg",
        capture_date=datetime(1998, 7, 10),
    )
)

graph.add_node(
    EventNode(
        id="event_001",
        title="Family Reunion",
        start_date=datetime(1998, 7, 10),
    )
)

view = TimelineView(graph)

print(view.summary())
print()
print(view.timeline_feed())
print()
print(view.archive_span())