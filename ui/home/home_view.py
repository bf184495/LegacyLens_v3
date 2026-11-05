"""
home_view.py

LegacyLens V3 Home View.
"""

from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
)

from core.module_registry import (
    ModuleRegistry,
)

from .module_selector import ModuleSelector


class HomeView(QWidget):

    module_selected = Signal(str)

    """
    Main LegacyLens Home Screen.
    """

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

        title = QLabel(
            "LegacyLens V3"
        )

        title.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            """
        )

        subtitle = QLabel(
            "Digital Legacy Operating System"
        )

        subtitle.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        subtitle.setStyleSheet(
            """
            font-size: 14px;
            color: gray;
            """
        )

        selector = ModuleSelector(
            self.registry
        )

        selector.module_selected.connect(
            self.module_selected.emit
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(selector)

        layout.addStretch()