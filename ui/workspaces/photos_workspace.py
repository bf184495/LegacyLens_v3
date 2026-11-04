"""
photos_workspace.py

Photos workspace for LegacyLens V3.
"""

from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
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

    TEST_FOLDER = r"C:\Photos"

    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Photos",
            parent,
        )

        self.analyzer = PhotoAnalyzer()

        self.analyze_button = QPushButton(
            "Analyze Folder"
        )

        self.results_label = QLabel(
            "No analysis has been run."
        )

        self.layout().addWidget(
            self.analyze_button
        )

        self.layout().addWidget(
            self.results_label
        )

        self.analyze_button.clicked.connect(
            self.run_analysis
        )

    def run_analysis(
        self,
    ) -> None:

        try:

            report = (
                self.analyzer.analyze_folder(
                    self.TEST_FOLDER
                )
            )

            self.results_label.setText(
                (
                    f"Items: {report.total_items}\n"
                    f"Score: {report.score}\n"
                    f"Warnings: {report.warning_count}\n"
                    f"Errors: {report.error_count}\n"
                    f"Critical: {report.critical_count}"
                )
            )

        except Exception as ex:

            self.results_label.setText(
                f"Error:\n{ex}"
            )
