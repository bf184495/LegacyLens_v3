from modules.photos.classification.classifier_engine import (
    ClassificationEngine
)


def test_engine_photo():

    engine = ClassificationEngine()

    result = engine.classify({

        "file_name":
            "IMG_1234.jpg",

        "camera_make":
            "Apple",

        "camera_model":
            "iPhone",

        "megapixels":
            12,

        "exif_present":
            True

    })

    assert (
        result.root_category
        == "Photography"
    )