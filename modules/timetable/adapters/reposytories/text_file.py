from pathlib import Path
from datetime import datetime

from domain.event import Event
from domain.interval import DatetimeInterval


class TextFileRepo:
    """
    Хранилище расписания в текстовом файле
    """
    def __init__(self, file: Path) -> None:
        self._file = file
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self) -> None:
        if not self._file.exists():
            self._file.touch(exist_ok=True)

    @staticmethod
    def to_text(event: Event) -> str:
        return f"{event.start_dttm}|{event.end_dttm}|{event.title}|{event.describe}\n"

    @staticmethod
    def from_text(line: str) -> Event:
        dttm_start, dttm_end, title,  desc = line.split("|")
        return Event(
            start_dttm=datetime.fromisoformat(dttm_start),
            end_dttm=datetime.fromisoformat(dttm_end),
            title=title,
            describe=desc,
        )


    def get(self, interval: DatetimeInterval) -> list[Event]:
        result: list[Event] = []
        with self._file.open(mode="r", encoding="utf-8") as f:
            for line in f:
                event: Event = self.from_text(line)

                if event.end_dttm <= interval.dttm_from or event.start_dttm >= interval.dttm_to:
                    continue

                result.append(event)
        return result

    def update(self, event: Event) -> bool:  pass


    def save(self, event: Event) -> bool:
        with self._file.open(mode="+a", encoding="utf-8") as f:
            f.write(self.to_text(event))

        
    def delete(self, event: Event) -> bool: pass


