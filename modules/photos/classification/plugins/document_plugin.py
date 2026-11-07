from .base_plugin import ClassificationPlugin


class DocumentPlugin(ClassificationPlugin):

    @property
    def name(self) -> str:
        return "DocumentPlugin"

    def score(self, metadata: dict) -> dict:

        score = 0
        reasons = []

        filename = metadata.get(
            "file_name",
            ""
        ).lower()

        document_terms = (

            "receipt",
            "invoice",
            "certificate",
            "form",
            "letter",
            "document",
            "contract",
            "statement",
            "bill"

        )

        if any(
            word in filename
            for word in document_terms
        ):
            score += 80

            reasons.append(
                "document filename indicators"
            )

        return {
            "root_category": "Documents",
            "subcategory": "Scanned Document",
            "score": min(score, 100),
            "reasons": reasons
        }