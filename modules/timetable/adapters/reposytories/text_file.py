from pathlib import Path

from timetable.domain.event import Event
from timetable.domain.interval import DatetimeInterval


class TextFileRepo:
    """
    Хранилище расписания в текстовом файле
    """
    def __init__(self, file: Path) -> None:
        self._file = file
        self._create_file_if_not_exists()

    def _create_file_if_not_exists(self) -> None:
        if not self._file.exists():
            self._file.mkdir(parents=True, exist_ok=True)
            self._file.touch(exist_ok=True)

    def to_text(event: Event) -> str:
        return f"{event.start_dttm}|{event.end_dttm}|{event.title}|{event.describe}"
        
    def from_text(line: str) -> Event:
        return Event(*line.split("|"))


    def get(self, interval: DatetimeInterval) -> list[Event]:
        result = []
        with self._file.open(mode="r") as f:
            for line in f:
                event: Event = self.from_text(line)

                if event.end_dttm <= interval.dttm_from or event.start_dttm >= interval.dttm_to:
                    continue

                result.append(event)

    def update(self, event: Event) -> bool:  pass


    def save(self, event: Event) -> bool:
        with self._file.open(mode="+a") as f:
            f.write(self.to_text(event))

        
    def delete(self, event: Event) -> bool: pass


