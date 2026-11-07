"""
LegacyLens V3

Photo Classification Plugin

Determines whether an item is likely
a personal photograph.

Scoring is based on:

- EXIF metadata
- Camera metadata
- Resolution
- Filename conventions
- Folder conventions
"""

from .base_plugin import ClassificationPlugin


class PhotoPlugin(ClassificationPlugin):

    @property
    def name(self) -> str:
        return "PhotoPlugin"

    def score(
        self,
        metadata: dict
    ) -> dict:

        score = 0

        reasons = []

        filename = (
            metadata.get(
                "file_name",
                ""
            )
            .lower()
        )

        path = (
            metadata.get(
                "full_path",
                ""
            )
            .lower()
        )

        # ----------------------------
        # EXIF
        # ----------------------------

        if metadata.get(
            "exif_present",
            False
        ):
            score += 25

            reasons.append(
                "contains EXIF metadata"
            )

        # ----------------------------
        # Camera
        # ----------------------------

        if metadata.get(
            "camera_make"
        ):
            score += 20

            reasons.append(
                "camera make present"
            )

        if metadata.get(
            "camera_model"
        ):
            score += 10

            reasons.append(
                "camera model present"
            )

        # ----------------------------
        # Resolution
        # ----------------------------

        megapixels = metadata.get(
            "megapixels",
            0
        )

        if megapixels >= 12:

            score += 20

            reasons.append(
                "high resolution photo"
            )

        elif megapixels >= 5:

            score += 10

            reasons.append(
                "photo-sized image"
            )

        # ----------------------------
        # Filename Patterns
        # ----------------------------

        photo_patterns = (

            "img_",
            "pxl_",
            "dsc",
            "mvimg",
            "fb_img",
            "received_",
            "photo_",
            "202",
            "20"

        )

        if (
            filename.startswith(photo_patterns)
            or
            filename[:8].isdigit()
        ):

            score += 20

            reasons.append(
                "camera filename pattern"
            )

        # Facebook image naming

        if filename.startswith(
            "fb_img"
        ):

            score += 25

            reasons.append(
                "facebook image pattern"
            )

        # Mobile camera naming

        if filename.startswith(
            "img_"
        ):

            score += 15

            reasons.append(
                "mobile camera pattern"
            )

        # Samsung camera naming

        if filename[:8].isdigit():

            score += 10

            reasons.append(
                "date-based camera filename"
            )

        # ----------------------------
        # Folder Clues
        # ----------------------------

        photo_folders = (

            "camera",
            "photos",
            "pictures",
            "dcim",
            "family",
            "vacation",
            "travel"

        )

        if any(
            folder in path
            for folder in photo_folders
        ):

            score += 10

            reasons.append(
                "photo folder path"
            )

        # ----------------------------
        # Size Penalties
        # ----------------------------

        width = metadata.get(
            "width",
            0
        )

        height = metadata.get(
            "height",
            0
        )

        if (
            width <= 256
            and
            height <= 256
        ):

            score -= 20

            reasons.append(
                "very small image"
            )

        score = max(
            0,
            min(score, 100)
        )

        return {

            "root_category":
                "Photography",

            "subcategory":
                "Personal Photo",

            "score":
                score,

            "reasons":
                reasons

        }