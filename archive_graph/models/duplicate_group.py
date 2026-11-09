from dataclasses import dataclass, field


@dataclass(slots=True)
class DuplicateGroupNode:
    """
    Represents a duplicate cluster.
    """

    id: str

    exact_count: int = 0

    near_count: int = 0

    recoverable_space: int = 0

    confidence: float = 1.0

    metadata: dict = field(default_factory=dict)

    @property
    def total_items(self) -> int:
        return self.exact_count + self.near_count