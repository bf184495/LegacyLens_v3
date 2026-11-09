from __future__ import annotations

from datetime import datetime
from pathlib import Path

from archive_graph.services.graph_service import GraphService
from archive_graph.storage.graph_serializer import (
    GraphSerializer,
)


class GraphRepository:
    """
    Persistent storage manager for Archive Graph.

    Responsibilities:
    - Save graph
    - Load graph
    - Create backups
    - Locate latest graph
    """

    DEFAULT_GRAPH_FILE = "archive_graph.json"

    def __init__(
        self,
        storage_dir: str | Path = "data/databases",
    ) -> None:

        self.storage_dir = Path(storage_dir)

        self.storage_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ---------------------------------------------------------
    # Paths
    # ---------------------------------------------------------

    @property
    def graph_file(self) -> Path:
        return self.storage_dir / self.DEFAULT_GRAPH_FILE

    # ---------------------------------------------------------
    # Save
    # ---------------------------------------------------------

    def save(
        self,
        graph: GraphService,
    ) -> Path:

        return GraphSerializer.save(
            graph,
            self.graph_file,
        )

    # ---------------------------------------------------------
    # Load
    # ---------------------------------------------------------

    def load(self) -> GraphService:

        if not self.graph_file.exists():
            return GraphService()

        return GraphSerializer.load(
            self.graph_file
        )

    # ---------------------------------------------------------
    # Backup
    # ---------------------------------------------------------

    def backup(
        self,
        graph: GraphService,
    ) -> Path:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        backup_file = (
            self.storage_dir
            / f"archive_graph_{timestamp}.json"
        )

        GraphSerializer.save(
            graph,
            backup_file,
        )

        return backup_file

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def exists(self) -> bool:
        return self.graph_file.exists()

    def list_backups(self) -> list[Path]:

        files = list(
            self.storage_dir.glob(
                "archive_graph_*.json"
            )
        )

        files.sort(reverse=True)

        return files

    def latest_backup(self) -> Path | None:

        backups = self.list_backups()

        if not backups:
            return None

        return backups[0]