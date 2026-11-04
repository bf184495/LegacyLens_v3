"""
archive_health_workspace.py

Archive Health workspace.
"""

from PySide6.QtWidgets import QLabel

from .base_workspace import BaseWorkspace


class ArchiveHealthWorkspace(
    BaseWorkspace
):
    """
    Archive Health workspace.
    """

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Archive Health",
            parent,
        )

        self.layout().addWidget(
            QLabel(
                "Archive Health Module\n\nComing Soon"
            )
        )