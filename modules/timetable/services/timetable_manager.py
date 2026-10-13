"""
Класс-менеджер. 
Управляет:
    - созданием объектов расписания (Event, TimetableTemplate)
    - обновлением объектов расписания 
    - удалением объектов расписания 

Зависит от:
    - Repository
"""
from dataclasses import dataclass
from pydantic import BaseModel

from timetable.domain.ports import Repository
from timetable.domain.interval import DatetimeInterval


class UserRequest(BaseModel):
    pass


class TimetableManager:
    def __init__(self, repo: Repository):
        self._repo = repo

    def create():
        pass