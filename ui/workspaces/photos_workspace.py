"""
photos_workspace.py

Photos workspace for LegacyLens V3.
"""

from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QFileDialog,
)

from .base_workspace import BaseWorkspace

from modules.photos.core.photo_analyzer import (
    PhotoAnalyzer,
)


class PhotosWorkspace(
    BaseWorkspace
):
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

        self.analyzer = PhotoAnalyzer()

        self.selected_folder = ""

        self.folder_label = QLabel(
            "No folder selected."
        )

        self.browse_button = QPushButton(
            "Browse Folder..."
        )

        self.analyze_button = QPushButton(
            "Analyze Folder"
        )

        self.results_label = QLabel(
            "No analysis has been run."
        )

        self.layout().addWidget(
            self.folder_label
        )

        self.layout().addWidget(
            self.browse_button
        )

        self.layout().addWidget(
            self.analyze_button
        )

        self.layout().addWidget(
            self.results_label
        )

        self.browse_button.clicked.connect(
            self.select_folder
        )

        self.analyze_button.clicked.connect(
            self.run_analysis
        )

    def select_folder(
        self,
    ) -> None:
        """
        Open a folder selection dialog.
        """

        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Photo Folder",
        )

        if not folder:
            return

        self.selected_folder = folder

        self.folder_label.setText(
            f"Selected Folder:\n{folder}"
        )

    def run_analysis(
        self,
    ) -> None:
        """
        Run photo analysis.
        """

        if not self.selected_folder:

            self.results_label.setText(
                "Please select a folder first."
            )

            return

        try:

            self.results_label.setText(
                "Analyzing..."
            )

            report = (
                self.analyzer.analyze_folder(
                    self.selected_folder
                )
            )

            self.results_label.setText(
                (
                    "Archive Health Report\n\n"
                    f"Items: {report.total_items}\n"
                    f"Score: {report.score}\n"
                    f"Warnings: {report.warning_count}\n"
                    f"Errors: {report.error_count}\n"
                    f"Critical: {report.critical_count}\n\n"
                    f"{report.summary}"
                )
            )

        except Exception as ex:

            self.results_label.setText(
                f"Error:\n{ex}"
            )