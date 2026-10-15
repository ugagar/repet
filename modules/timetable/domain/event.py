"""
Модель событий в расписании/графике
"""
from dataclasses import dataclass
from datetime import datetime




@dataclass
class Event:
    title: str
    describe: str
    start_dttm: datetime
    end_dttm: datetime
