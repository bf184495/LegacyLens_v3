"""
photo_analyzer.py

Photo analysis orchestration
for LegacyLens V3.
"""

from core.archive_health import (
    ArchiveHealthEngine,
)

from modules.photos.classification.classifier_engine import (
    ClassificationEngine
)

from modules.photos.classification.validator import (
    ClassificationValidator
)

from .scanner import scan_folder
from .metadata import get_metadata
from .photo_health import PhotoHealthAnalyzer
from .duplicates import find_exact_duplicates
from .duplicates_near import find_near_duplicates


class PhotoAnalyzer:
    """
    Orchestrates photo analysis.
    """

    def __init__(self):

        self.classifier = (
            ClassificationEngine()
        )

        self.validator = (
            ClassificationValidator()
        )

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

        self.health_engine.clear()

        image_files = scan_folder(
            folder_path
        )

        #
        # Exact duplicate scan
        #

        duplicate_pairs = (
            find_exact_duplicates(
                folder_path
            )
        )

        duplicate_count = len(
            duplicate_pairs
        )

        duplicate_issues = (
            self.health_analyzer.analyze_duplicates(
                duplicate_pairs
            )
        )

        self.health_engine.add_issues(
            duplicate_issues
        )

        #
        # Near duplicate scan
        #

        near_duplicate_pairs = (
            find_near_duplicates(
                folder_path
            )
        )

        near_duplicate_count = len(
            near_duplicate_pairs
        )

        print()
        print("=" * 60)
        print("NEAR DUPLICATE RESULTS")
        print("=" * 60)

        if not near_duplicate_pairs:

            print(
                "No near duplicate pairs found."
            )

        else:

            for match in near_duplicate_pairs:

                print()

                print(
                    f"Similarity: "
                    f"{match['similarity']}%"
                )

                print(
                    f"A: "
                    f"{match['file_a']}"
                )

                print(
                    f"B: "
                    f"{match['file_b']}"
                )

        print("=" * 60)
        print()

        #
        # Classification
        # Validation
        # Archive Health
        #

        validation_count = 0

        for image_path in image_files:

            metadata = get_metadata(
                image_path
            )

            classification = (
                self.classifier.classify(
                    metadata
                )
            )

            metadata[
                "root_category"
            ] = (
                classification.root_category
            )

            metadata[
                "subcategory"
            ] = (
                classification.subcategory
            )

            metadata[
                "classification_confidence"
            ] = (
                classification.confidence
            )

            needs_validation = (
                self.validator.should_validate(
                    classification
                )
            )

            metadata[
                "needs_validation"
            ] = needs_validation

            if needs_validation:

                validation_count += 1

                metadata[
                    "validation_reason"
                ] = (
                    self.validator.validation_reason(
                        classification
                    )
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

        report.summary = (
            f"Exact duplicate pairs: "
            f"{duplicate_count}\n"
            f"Near duplicate pairs: "
            f"{near_duplicate_count}\n"
            f"Validation Queue: "
            f"{validation_count}"
        )

        return report