"""
LegacyLens V3

Classification Engine

Coordinates all classification plugins and
returns a standardized ClassificationResult.

This engine should contain:

    - Plugin orchestration
    - Result ranking
    - Confidence evaluation
    - Validation enforcement

This engine should NOT contain:

    - Photo analysis rules
    - Screenshot rules
    - Graphics rules
    - Adult content rules

Those belong inside plugins.
"""

from core.models.classification_result import (
    ClassificationResult
)

from modules.photos.classification.plugins.photo_plugin import (
    PhotoPlugin
)

from modules.photos.classification.plugins.screenshot_plugin import (
    ScreenshotPlugin
)

from modules.photos.classification.plugins.graphics_plugin import (
    GraphicsPlugin
)

from modules.photos.classification.plugins.document_plugin import (
    DocumentPlugin
)

from modules.photos.classification.plugins.internet_content_plugin import (
    InternetContentPlugin
)

from modules.photos.classification.plugins.adult_content_plugin import (
    AdultContentPlugin
)

from modules.photos.classification.plugins.archive_asset_plugin import (
    ArchiveAssetPlugin
)


class ClassificationEngine:

    def __init__(self):

        self.plugins = [

            AdultContentPlugin(),

            ArchiveAssetPlugin(),

            PhotoPlugin(),

            ScreenshotPlugin(),

            GraphicsPlugin(),

            DocumentPlugin(),

            InternetContentPlugin()

        ]

    def classify(
        self,
        metadata: dict
    ) -> ClassificationResult:

        candidate_results = []

        for plugin in self.plugins:

            try:

                result = plugin.score(
                    metadata
                )

                candidate_results.append(
                    result
                )

            except Exception as error:

                print(
                    f"[Classifier]"
                    f" {plugin.name}"
                    f" failed:"
                    f" {error}"
                )

        if not candidate_results:

            return self._default_result()

        winner = self._select_winner(
            candidate_results
        )

        return self._build_result(
            winner,
            candidate_results
        )

    def _select_winner(
        self,
        results: list
    ) -> dict:

        results = sorted(

            results,

            key=lambda x:
                x.get("score", 0),

            reverse=True

        )

        return results[0]

    def _build_result(
        self,
        winner: dict,
        all_results: list
    ) -> ClassificationResult:

        confidence = winner.get(
            "score",
            0
        )

        requires_review = (
            confidence < 60
        )

        review_reason = ""

        if confidence < 60:

            review_reason = (
                "Low confidence"
            )

        score_map = {}

        for result in all_results:

            category = (
                result.get(
                    "root_category",
                    "Unknown"
                )
            )

            score_map[
                category
            ] = result.get(
                "score",
                0
            )

        return ClassificationResult(

            root_category=
                winner.get(
                    "root_category",
                    "Needs Review"
                ),

            subcategory=
                winner.get(
                    "subcategory",
                    "Uncertain"
                ),

            confidence=
                confidence,

            reasons=
                winner.get(
                    "reasons",
                    []
                ),

            scores=
                score_map,

            requires_review=
                requires_review,

            review_reason=
                review_reason,

            classifier_name=
                "LegacyLens Classification Engine",

            classifier_version=
                "1.0"

        )

    def _default_result(
        self
    ) -> ClassificationResult:

        return ClassificationResult(

            root_category=
                "Needs Review",

            subcategory=
                "Unknown Content",

            confidence=0,

            reasons=[
                "No classification candidates returned"
            ],

            requires_review=True,

            review_reason=
                "No plugin produced a result"

        )