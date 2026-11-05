"""
photo_analyzer.py

Photo analysis orchestration for LegacyLens V3.
"""

from platform.archive_health import (
    ArchiveHealthEngine,
)

from .scanner import scan_folder
from .metadata import get_metadata
from .photo_health import PhotoHealthAnalyzer
from .duplicates import find_exact_duplicates


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

        #
        # Duplicate scan
        #

        duplicate_pairs = (
            find_exact_duplicates(
                folder_path
            )
        )

        duplicate_count = len(
            duplicate_pairs
        )

        #
        # Metadata / Health Scan
        #

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

        #
        # Temporary duplicate reporting
        #

        report.summary = (
            f"Exact duplicate pairs: "
            f"{duplicate_count}"
        )

        return report