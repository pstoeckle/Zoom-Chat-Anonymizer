"""
Artemis
"""
from dataclasses import dataclass
from typing import TypedDict


class ArtemisJSONStudent(TypedDict):
    """
    Artemis.
    """

    id: int
    firstName: str
    lastName: str
    email: str


@dataclass(frozen=True)
class ArtemisStudent(object):
    """
    Artemis.
    """

    id: int
    first_name: str
    last_name: str
    email: str

    @staticmethod
    def create_from_json(json_student: ArtemisJSONStudent) -> "ArtemisStudent":
        """

        :param json_student:
        :return:
        """
        return ArtemisStudent(
            id=json_student["id"],
            first_name=json_student["firstName"],
            last_name=json_student["lastName"],
            email=json_student["email"],
        )

    def __lt__(self, other: "ArtemisStudent"):
        return self.id < other.id
