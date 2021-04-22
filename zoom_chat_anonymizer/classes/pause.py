"""
Pause.
"""
from dataclasses import dataclass
from datetime import datetime, time, timedelta
from typing import Sequence


@dataclass(frozen=True)
class Pause(object):
    """
    Pause.
    """

    from_time: time
    to_time: time

    @property
    def duration(self) -> timedelta:
        """
        Duration.
        :return:
        """
        return datetime.combine(
            date=datetime.now().date(), time=self.to_time
        ) - datetime.combine(date=datetime.now().date(), time=self.from_time)


@dataclass(frozen=True)
class PausesStart(object):
    """
    Pause.
    """

    start: timedelta
    pauses: Sequence[Pause]
