"""
Порты модуля timetable. (Что нужно для работы)
"""


class Repository(Protocol):
    def get(): pass
    def update(): pass
    def save(): pass
    def delete(): pass


class Printer(Protocol):
    def print(): pass

