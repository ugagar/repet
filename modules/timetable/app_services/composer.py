"""
Составляет расписание за указанный период из 
list[Event] и list[TemplateTimetable]
"""
from timetable.domain.interval import DatetimeInterval
from timetable.domain.event import Event
from timetable.domain.template import TemplateTimetable

class Composer:
    """
    Класс для сборки расписания
    """
    def compose(templates: list[TemplateTimetable], events: list[Event], interval: DatetimeInterval) -> list[Event]:
        pass