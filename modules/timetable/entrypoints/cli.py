"""
Точка входа для запуска из командной строки
"""
from datetime import datetime
from pathlib import Path

from domain.event import Event
from domain.interval import DatetimeInterval
from adapters.reposytories.text_file import TextFileRepo


def create_event(dttm_from: datetime, dttm_to: datetime, title: str, describe: str):
    text_repo = TextFileRepo(Path("event_repo.txt"))
    event = Event(start_dttm=dttm_from, end_dttm=dttm_to, title=title, describe=describe)
    text_repo.save(event)


def get_event(dttm_from: datetime, dttm_to: datetime):
    text_repo = TextFileRepo(Path("event_repo.txt"))
    interval = DatetimeInterval(dttm_from=dttm_from, dttm_to=dttm_to)
    return text_repo.get(interval)
