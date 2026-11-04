"""
bootstrap_legacylens_v3.py

Creates the initial LegacyLens V3 architecture.

Usage:

    python bootstrap_legacylens_v3.py --dry-run

        Preview changes only.

    python bootstrap_legacylens_v3.py

        Create folders and starter files.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent

DRY_RUN = "--dry-run" in sys.argv


DIRECTORIES = [

    # Platform
    "platform",
    "platform/archive_health",
    "platform/models",
    "platform/reporting",
    "platform/validation",
    "platform/search",
    "platform/scoring",
    "platform/relationships",
    "platform/timelines",

    # Modules Root
    "modules",

    # Photos
    "modules/photos",
    "modules/photos/core",
    "modules/photos/storage",
    "modules/photos/reports",
    "modules/photos/ui",

    # Contacts
    "modules/contacts",
    "modules/contacts/core",
    "modules/contacts/storage",
    "modules/contacts/reports",
    "modules/contacts/ui",

    # Documents
    "modules/documents",
    "modules/documents/core",
    "modules/documents/storage",
    "modules/documents/reports",
    "modules/documents/ui",

    # Email
    "modules/email",
    "modules/email/core",
    "modules/email/storage",
    "modules/email/reports",
    "modules/email/ui",

    # Calendar
    "modules/calendar",
    "modules/calendar/core",
    "modules/calendar/storage",
    "modules/calendar/reports",
    "modules/calendar/ui",

    # Knowledge
    "modules/knowledge",
    "modules/knowledge/core",
    "modules/knowledge/storage",
    "modules/knowledge/reports",
    "modules/knowledge/ui",

    # UI
    "ui",
    "ui/home",
    "ui/common",
    "ui/dialogs",
    "ui/themes",

    # Data
    "data",
    "data/cache",
    "data/history",
    "data/imports",
    "data/exports",
    "data/databases",

    # Misc.
    "docs",
    "docs/architecture",
    "docs/decisions",
    "docs/whitepapers",
    "docs/roadmaps",
    "resources",
    "reports",
]


MODEL_FILES = {

    "platform/models/archive_item.py": """
from dataclasses import dataclass

@dataclass
class ArchiveItem:
    item_id: str
    module: str
    title: str
    full_path: str
""",

    "platform/models/health_issue.py": """
from dataclasses import dataclass

@dataclass
class HealthIssue:
    issue_id: str
    module: str
    severity: str
    category: str
    title: str
    description: str
    recommendation: str
    auto_fixable: bool
    confidence: float
""",

    "platform/models/health_report.py": """
from dataclasses import dataclass, field

@dataclass
class HealthReport:
    score: int = 100
    healthy: int = 0
    warnings: int = 0
    errors: int = 0

    issues: list = field(default_factory=list)
""",

    "platform/models/module_info.py": """
from dataclasses import dataclass

@dataclass
class ModuleInfo:
    name: str
    version: str
    enabled: bool
    description: str
""",

    "platform/models/relationship.py": """
from dataclasses import dataclass

@dataclass
class Relationship:
    source_id: str
    target_id: str
    relationship_type: str
    confidence: float
""",

    "platform/models/scan_result.py": """
from dataclasses import dataclass

@dataclass
class ScanResult:
    module: str
    item_count: int
    warning_count: int
    error_count: int
""",

    "platform/models/timeline_event.py": """
from dataclasses import dataclass

@dataclass
class TimelineEvent:
    title: str
    date: str
    source_module: str
    description: str
"""
}


def log(message: str):
    print(message)


def create_directories():

    for directory in DIRECTORIES:

        path = ROOT / directory

        if DRY_RUN:

            log(
                f"[DRY RUN] "
                f"Would create directory: {path}"
            )

        else:

            path.mkdir(
                parents=True,
                exist_ok=True
            )


def create_init_files():

    for directory in DIRECTORIES:

        init_file = ROOT / directory / "__init__.py"

        if DRY_RUN:

            log(
                f"[DRY RUN] "
                f"Would create file: {init_file}"
            )

        else:

            init_file.touch(
                exist_ok=True
            )


def create_model_files():

    for relative_path, content in MODEL_FILES.items():

        file_path = ROOT / relative_path

        if file_path.exists():

            log(
                f"[SKIP] "
                f"Already exists: {file_path}"
            )

            continue

        if DRY_RUN:

            log(
                f"[DRY RUN] "
                f"Would create model: {file_path}"
            )

        else:

            file_path.write_text(
                content.strip() + "\n",
                encoding="utf-8"
            )

            log(
                f"[CREATE] {file_path}"
            )


def main():

    log("")
    log("LegacyLens V3 Bootstrap")
    log("=======================")
    log("")

    if DRY_RUN:

        log(
            "Running in DRY RUN mode"
        )

        log("")

    create_directories()

    create_init_files()

    create_model_files()

    log("")
    log("Bootstrap complete.")
    log("")


if __name__ == "__main__":
    main()