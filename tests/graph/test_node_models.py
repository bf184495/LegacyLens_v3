# graph_smoke_test.py

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.models import (
    PhotoNode,
    PersonNode,
    DiscoveryNode
)

photo = PhotoNode(
    id="photo_001",
    filename="vacation.jpg",
    path="c:/photos/vacation.jpg"
)

person = PersonNode(
    id="person_001",
    display_name="Unknown Person"
)

discovery = DiscoveryNode(
    id="disc_001",
    title="Possible Family Cluster",
    discovery_type="person_cluster"
)

print(photo)
print(person)
print(discovery)