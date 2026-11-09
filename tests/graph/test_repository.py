from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from archive_graph.builders.graph_builder import GraphBuilder
from archive_graph.services.graph_service import GraphService
from archive_graph.storage.graph_repository import (
    GraphRepository,
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

repo = GraphRepository()

saved_file = repo.save(graph)

print("Saved:")
print(saved_file)

loaded_graph = repo.load()

print()
print("Loaded:")

print(
    loaded_graph.summary()
)

backup_file = repo.backup(graph)

print()
print("Backup:")

print(backup_file)

print()
print(
    "Backups:",
    len(repo.list_backups())
)
