"""Filesystem discovery for image archives; this stage never modifies files."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable

IMAGE_EXTENSIONS = frozenset({
    ".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tif", ".tiff",
    ".webp", ".heic", ".heif",
})


def is_image_file(filepath: str | os.PathLike[str]) -> bool:
    """Return whether a path has a supported image suffix."""
    return Path(filepath).suffix.lower() in IMAGE_EXTENSIONS


def scan_folder(folder_path: str | os.PathLike[str], *, exclude_dirs: Iterable[str] = ()) -> list[str]:
    """Return supported image paths recursively, in stable sorted order."""
    root_path = Path(folder_path)
    if not root_path.is_dir():
        return []
    excluded = set(exclude_dirs) | {"_LegacyLens_Trash", "_LegacyLens_Quarantine"}
    image_files: list[str] = []
    for root, dirs, files in os.walk(root_path):
        dirs[:] = sorted(d for d in dirs if d not in excluded)
        image_files.extend(str(Path(root) / name) for name in files if is_image_file(name))
    return sorted(image_files, key=str.casefold)


def count_images(folder_path: str | os.PathLike[str]) -> int:
    """Return the number of supported images beneath a folder."""
    return len(scan_folder(folder_path))
