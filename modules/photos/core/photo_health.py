"""
photo_health.py

Photo-specific health analysis.

Converts photo metadata findings into
platform HealthIssue objects.
"""

from pathlib import Path

from core.models import HealthIssue
from core.archive_health import Severity


class PhotoHealthAnalyzer:
    """
    Generates photo health findings from
    photo metadata records.
    """

    def analyze(
        self,
        metadata: dict,
        file_path: str,
    ) -> list[HealthIssue]:
        """
        Analyze metadata and generate
        HealthIssue objects.
        """

        issues: list[HealthIssue] = []

        filename = Path(file_path).name

        #
        # File unreadable
        #

        if not metadata.get(
            "readable",
            True
        ):

            issues.append(
                HealthIssue(
                    issue_id=(
                        f"PHOTO-ERROR-{filename}"
                    ),
                    module="photos",
                    severity=Severity.ERROR,
                    category="readability",
                    title="Unreadable Image",
                    description=(
                        metadata.get(
                            "error",
                            "Image could not be read."
                        )
                    ),
                    item_id=file_path,
                    source_path=file_path,
                )
            )

        #
        # Missing capture date
        #

        if not metadata.get(
            "date_taken"
        ):

            issues.append(
                HealthIssue(
                    issue_id=(
                        f"PHOTO-DATE-{filename}"
                    ),
                    module="photos",
                    severity=Severity.WARNING,
                    category="metadata",
                    title="Missing Capture Date",
                    description=(
                        f"{filename} does not "
                        f"contain a capture date."
                    ),
                    item_id=file_path,
                    source_path=file_path,
                )
            )

        #
        # Missing camera metadata
        #

        if (
            not metadata.get(
                "camera_make"
            )
            and not metadata.get(
                "camera_model"
            )
        ):

            issues.append(
                HealthIssue(
                    issue_id=(
                        f"PHOTO-CAMERA-{filename}"
                    ),
                    module="photos",
                    severity=Severity.INFO,
                    category="metadata",
                    title="Missing Camera Metadata",
                    description=(
                        f"{filename} does not "
                        f"contain camera information."
                    ),
                    item_id=file_path,
                    source_path=file_path,
                )
            )

        #
        # Missing EXIF
        #

        if not metadata.get(
            "exif_present",
            False
        ):

            issues.append(
                HealthIssue(
                    issue_id=(
                        f"PHOTO-EXIF-{filename}"
                    ),
                    module="photos",
                    severity=Severity.INFO,
                    category="metadata",
                    title="Missing EXIF Metadata",
                    description=(
                        f"{filename} contains "
                        f"no EXIF metadata."
                    ),
                    item_id=file_path,
                    source_path=file_path,
                )
            )

        #
        # Zero-byte file
        #

        if (
            metadata.get(
                "file_size_bytes",
                0
            ) == 0
        ):

            issues.append(
                HealthIssue(
                    issue_id=(
                        f"PHOTO-ZERO-{filename}"
                    ),
                    module="photos",
                    severity=Severity.ERROR,
                    category="filesystem",
                    title="Zero-Byte File",
                    description=(
                        f"{filename} appears "
                        f"to contain no data."
                    ),
                    item_id=file_path,
                    source_path=file_path,
                )
            )

        return issues

    def analyze_duplicates(
        self,
        duplicate_pairs,
    ) -> list[HealthIssue]:
        """"
        Convert duplicate findings into
        HealthIssue objects.
        """

        issues: list[HealthIssue] = []

        for index, (
            original,
            duplicate,
        ) in enumerate(
            duplicate_pairs,
            start=1
        ):

            issues.append(
                HealthIssue(
                    issue_id=(
                        f"DUPLICATE-{index}"
                    ),
                    module="photos",
                    severity=Severity.WARNING,
                    category="duplicates",
                    title="Exact Duplicate File",
                    description=(
                        f"Duplicate detected. "
                        f"Original: {original}"
                    ),
                    item_id=duplicate,
                    source_path=duplicate,
                )
            )
            
        return issues