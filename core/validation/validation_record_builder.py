"""
LegacyLens V3

Validation Record Builder

Builds ValidationRecord instances from:

- metadata
- classification results
- validator decisions

The builder centralizes record creation
so PhotoAnalyzer stays clean.
"""

from pathlib import Path

from core.models.validation_record import (
    ValidationRecord
)


class ValidationRecordBuilder:

    _record_counter = 0

    @classmethod
    def build(
        cls,
        metadata: dict,
        classification,
        validator_reason: str = "",
        needs_validation: bool = False
    ) -> ValidationRecord:

        cls._record_counter += 1

        file_path = metadata.get(
            "full_path",
            ""
        )

        path_obj = Path(
            file_path
        )

        return ValidationRecord(

            #
            # Identity
            #

            record_id=(
                f"VAL-{cls._record_counter:06d}"
            ),

            file_name=metadata.get(
                "file_name",
                ""
            ),

            file_path=file_path,

            file_extension=(
                path_obj.suffix.lower()
            ),

            #
            # File Information
            #

            file_size_bytes=metadata.get(
                "file_size_bytes",
                0
            ),

            width=metadata.get(
                "width",
                0
            ),

            height=metadata.get(
                "height",
                0
            ),

            megapixels=metadata.get(
                "megapixels",
                0.0
            ),

            #
            # Metadata
            #

            exif_present=metadata.get(
                "exif_present",
                False
            ),

            camera_make=metadata.get(
                "camera_make",
                ""
            ),

            camera_model=metadata.get(
                "camera_model",
                ""
            ),

            date_taken=metadata.get(
                "date_taken",
                ""
            ),

            modified_at=metadata.get(
                "modified_at",
                ""
            ),

            #
            # Classification
            #

            root_category=(
                classification.root_category
            ),

            subcategory=(
                classification.subcategory
            ),

            confidence=(
                classification.confidence
            ),

            classifier_name=(
                getattr(
                    classification,
                    "classifier_name",
                    "ClassificationEngine"
                )
            ),

            classifier_version=(
                getattr(
                    classification,
                    "classifier_version",
                    "1.0"
                )
            ),

            requires_review=(
                getattr(
                    classification,
                    "requires_review",
                    False
                )
            ),

            classification_reasons=(
                getattr(
                    classification,
                    "reasons",
                    []
                )
            ),

            #
            # Validation
            #

            needs_validation=(
                needs_validation
            ),

            validation_reason=(
                validator_reason
            ),

            #
            # Archive Health
            #

            health_status=metadata.get(
                "health_status",
                ""
            ),

            health_message=metadata.get(
                "health_message",
                ""
            ),

            health_warnings=metadata.get(
                "health_warnings",
                []
            ),

            #
            # Duplicate Information
            #

            exact_duplicate=False,

            exact_duplicate_group="",

            near_duplicate=False,

            near_duplicate_score=0.0,
        )