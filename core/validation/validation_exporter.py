"""
LegacyLens V3

Validation Exporter

Responsible for:

- Exporting validation_queue.json
- Exporting validation_stats.json
- Applying retention policies
- Maintaining historical snapshots
"""

import json

from pathlib import Path

from datetime import datetime

from core.validation.validation_queue import (
    ValidationQueue
)


class ValidationExporter:

    def __init__(
        self,
        config_file: str = (
            "data/config/"
            "validation_config.json"
        )
    ):

        self.config_file = Path(
            config_file
        )

        self.config = (
            self._load_config()
        )

    #
    # Configuration
    #

    def _load_config(
        self
    ) -> dict:

        if not self.config_file.exists():

            return {

                "validation_mode":
                    "history",

                "max_history":
                    100
            }

        with open(
            self.config_file,
            "r",
            encoding="utf-8"
        ) as fp:

            return json.load(fp)

    #
    # Export
    #

    def export(
        self,
        queue: ValidationQueue
    ):

        mode = self.config.get(
            "validation_mode",
            "history"
        )

        latest_queue = Path(
            "data/validation/"
            "validation_queue.json"
        )

        latest_stats = Path(
            "data/validation/"
            "validation_stats.json"
        )

        #
        # Always write latest
        #

        queue.export_json(
            str(latest_queue)
        )

        self._export_stats(
            queue,
            latest_stats
        )

        #
        # History Mode
        #

        if mode in (
            "history",
            "rolling",
            "archive"
        ):

            self._write_history(
                queue
            )

        #
        # Rolling Retention
        #

        if mode == "rolling":

            self._cleanup_history()

    #
    # Statistics
    #

    def _export_stats(
        self,
        queue: ValidationQueue,
        output_file: Path
    ):

        stats = (
            queue.build_statistics()
        )

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as fp:

            json.dump(

                stats,

                fp,

                indent=4,

                ensure_ascii=False
            )

    #
    # Historical Snapshots
    #

    def _write_history(
        self,
        queue: ValidationQueue
    ):

        history_folder = Path(
            "data/validation/history"
        )

        history_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = (
            datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )
        )

        output_file = (
            history_folder
            /
            f"validation_queue_"
            f"{timestamp}.json"
        )

        queue.export_json(
            str(output_file)
        )

    #
    # Rolling Cleanup
    #

    def _cleanup_history(
        self
    ):

        max_history = (
            self.config.get(
                "max_history",
                100
            )
        )

        history_folder = Path(
            "data/validation/history"
        )

        if not history_folder.exists():

            return

        files = sorted(

            history_folder.glob(
                "validation_queue_*.json"
            ),

            key=lambda f:
            f.stat().st_mtime

        )

        while (
            len(files)
            > max_history
        ):

            oldest = files.pop(0)

            oldest.unlink()