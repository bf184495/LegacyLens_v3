"""
LegacyLens V3

Classification Result

The ClassificationResult represents the output of any
LegacyLens classification engine.

Initially used by:

    Photos

Future use:

    Documents
    Contacts
    Email
    Calendar
    Knowledge

Long-Term Vision:

    Person Classification
    Relationship Classification
    Event Classification
    Timeline Classification
    Archive Intelligence

This object should remain stable across the platform.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict
from typing import List
from typing import Optional


@dataclass
class ClassificationResult:

    # --------------------------------------------------
    # Primary Classification
    # --------------------------------------------------

    root_category: str

    subcategory: str

    confidence: int

    # --------------------------------------------------
    # Explainability
    # --------------------------------------------------

    reasons: List[str] = field(
        default_factory=list
    )

    scores: Dict[str, int] = field(
        default_factory=dict
    )

    metadata: Dict = field(
        default_factory=dict
    )

    # --------------------------------------------------
    # Review Workflow
    # --------------------------------------------------

    requires_review: bool = False

    review_reason: str = ""

    review_priority: str = "normal"

    # --------------------------------------------------
    # Human Validation
    # --------------------------------------------------

    human_verified: bool = False

    human_root_category: str = ""

    human_subcategory: str = ""

    human_notes: str = ""

    reviewed_by: str = ""

    reviewed_date: Optional[str] = None

    # --------------------------------------------------
    # Engine Information
    # --------------------------------------------------

    classifier_name: str = (
        "LegacyLens Classifier"
    )

    classifier_version: str = "1.0"

    classification_source: str = (
        "automated"
    )

    # --------------------------------------------------
    # Archive Intelligence
    # --------------------------------------------------

    related_entities: List[str] = field(
        default_factory=list
    )

    related_events: List[str] = field(
        default_factory=list
    )

    related_locations: List[str] = field(
        default_factory=list
    )

    tags: List[str] = field(
        default_factory=list
    )

    # --------------------------------------------------
    # Auditing
    # --------------------------------------------------

    created_utc: str = field(
        default_factory=lambda: (
            datetime.utcnow().isoformat()
        )
    )

    # --------------------------------------------------
    # Category Helpers
    # --------------------------------------------------

    def category_path(self) -> str:
        """
        Example:

        Photography/Personal Photo
        """

        return (
            f"{self.root_category}/"
            f"{self.subcategory}"
        )

    def human_category_path(self) -> str:
        """
        Human validated category path.
        """

        if (
            not self.human_root_category
            or
            not self.human_subcategory
        ):
            return ""

        return (
            f"{self.human_root_category}/"
            f"{self.human_subcategory}"
        )

    # --------------------------------------------------
    # Confidence Helpers
    # --------------------------------------------------

    def is_confident(self) -> bool:

        return self.confidence >= 80

    def is_low_confidence(self) -> bool:

        return self.confidence < 60

    # --------------------------------------------------
    # Review Helpers
    # --------------------------------------------------

    def mark_reviewed(
        self,
        root_category: str,
        subcategory: str,
        reviewer: str = "",
        notes: str = ""
    ):

        self.human_verified = True

        self.human_root_category = (
            root_category
        )

        self.human_subcategory = (
            subcategory
        )

        self.reviewed_by = reviewer

        self.human_notes = notes

        self.reviewed_date = (
            datetime.utcnow().isoformat()
        )

    # --------------------------------------------------
    # Export Helpers
    # --------------------------------------------------

    def to_dict(self) -> Dict:

        return {
            "root_category":
                self.root_category,

            "subcategory":
                self.subcategory,

            "confidence":
                self.confidence,

            "reasons":
                self.reasons,

            "scores":
                self.scores,

            "metadata":
                self.metadata,

            "requires_review":
                self.requires_review,

            "review_reason":
                self.review_reason,

            "review_priority":
                self.review_priority,

            "human_verified":
                self.human_verified,

            "human_root_category":
                self.human_root_category,

            "human_subcategory":
                self.human_subcategory,

            "human_notes":
                self.human_notes,

            "reviewed_by":
                self.reviewed_by,

            "reviewed_date":
                self.reviewed_date,

            "classifier_name":
                self.classifier_name,

            "classifier_version":
                self.classifier_version,

            "classification_source":
                self.classification_source,

            "related_entities":
                self.related_entities,

            "related_events":
                self.related_events,

            "related_locations":
                self.related_locations,

            "tags":
                self.tags,

            "created_utc":
                self.created_utc,
        }

    # --------------------------------------------------
    # Display
    # --------------------------------------------------

    def __str__(self):

        return (
            f"{self.category_path()} "
            f"({self.confidence}%)"
        )