"""
Message
"""
from dataclasses import dataclass
from datetime import time
from re import compile as re_compile

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
