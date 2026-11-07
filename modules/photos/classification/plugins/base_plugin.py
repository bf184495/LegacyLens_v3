"""
LegacyLens V3

Classification Plugin Base Class

All classification plugins should inherit
from this class.

Examples:

    PhotoPlugin
    ScreenshotPlugin
    GraphicsPlugin
    AdultContentPlugin
"""

from abc import ABC
from abc import abstractmethod


class ClassificationPlugin(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def score(self, metadata: dict) -> dict:
        """
        Returns:

        {
            "root_category": str,
            "subcategory": str,
            "score": int,
            "reasons": list[str]
        }
        """
        pass