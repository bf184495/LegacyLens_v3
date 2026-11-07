"""
LegacyLens V3 Classification Taxonomy
"""

import json
from pathlib import Path

DEFAULT_TAXONOMY = Path(
    "modules/photos/classification/taxonomy.json"
)

def load_taxonomy():
    with open(DEFAULT_TAXONOMY, "r", encoding="utf-8") as f:
        taxonomy = json.load(f)

    if CUSTOM_TAXONOMY.exists():
        with open(CUSTOM_TAXONOMY, "r", encoding="utf-8") as f:
            custom = json.load(f)

        merge_dicts(taxonomy, custom)

    return taxonomy


def merge_dicts(base, overlay):
    for key, value in overlay.items():
        if (
            key in base
            and isinstance(base[key], dict)
            and isinstance(value, dict)
        ):
            merge_dicts(base[key], value)
        else:
            base[key] = value


def get_all_categories(node=None, prefix=""):
    if node is None:
        node = load_taxonomy()

    categories = []

    for name, children in node.items():

        full = (
            f"{prefix}/{name}"
            if prefix
            else name
        )

        categories.append(full)

        if children:
            categories.extend(
                get_all_categories(
                    children,
                    full
                )
            )

    return categories