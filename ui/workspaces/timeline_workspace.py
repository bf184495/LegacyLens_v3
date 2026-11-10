from .base_workspace import BaseWorkspace


class TimelineWorkspace(
    BaseWorkspace
):
    def __init__(
        self,
        parent=None,
    ):
        super().__init__(
            "Timeline",
            parent,
        )