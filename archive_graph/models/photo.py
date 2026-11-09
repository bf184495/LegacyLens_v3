from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class PhotoNode:
    id: str

    filename: str
    path: str

    capture_date: datetime | None = None

    width: int = 0
    height: int = 0

    file_size: int = 0

    sha256: str = ""
    phash: str = ""

    category: str = "UNKNOWN"

    confidence: float = 1.0

    thumbnail_path: str = ""

    review_status: str = "pending"

    metadata: dict = field(default_factory=dict)