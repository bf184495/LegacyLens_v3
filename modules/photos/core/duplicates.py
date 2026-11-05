import hashlib

from .scanner import scan_folder


def sha256_hash(filepath):
    """
    Generate a SHA256 hash
    for a file.
    """

    hash_object = hashlib.sha256()

    with open(filepath, "rb") as file:

        while True:

            chunk = file.read(65536)

            if not chunk:
                break

            hash_object.update(chunk)

    return hash_object.hexdigest()


def find_exact_duplicates(folder_path):
    """
    Scan folder and find files
    with identical SHA256 hashes.
    """

    hash_lookup = {}

    duplicate_groups = []

    image_files = scan_folder(
        folder_path
    )

    for image_path in image_files:

        file_hash = sha256_hash(
            image_path
        )

        if file_hash in hash_lookup:

            duplicate_groups.append(
                (
                    hash_lookup[file_hash],
                    image_path
                )
            )

        else:

            hash_lookup[file_hash] = (
                image_path
            )

    return duplicate_groups


if __name__ == "__main__":

    folder = input(
        "Folder to scan: "
    ).strip()

    duplicates = find_exact_duplicates(
        folder
    )

    print()

    print(
        f"Duplicate Pairs Found: "
        f"{len(duplicates)}"
    )

    print()

    for original, duplicate in duplicates:

        print("ORIGINAL:")
        print(original)

        print()

        print("DUPLICATE:")
        print(duplicate)

        print()

        print("-" * 60)