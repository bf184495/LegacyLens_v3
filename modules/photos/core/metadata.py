import os
import warnings
from datetime import datetime

from PIL import Image

warnings.filterwarnings(
    "ignore",
    category=Image.DecompressionBombWarning
)

warnings.filterwarnings(
    "ignore",
    message="Palette images with Transparency"
)


def get_metadata(image_path):
    """
    Extract metadata from an image.

    Returns a dictionary containing:
        - file information
        - dimensions
        - EXIF metadata
        - archive health information
    """

    metadata = {
        "file_name": os.path.basename(image_path),
        "full_path": image_path,

        "width": 0,
        "height": 0,
        "megapixels": 0,

        "file_size_bytes": 0,
        "modified_at": "",

        "exif_present": False,
        "camera_make": "",
        "camera_model": "",
        "date_taken": "",

        # Existing health fields
        "readable": False,
        "error": "",

        # New archive-health fields
        "health_status": "unknown",
        "health_message": "",
        "health_warnings": [],
    }

    #
    # Filesystem metadata
    #
    try:
        stat = os.stat(image_path)

        metadata["file_size_bytes"] = stat.st_size

        metadata["modified_at"] = datetime.fromtimestamp(
            stat.st_mtime
        ).isoformat(
            timespec="seconds"
        )

        if stat.st_size == 0:
            metadata["health_warnings"].append(
                "Zero-byte file"
            )

    except OSError as ex:
        metadata["error"] = str(ex)
        metadata["readable"] = False
        metadata["health_status"] = "error"
        metadata["health_message"] = str(ex)
        return metadata

    #
    # Image validation / metadata extraction
    #
    try:
        with Image.open(image_path) as img:

            metadata["width"] = img.width
            metadata["height"] = img.height

            metadata["megapixels"] = round(
                (img.width * img.height) / 1_000_000,
                2
            )

            #
            # Force Pillow to actually read image data.
            #
            # This catches more corruption than simply
            # opening the file.
            #
            # img.verify()

        #
        # Reopen after verify()
        #
        with Image.open(image_path) as img:

            exif = img.getexif()

            if exif:

                metadata["exif_present"] = True

                metadata["camera_make"] = str(
                    exif.get(271, "")
                )

                metadata["camera_model"] = str(
                    exif.get(272, "")
                )

                metadata["date_taken"] = str(
                    exif.get(
                        36867,
                         exif.get(
                             306,
                             ""
                         ))
                )

            else:
                metadata["health_warnings"].append(
                    "Missing EXIF metadata"
                )

            if not metadata["date_taken"]:
                metadata["health_warnings"].append(
                    "Missing capture date"
                )
            
            if (
                not metadata["camera_make"]
                and not metadata["camera_model"]
            ):
                metadata["health_warnings"].append(
                    "Missing camera metadata"
                )

        metadata["readable"] = True

        #
        # Health classification
        #
        if metadata["health_warnings"]:

            metadata["health_status"] = "warning"

            metadata["health_message"] = "; ".join(
                metadata["health_warnings"]
            )

        else:

            metadata["health_status"] = "healthy"

            metadata["health_message"] = (
                "No archive health issues detected"
            )

    except Exception as ex:

        metadata["error"] = str(ex)

        metadata["readable"] = False

        metadata["health_status"] = "error"

        metadata["health_message"] = str(ex)

    return metadata


if __name__ == "__main__":

    image_path = input(
        "Image path: "
    ).strip()

    result = get_metadata(
        image_path
    )

    print()

    for key, value in result.items():

        print(
            f"{key}: {value}"
        )