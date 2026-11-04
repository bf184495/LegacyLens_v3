"""
base_workspace.py

Base class for all LegacyLens workspaces.
"""

from PySide6.QtCore import (
    Qt,
    Signal,
)

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
)


class BaseWorkspace(QWidget):
    """
    Base workspace used by all modules.
    """

    home_requested = Signal()

    def __init__(
        self,
        module_name: str,
        parent=None,
    ):
        super().__init__(parent)

        self.module_name = module_name

        self._build_ui()

    def _build_ui(self) -> None:

        layout = QVBoxLayout(self)

        header_layout = QHBoxLayout()

        home_button = QPushButton(
            "🏠 Home"
        )

        home_button.clicked.connect(
            self.home_requested.emit
        )

        header_layout.addWidget(
            home_button
        )

        header_layout.addStretch()

        title = QLabel(
            self.module_name
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

        layout.addLayout(
            header_layout
        )

        layout.addWidget(
            title
        )

        layout.addStretch()