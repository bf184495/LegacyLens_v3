from .base_plugin import ClassificationPlugin


class ArchiveAssetPlugin(
    ClassificationPlugin
):

    @property
    def name(self) -> str:
        return "ArchiveAssetPlugin"

    def score(
        self,
        metadata: dict
    ) -> dict:

        score = 0
        reasons = []
        subcategory = "Derived Asset"

        if metadata.get(
            "duplicate_exact"
        ):

            score = 100

            subcategory = (
                "Duplicate"
            )

            reasons.append(
                "exact duplicate"
            )

        elif metadata.get(
            "duplicate_near"
        ):

            score = 90

            subcategory = (
                "Near Duplicate"
            )

            reasons.append(
                "near duplicate"
            )

        return {

            "root_category":
                "Archive Assets",

            "subcategory":
                subcategory,

            "score":
                score,

            "reasons":
                reasons
        }