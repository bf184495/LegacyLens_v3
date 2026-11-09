from dataclasses import dataclass, field


@dataclass(slots=True)
class LocationNode:
    id: str

    name: str

    city: str = ""
    state: str = ""
    country: str = ""

    latitude: float | None = None
    longitude: float | None = None

    confidence: float = 0.0

    metadata: dict = field(default_factory=dict)