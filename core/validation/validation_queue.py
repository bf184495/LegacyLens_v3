"""
LegacyLens V3

Validation Queue

Maintains ValidationRecord objects
generated during classification.

Responsible for:

- Queue management
- Statistics
- JSON export
- JSON import
"""

import json

from pathlib import Path

from datetime import datetime

from core.models.validation_record import (
    ValidationRecord
)


class ValidationQueue:

    def __init__(self):

        self.records = []

    #
    # Queue Operations
    #

    def add_record(
        self,
        record: ValidationRecord
    ):

        self.records.append(
            record
        )

    def clear(
        self
    ):

        self.records.clear()

    def count(
        self
    ) -> int:

        return len(
            self.records
        )

    #
    # Statistics
    #

    def build_statistics(
        self
    ) -> dict:

        total = len(
            self.records
        )

        if total == 0:

            return {

                "total_records": 0,

                "needs_validation": 0,

                "average_confidence": 0
            }

        confidence_values = [

            record.confidence

            for record in self.records

        ]

        average_confidence = round(
            sum(confidence_values)
            / len(confidence_values),
            2
        )

        needs_validation = sum(

            1

            for record
            in self.records

            if record.needs_validation
        )

        category_counts = {}

        validation_reasons = {}

        for record in self.records:

            #
            # Categories
            #

            category_counts[
                record.root_category
            ] = (

                category_counts.get(
                    record.root_category,
                    0
                )
                + 1
            )

            #
            # Validation Reasons
            #

            reason = (
                record.validation_reason
                or
                "none"
            )

            validation_reasons[
                reason
            ] = (

                validation_reasons.get(
                    reason,
                    0
                )
                + 1
            )

        return {

            "total_records":
                total,

            "needs_validation":
                needs_validation,

            "average_confidence":
                average_confidence,

            "categories":
                category_counts,

            "validation_reasons":
                validation_reasons,
        }

    #
    # Export
    #

    def export_json(
        self,
        output_file: str
    ):

        output_path = Path(
            output_file
        )

        document = {

            "generated_at":
                datetime.now().isoformat(),

            "summary":
                self.build_statistics(),

            "records": [

                record.to_dict()

                for record
                in self.records

            ]
        }

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as fp:

            json.dump(

                document,

                fp,

                indent=4,

                ensure_ascii=False
            )

    #
    # Future Import Support
    #

    def load_json(
        self,
        json_file: str
    ):

        with open(
            json_file,
            "r",
            encoding="utf-8"
        ) as fp:

            return json.load(fp)