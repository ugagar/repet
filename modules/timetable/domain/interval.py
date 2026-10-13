"""
Временной интервал 
"""


from dataclasses import dataclass
from datetime import datetime


@dataclass
class DatetimeInterval:
    dttm_from: datetime
    dttm_to: datetime

    def __post_init__(self) -> None:
        if self.dttm_from > self.dttm_to:
            raise ValueError(f"Invalid datetime interval: {self.dttm_from} > {self.dttm_to}")
