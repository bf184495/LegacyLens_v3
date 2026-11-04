"""
photos_workspace.py

Photos workspace for LegacyLens V3.
"""

from PySide6.QtWidgets import QLabel

from .base_workspace import BaseWorkspace


class PhotosWorkspace(BaseWorkspace):
    """
    Photos module workspace.
    """

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Photos",
            parent,
        )

        self.layout().addWidget(
            QLabel(
                "Photos Module\n\nComing Soon"
            )
        )