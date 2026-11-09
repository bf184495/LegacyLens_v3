from dataclasses import dataclass, field


@dataclass(slots=True)
class PersonNode:
    id: str

    display_name: str

    verified: bool = False

    face_cluster_size: int = 0

    confidence: float = 0.0

    representative_photo: str | None = None

    notes: str = ""

    metadata: dict = field(default_factory=dict)