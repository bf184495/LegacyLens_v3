from __future__ import annotations

from collections import defaultdict

from archive_graph.models import (
    EventNode,
    PhotoNode,
)
from archive_graph.services.graph_service import GraphService


class TimelineView:
    """
    Provides timeline-oriented access
    to Archive Graph content.

    Supports:
    - Photos by year
    - Events by year
    - Timeline summaries
    - Archive eras
    """

    def __init__(self, graph: GraphService):
        self.graph = graph

    # ---------------------------------------------------------
    # Photos
    # ---------------------------------------------------------

    def photos(self) -> list[PhotoNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, PhotoNode)
        ]

    # ---------------------------------------------------------
    # Events
    # ---------------------------------------------------------

    def events(self) -> list[EventNode]:
        return [
            node
            for node in self.graph.all_nodes()
            if isinstance(node, EventNode)
        ]

    # ---------------------------------------------------------
    # Photos by Year
    # ---------------------------------------------------------

    def photos_by_year(self) -> dict[int, list[PhotoNode]]:

        results = defaultdict(list)

        for photo in self.photos():

            if photo.capture_date is None:
                continue

            results[photo.capture_date.year].append(
                photo
            )

        return dict(results)

    # ---------------------------------------------------------
    # Events by Year
    # ---------------------------------------------------------

    def events_by_year(self) -> dict[int, list[EventNode]]:

        results = defaultdict(list)

        for event in self.events():

            if event.start_date is None:
                continue

            results[event.start_date.year].append(
                event
            )

        return dict(results)

    # ---------------------------------------------------------
    # Available Years
    # ---------------------------------------------------------

    def years(self) -> list[int]:

        years = set()

        for photo in self.photos():

            if photo.capture_date:
                years.add(
                    photo.capture_date.year
                )

        for event in self.events():

            if event.start_date:
                years.add(
                    event.start_date.year
                )

        return sorted(years)

    # ---------------------------------------------------------
    # Timeline Summary
    # ---------------------------------------------------------

    def summary(self) -> dict:

        years = self.years()

        return {
            "years": years,
            "year_count": len(years),
            "photo_years": len(
                self.photos_by_year()
            ),
            "event_years": len(
                self.events_by_year()
            ),
        }

    # ---------------------------------------------------------
    # Timeline Feed
    # ---------------------------------------------------------

    def timeline_feed(self) -> list[dict]:

        feed = []

        for year in self.years():

            feed.append(
                {
                    "year": year,
                    "photos": len(
                        self.photos_by_year().get(
                            year,
                            [],
                        )
                    ),
                    "events": len(
                        self.events_by_year().get(
                            year,
                            [],
                        )
                    ),
                }
            )

        return feed

    # ---------------------------------------------------------
    # Archive Span
    # ---------------------------------------------------------

    def archive_span(self) -> tuple[int, int] | None:

        years = self.years()

        if not years:
            return None

        return (
            min(years),
            max(years),
        )