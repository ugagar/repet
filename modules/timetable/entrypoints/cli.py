"""
Точка входа для запуска из командной строки
"""
from datetime import datetime

from timetable.domain.event import Event
from timetable.domain.interval import DatetimeInterval
from timetable.adapters.reposytories.text_file import TextFileRepo


def create_event(dttm_from: datetime, dttm_to: datetime, title: str, describe: str):
    text_repo = TextFileRepo("event_repo.txt")
    event = Event(start_dttm=dttm_from, end_dttm=dttm_to, title=title, describe=describe)
    text_repo.save(event)


def get_event(dttm_from: datetime, dttm_to: datetime):
    text_repo = TextFileRepo("event_repo.txt")
    interval = DatetimeInterval(dttm_from=dttm_from, dttm_to=dttm_to)
    text_repo.save(interval)
