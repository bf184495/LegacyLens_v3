from modules.photos.classification.plugins.photo_plugin import (
    PhotoPlugin
)


def test_camera_photo():

    plugin = PhotoPlugin()

    result = plugin.score({

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
        result["root_category"]
        == "Photography"
    )

    assert (
        result["score"] >= 70
    )