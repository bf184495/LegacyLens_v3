from .base_plugin import ClassificationPlugin


class InternetContentPlugin(
    ClassificationPlugin
):

    @property
    def name(self) -> str:
        return "InternetContentPlugin"

    def score(self, metadata: dict) -> dict:

        score = 0
        reasons = []

        filename = metadata.get(
            "file_name",
            ""
        ).lower()

        internet_terms = (

            "meme",
            "reaction",
            "funny",
            "comic",
            "wallpaper",
            "facebook",
            "reddit",
            "twitter",
            "x_",
            "social"

        )

        if any(
            term in filename
            for term in internet_terms
        ):
            score += 75

            reasons.append(
                "internet content naming"
            )

        subcategory = (
            "Downloaded Image"
        )

        if "meme" in filename:
            subcategory = "Meme"

        elif "wallpaper" in filename:
            subcategory = "Wallpaper"

        elif "comic" in filename:
            subcategory = "Web Comic"

        return {
            "root_category":
                "Internet Content",

            "subcategory":
                subcategory,

            "score":
                min(score, 100),

            "reasons":
                reasons
        }