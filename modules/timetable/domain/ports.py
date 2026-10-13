"""
Порты модуля timetable. (Что нужно для работы)
"""


class Repository(Protocol):
    def get(): pass
    def update(): pass
    def save(): pass
    def delete(): pass


class Viewer(Protocol):
    def view(): pass
