"""
photo_analyzer.py

Photo analysis orchestration for LegacyLens V3.

Pipeline:

scan_folder()
    ↓
get_metadata()
    ↓
PhotoHealthAnalyzer()
    ↓
HealthIssue objects
"""

from platform.archive_health import (
    ArchiveHealthEngine,
)

from .scanner import scan_folder
from .metadata import get_metadata
from .photo_health import PhotoHealthAnalyzer


class PhotoAnalyzer:
    """
    Orchestrates photo analysis for V3.
    """

    def __init__(self):

        self.health_engine = (
            ArchiveHealthEngine()
        )

        self.health_analyzer = (
            PhotoHealthAnalyzer()
        )

    def analyze_folder(
        self,
        folder_path: str,
    ):
        """
        Analyze an entire folder.

        Returns:
            HealthReport
        """

        self.health_engine.clear()

        image_files = scan_folder(
            folder_path
        )

        for image_path in image_files:

            metadata = get_metadata(
                image_path
            )

            issues = (
                self.health_analyzer.analyze(
                    metadata=metadata,
                    file_path=image_path,
                )
            )

            self.health_engine.add_issues(
                issues
            )

        report = (
            self.health_engine.build_report(
                report_id="PHOTO-HEALTH",
                module="photos",
                total_items=len(
                    image_files
                ),
            )
        )

        return report