from .base_plugin import ClassificationPlugin


class ScreenshotPlugin(ClassificationPlugin):

    @property
    def name(self) -> str:
        return "ScreenshotPlugin"

    def score(self, metadata: dict) -> dict:

        score = 0
        reasons = []

        filename = metadata.get(
            "file_name",
            ""
        ).lower()

        path = metadata.get(
            "full_path",
            ""
        ).lower()

        screenshot_terms = (
            "screenshot",
            "screen shot",
            "capture",
            "snip",
            "snipping"
        )

        if any(
            term in filename
            for term in screenshot_terms
        ):
            score += 80
            reasons.append(
                "screenshot filename"
            )

        if "screenshots" in path:
            score += 20
            reasons.append(
                "screenshots folder"
            )

        return {
            "root_category": "Screenshots",
            "subcategory": "Desktop Screenshot",
            "score": min(score, 100),
            "reasons": reasons
        }