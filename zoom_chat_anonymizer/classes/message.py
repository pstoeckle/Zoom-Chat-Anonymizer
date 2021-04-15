"""
Message
"""
from collections import Sequence
from dataclasses import dataclass
from datetime import datetime, time, timedelta
from re import compile as re_compile

from zoom_chat_anonymizer.classes.pause import Pause

_LINK = re_compile(r"(https://[^ ]+)")


@dataclass()
class Message(object):
    """
    Class.
    """

    text: str
    current_time: time
    author: str
    anonymized_author: str

    def sanitize(self) -> None:
        """

        :return:
        """
        self.text = _LINK.sub(r"[\1](\1)", self.text)

    def __str__(self) -> str:
        return f"**{self.current_time.strftime('%H:%M:%S')}**, *{self.anonymized_author}*: {self.text}"

    def make_time_relative(
        self, pauses: Sequence[Pause], starting_time: timedelta
    ) -> None:
        """
        Relative.
        :param pauses:
        :param starting_time:
        :return:
        """
        current_time = (
            datetime.combine(date=datetime.now().date(), time=self.current_time)
            - starting_time
        )
        for pause in pauses:
            if self.current_time > pause.from_time:
                current_time = current_time - pause.duration
        self.current_time = current_time # type: ignore
