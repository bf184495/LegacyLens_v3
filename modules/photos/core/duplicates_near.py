import os
import warnings
from PIL import Image
import imagehash

# Large scans are legitimate; the bomb warning and palette-alpha notice are noise.
warnings.filterwarnings("ignore", category=Image.DecompressionBombWarning)
warnings.filterwarnings("ignore", message="Palette images with Transparency")
from collections import defaultdict
from itertools import combinations
from concurrent.futures import ThreadPoolExecutor
from .scanner import scan_folder


DEFAULT_THRESHOLD = 90


def generate_phash(image_path):

    try:

        with Image.open(image_path) as image:

            phash = imagehash.phash(
                image
            )

            return phash

    except Exception as ex:

            print()

            print(
                f"PHASH ERROR:"
            )

            print(
                image_path
            )

            print(
                ex
            )

            print()

            return None     

            return imagehash.phash(image)


def generate_phash_cached(args):
    image_path, cache = args

    cached = cache.get_phash(image_path) if cache else None

    if cached:
        return image_path, imagehash.hex_to_hash(cached)

    phash = generate_phash(image_path)

    if cache and phash is not None:
        cache.put_phash(image_path, str(phash))

    return image_path, phash


def similarity_percent(hash1, hash2):

    if hash1 is None:
        return 0

    if hash2 is None:
        return 0

    difference = hash1 - hash2

    similarity = 100 - (
        difference / 64 * 100
    )

    return round(similarity, 2)


def find_near_duplicates(
    folder_path,
    threshold=DEFAULT_THRESHOLD,
    image_files=None,
    cache=None,
):

    image_files = (
        image_files
        if image_files is not None 
        else scan_folder(folder_path)
    )
    
    hashes = {}
    results = []

    max_workers = min(8, max(1, os.cpu_count() or 1))

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for image_path, phash in executor.map(
            generate_phash_cached,
            [(path, cache) for path in image_files],
        ):
            print(image_path, phash)
            hashes[image_path] = phash


    if cache:
           cache.flush()

    valid = {path: int(str(value), 16) for path, value in hashes.items() if value is not None}
    # A pair within d Hamming bits must share at least one of d+1 disjoint
    # bit chunks. This avoids comparing every image pair in large collections.
    max_distance = max(0, min(64, int((100 - float(threshold)) * 64 / 100)))
    chunk_count = max_distance + 1
    boundaries = [round(i * 64 / chunk_count) for i in range(chunk_count + 1)]
    candidate_pairs = set()
    if max_distance >= 64:
        candidate_pairs = set(combinations(valid, 2))
    else:
        for chunk_index in range(chunk_count):
            low, high = boundaries[chunk_index], boundaries[chunk_index + 1]
            width = high - low
            mask = (1 << width) - 1
            buckets = defaultdict(list)
            for path, value in valid.items():
                buckets[(value >> low) & mask].append(path)
            for paths_in_bucket in buckets.values():
                if len(paths_in_bucket) > 1:
                    candidate_pairs.update(combinations(paths_in_bucket, 2))

    for file_a, file_b in candidate_pairs:
        similarity = similarity_percent(hashes[file_a], hashes[file_b])
        if similarity >= threshold:
            results.append({"file_a": file_a, "file_b": file_b, "similarity": similarity})

    return sorted(results, key=lambda match: (-match["similarity"], match["file_a"], match["file_b"]))


if __name__ == "__main__":

    folder = input(
        "Folder to analyze: "
    ).strip()

    threshold_text = input(
        "Similarity threshold (95 recommended): "
    ).strip()

    if threshold_text:

        threshold = int(
            threshold_text
        )

    else:

        threshold = DEFAULT_THRESHOLD

    matches = find_near_duplicates(

        folder,

        threshold

    )

    print()

    print(
        f"Near Duplicate Pairs Found: "
        f"{len(matches)}"
    )

    print()

    for match in matches:

        print(
            f"Similarity: "
            f"{match['similarity']}%"
        )

        print(
            match["file_a"]
        )

        print(
            match["file_b"]
        )

        print("-" * 60)
