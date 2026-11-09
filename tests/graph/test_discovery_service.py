from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import GraphBuilder
from archive_graph.services.discovery_service import (
    DiscoveryService,
)
from archive_graph.services.graph_service import (
    GraphService,
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
            "display_name": "Unknown Person",
        }
    ]
)

builder.create_discovery(
    discovery_id="disc_001",
    title="Unknown Person Cluster",
    discovery_type="people",
    confidence=0.91,
)

builder.create_discovery(
    discovery_id="disc_002",
    title="Possible Reunion Event",
    discovery_type="event",
    confidence=0.72,
)

service = DiscoveryService(graph)

print(service.discovery_summary())