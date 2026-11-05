"""
module_selector.py

LegacyLens V3 Module Selector.

Displays modules registered with the
Module Registry and allows users to
launch workspaces.

Future responsibilities:

- Module launching
- Module filtering
- Module health indicators
- Module search
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
)

from core.module_registry import (
    ModuleRegistry,
)


class ModuleSelector(QWidget):
    """
    Displays available LegacyLens modules.
    """

    module_selected = Signal(str)

    def __init__(
        self,
        registry: ModuleRegistry,
        parent=None,
    ):

        super().__init__(parent)

        self.registry = registry

        self._build_ui()

    def _build_ui(self) -> None:

        layout = QVBoxLayout(self)

        for manifest in self.registry.visible_modules():

            button = QPushButton(
                manifest.name
            )

            button.clicked.connect(
                lambda checked=False,
                module_id=manifest.module_id:
                self.module_selected.emit(
                    module_id
                )
            )

            layout.addWidget(button)

        layout.addStretch()