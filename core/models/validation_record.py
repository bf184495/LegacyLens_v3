"""
LegacyLens V3

Validation Record

Represents a full classification and
validation record for a single asset.

ValidationRecord is intended to be the
canonical source for:

- Validation Queue
- Validation Reports
- Dashboard Reporting
- Review Workflow
- Feedback / Learning
- Archive Intelligence
"""

from dataclasses import dataclass
from dataclasses import field

from datetime import datetime

from typing import List
from typing import Optional


@dataclass
class ValidationRecord:

    #
    # Identity
    #

    record_id: str

    file_name: str

    file_path: str

    file_extension: str

    #
    # File Information
    #

    file_size_bytes: int = 0

    width: int = 0

    height: int = 0

    megapixels: float = 0.0

    #
    # Metadata
    #

    exif_present: bool = False

    camera_make: str = ""

    camera_model: str = ""

    date_taken: str = ""

    modified_at: str = ""

    #
    # Classification
    #

    root_category: str = ""

    subcategory: str = ""

    confidence: int = 0

    classifier_name: str = ""

    classifier_version: str = ""

    requires_review: bool = False

    classification_reasons: List[str] = (
        field(default_factory=list)
    )

    #
    # Validation
    #

    needs_validation: bool = False

    validation_reason: str = ""

    #
    # Duplicate Detection
    #

    exact_duplicate: bool = False

    exact_duplicate_group: str = ""

    near_duplicate: bool = False

    near_duplicate_score: float = 0.0

    #
    # Archive Health
    #

    health_status: str = ""

    health_message: str = ""

    health_warnings: List[str] = (
        field(default_factory=list)
    )

    #
    # Future Review Workflow
    #

    review_status: str = "pending"

    review_decision: Optional[str] = None

    reviewed_by: Optional[str] = None

    reviewed_at: Optional[str] = None

    review_notes: Optional[str] = None

    #
    # Audit Fields
    #

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )

    updated_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat()
    )

    #
    # Serialization
    #

    def to_dict(
        self
    ) -> dict:

        return {

            "record_id":
                self.record_id,

            "file_name":
                self.file_name,

            "file_path":
                self.file_path,

            "file_extension":
                self.file_extension,

            "file_size_bytes":
                self.file_size_bytes,

            "width":
                self.width,

            "height":
                self.height,

            "megapixels":
                self.megapixels,

            "exif_present":
                self.exif_present,

            "camera_make":
                self.camera_make,

            "camera_model":
                self.camera_model,

            "date_taken":
                self.date_taken,

            "modified_at":
                self.modified_at,

            "root_category":
                self.root_category,

            "subcategory":
                self.subcategory,

            "confidence":
                self.confidence,

            "classifier_name":
                self.classifier_name,

            "classifier_version":
                self.classifier_version,

            "requires_review":
                self.requires_review,

            "classification_reasons":
                self.classification_reasons,

            "needs_validation":
                self.needs_validation,

            "validation_reason":
                self.validation_reason,

            "exact_duplicate":
                self.exact_duplicate,

            "exact_duplicate_group":
                self.exact_duplicate_group,

            "near_duplicate":
                self.near_duplicate,

            "near_duplicate_score":
                self.near_duplicate_score,

            "health_status":
                self.health_status,

            "health_message":
                self.health_message,

            "health_warnings":
                self.health_warnings,

            "review_status":
                self.review_status,

            "review_decision":
                self.review_decision,

            "reviewed_by":
                self.reviewed_by,

            "reviewed_at":
                self.reviewed_at,

            "review_notes":
                self.review_notes,

            "created_at":
                self.created_at,

            "updated_at":
                self.updated_at
        }