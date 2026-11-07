"""
LegacyLens V3
Classification Taxonomy Services

Provides a common interface for loading,
querying, validating, and flattening the
classification hierarchy.

All classifier logic should depend on this
module rather than directly reading the JSON.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional


TAXONOMY_FILE = (
    Path(__file__).parent / "taxonomy.json"
)


def load_taxonomy() -> Dict:
    """
    Load taxonomy from disk.
    """

    with open(
        TAXONOMY_FILE,
        "r",
        encoding="utf-8"
    ) as handle:

        return json.load(handle)


def get_root_categories() -> List[str]:
    """
    Return top-level categories.
    """

    taxonomy = load_taxonomy()

    return sorted(
        taxonomy.keys()
    )


def get_subcategories(
    root_category: str
) -> List[str]:
    """
    Return direct subcategories
    beneath a root category.
    """

    taxonomy = load_taxonomy()

    children = taxonomy.get(
        root_category,
        {}
    )

    return sorted(
        children.keys()
    )


def category_exists(
    root_category: str,
    subcategory: str
) -> bool:
    """
    Verify a category path exists.
    """

    taxonomy = load_taxonomy()

    return (
        root_category in taxonomy
        and subcategory
        in taxonomy[root_category]
    )


def validate_category_path(
    root_category: str,
    subcategory: str
) -> None:
    """
    Raise a ValueError if the category
    does not exist.
    """

    if not category_exists(
        root_category,
        subcategory
    ):
        raise ValueError(
            f"Invalid category path: "
            f"{root_category} -> {subcategory}"
        )


def flatten_taxonomy() -> List[dict]:
    """
    Return every valid category pair.

    Example:

    [
        {
            "root": "Photography",
            "subcategory": "Personal Photo"
        }
    ]
    """

    taxonomy = load_taxonomy()

    flattened = []

    for root, children in taxonomy.items():

        for subcategory in children.keys():

            flattened.append(
                {
                    "root": root,
                    "subcategory": subcategory
                }
            )

    return flattened


def get_all_subcategories() -> List[str]:
    """
    Return all known subcategories.
    """

    return sorted(
        item["subcategory"]
        for item in flatten_taxonomy()
    )


def find_root_category(
    subcategory: str
) -> Optional[str]:
    """
    Find the parent category for
    a given subcategory.
    """

    taxonomy = load_taxonomy()

    for root, children in taxonomy.items():

        if subcategory in children:

            return root

    return None


def get_default_classification():
    """
    Safe fallback classification.
    """

    return {
        "root_category": "Needs Review",
        "subcategory": "Uncertain"
    }


if __name__ == "__main__":

    print(
        "LegacyLens Taxonomy"
    )

    print()

    for category in get_root_categories():

        print(category)

        for sub in get_subcategories(
            category
        ):

            print(
                f"  - {sub}"
            )