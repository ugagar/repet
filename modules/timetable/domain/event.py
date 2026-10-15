"""
Модель событий в расписании/графике
"""
from dataclasses import dataclass
from datetime import datetime




@dataclass
class Event:
    start_dttm: datetime
    end_dttm: datetime
    title: str
    describe: str
