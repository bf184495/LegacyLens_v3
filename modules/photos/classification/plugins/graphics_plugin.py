"""
LegacyLens V3

Graphics Classification Plugin

Determines whether an image is likely:

- Program Graphic
- Logo
- Icon
- UI Asset
- Technical Graphic

Scoring is based on:

- Path analysis
- Filename analysis
- Resolution
- Metadata presence
"""

from .base_plugin import ClassificationPlugin


class GraphicsPlugin(ClassificationPlugin):

    @property
    def name(self) -> str:

        return "GraphicsPlugin"

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

        width = metadata.get(
            "width",
            0
        )

        height = metadata.get(
            "height",
            0
        )

        megapixels = metadata.get(
            "megapixels",
            0
        )

        # -------------------------
        # Path Analysis
        # -------------------------

        graphic_paths = (

            "appdata",
            "assets",
            "icons",
            "extension",
            "node_modules",
            "office",
            "edge",
            "packageresources"

        )

        if any(
            hint in path
            for hint in graphic_paths
        ):

            score += 70

            reasons.append(
                "graphic asset path"
            )

        # -------------------------
        # Filename Analysis
        # -------------------------

        graphic_names = (

            "icon",
            "favicon",
            "logo",
            "thumb",
            "thumbnail",
            "sprite",
            "button",
            "banner",
            "toolbar",
            "background",
            "wallpaper"

        )

        if any(
            hint in filename
            for hint in graphic_names
        ):

            score += 40

            reasons.append(
                "graphics filename"
            )

        # -------------------------
        # QR Code Detection
        # -------------------------

        if (
            "qr" in filename
            or
            "qrcode" in filename
        ):

            score += 100

            reasons.append(
                "QR naming convention"
            )

            return {

                "root_category":
                    "Technical Graphics",

                "subcategory":
                    "QR Code",

                "score":
                    100,

                "reasons":
                    reasons
            }

        # -------------------------
        # Small Assets
        # -------------------------

        if (
            width <= 256
            and
            height <= 256
        ):

            score += 50

            reasons.append(
                "small graphic dimensions"
            )

        if megapixels < 0.10:

            score += 30

            reasons.append(
                "very low megapixels"
            )

        # -------------------------
        # Camera Penalty
        # -------------------------

        if metadata.get(
            "camera_make"
        ):

            score -= 30

            reasons.append(
                "camera metadata present"
            )

        if metadata.get(
            "camera_model"
        ):

            score -= 20

            reasons.append(
                "camera model present"
            )

        score = max(
            0,
            min(score, 100)
        )

        # -------------------------
        # Determine Subcategory
        # -------------------------

        subcategory = (
            self._determine_subcategory(
                filename
            )
        )

        return {

            "root_category":
                "Technical Graphics",

            "subcategory":
                subcategory,

            "score":
                score,

            "reasons":
                reasons
        }

    def _determine_subcategory(
        self,
        filename: str
    ) -> str:

        if "logo" in filename:

            return "Logo"

        if (
            "icon" in filename
            or
            "favicon" in filename
        ):

            return "Icon"

        if any(
            x in filename
            for x in (
                "button",
                "toolbar"
            )
        ):

            return "UI Asset"

        if (
            "diagram" in filename
            or
            "flowchart" in filename
        ):

            return "Diagram"

        if "chart" in filename:

            return "Chart"

        return "Program Graphic"