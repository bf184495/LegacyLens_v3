"""
LegacyLens V3

Classification Validator

Determines whether a classification
should be reviewed by a human.

Validator goals:

- Catch low-confidence classifications
- Catch explicit review requests
- Randomly sample high-confidence results
- Produce validation statistics
- Prepare for future learning workflows
"""

from __future__ import annotations

import random

from core.models.classification_result import (
    ClassificationResult
)


class ClassificationValidator:

    def __init__(
        self,
        sample_rate: float = 0.10,
        confidence_threshold: int = 60
    ):
        self.sample_rate = sample_rate
        self.confidence_threshold = (
            confidence_threshold
        )

        self.stats = {
            "validated": 0,
            "low_confidence": 0,
            "requires_review": 0,
            "needs_review_category": 0,
            "random_sample": 0,
            "skipped": 0,
        }

    def should_validate(
        self,
        result: ClassificationResult
    ) -> bool:

        reason = self.validation_reason(
            result
        )

        if reason == "none":

            self.stats["skipped"] += 1

            return False

        self.stats["validated"] += 1
        self.stats[reason] += 1

        return True

    def validation_reason(
        self,
        result: ClassificationResult
    ) -> str:

        if result.requires_review:

            return "requires_review"

        if (
            result.confidence
            < self.confidence_threshold
        ):

            return "low_confidence"

        if (
            result.root_category
            == "Needs Review"
        ):

            return (
                "needs_review_category"
            )

        if (
            random.random()
            < self.sample_rate
        ):

            return "random_sample"

        return "none"

    def build_validation_record(
        self,
        result: ClassificationResult
    ) -> dict:

        return {

            "root_category":
                result.root_category,

            "subcategory":
                result.subcategory,

            "confidence":
                result.confidence,

            "reason":
                self.validation_reason(
                    result
                ),

            "classifier":
                result.classifier_name,

            "version":
                result.classifier_version,
        }

    def get_statistics(
        self
    ) -> dict:

        return dict(
            self.stats
        )

    def reset_statistics(
        self
    ):

        for key in self.stats:

            self.stats[key] = 0