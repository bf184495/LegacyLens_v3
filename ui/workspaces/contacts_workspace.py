"""
contacts_workspace.py

Contacts workspace for LegacyLens V3.
"""

from PySide6.QtWidgets import QLabel

from .base_workspace import BaseWorkspace


class ContactsWorkspace(BaseWorkspace):
    """
    Contacts module workspace.
    """

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Contacts",
            parent,
        )

        self.layout().addWidget(
            QLabel(
                "Contacts Module\n\nComing Soon"
            )
        )