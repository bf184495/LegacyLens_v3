from modules.photos.classification.plugins.graphics_plugin import (
    GraphicsPlugin
)


def test_logo_file():

    plugin = GraphicsPlugin()

    result = plugin.score({

        "file_name":
            "company_logo.png",

        "width":
            128,

        "height":
            128,

        "megapixels":
            0.01

    })

    assert (
        result["root_category"]
        == "Technical Graphics"
    )

    assert (
        result["score"] > 50
    )