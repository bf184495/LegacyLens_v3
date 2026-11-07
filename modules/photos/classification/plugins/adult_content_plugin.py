from .base_plugin import ClassificationPlugin


class AdultContentPlugin(
    ClassificationPlugin
):

    @property
    def name(self) -> str:
        return "AdultContentPlugin"

    def score(self, metadata: dict) -> dict:

        adult_score = metadata.get(
            "adult_score",
            0
        )

        reasons = []

        if adult_score:

            reasons.append(
                f"adult score: {adult_score}"
            )

        return {

            "root_category":
                "Adult Content",

            "subcategory":
                "Downloaded",

            "score":
                adult_score,

            "reasons":
                reasons
        }