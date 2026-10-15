"""
Порты модуля timetable. (Что нужно для работы)
"""
from typing import Protocol

from timetable.domain.event import Event
from timetable.domain.interval import DatetimeInterval


class Repository(Protocol):
    def get(self, interval: DatetimeInterval) -> list[Event]: ...
    def update(self, event: Event) -> bool: ...
    def save(self, event: Event) -> bool: ...
    def delete(self, event: Event) -> bool: ...


class Viewer(Protocol):
    def view(): pass
