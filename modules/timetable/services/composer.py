"""
Составляет расписание за указанный период из 
list[Event] и list[TemplateTimetable]
"""
from timetable.domain.interval import DatetimeInterval
from timetable.domain.event import Event

class Composer:
    """
    Класс для сборки расписания
    """
    def compose(events: list[Event], interval: DatetimeInterval) -> list[Event]:
        pass