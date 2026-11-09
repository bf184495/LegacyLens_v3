from modules.photos.classification.plugins.screenshot_plugin import (
    ScreenshotPlugin
)


def test_screenshot():

    plugin = ScreenshotPlugin()

    result = plugin.score({

        "file_name":
            "Screenshot 2026-11-07.png",

        "full_path":
            r"C:\Users\Brad\Pictures\Screenshots"
    })

    assert (
        result["root_category"]
        == "Screenshots"
    )

    assert (
        result["score"] >= 80
    )