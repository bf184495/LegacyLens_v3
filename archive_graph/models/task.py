from dataclasses import dataclass, field


@dataclass(slots=True)
class TaskNode:
    """
    Actionable work item surfaced
    by the Workbench.
    """

    id: str

    title: str

    task_type: str

    priority: str = "normal"

    status: str = "open"

    estimated_minutes: int = 0

    estimated_impact: float = 0.0

    metadata: dict = field(default_factory=dict)