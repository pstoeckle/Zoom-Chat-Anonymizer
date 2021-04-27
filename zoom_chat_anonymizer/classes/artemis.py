"""
Artemis
"""
from dataclasses import dataclass
from typing import Any, TypedDict


class ArtemisJSONStudent(TypedDict):
    """
    Artemis.
    """

    id: int
    firstName: str
    lastName: str
    email: str


@dataclass(frozen=True)
class Student(object):
    """
    Artemis.
    """

    first_name: str
    last_name: str
    email: str


class MoodleStudentCSV(TypedDict):
    """
    Moodle.
    """

    Vorname: str
    Nachname: str
    Matrikelnummer: str


@dataclass(frozen=True)
class MoodleStudent(Student):
    """
    Artemis.
    """

    matriculation_number: str

    @staticmethod
    def create_from_json(json_student: MoodleStudentCSV) -> "MoodleStudent":
        """

        :param json_student:
        :return:
        """
        if json_student["Matrikelnummer"] == "":
            json_student["Matrikelnummer"] = "-1"
        return MoodleStudent(
            first_name=json_student["Vorname"],
            last_name=json_student["Nachname"],
            matriculation_number=json_student["Matrikelnummer"],
            email=json_student["E-Mail-Adresse"],  # type: ignore
        )

    def __lt__(self, other: Any) -> bool:
        m_a = int(self.matriculation_number)
        m_b = int(other.matriculation_number)
        if m_a == -1 and m_b == -1:
            return bool(self.last_name < other.last_name)
        return m_a < m_b


@dataclass(frozen=True)
class ArtemisStudent(Student):
    """
    Artemis.
    """

    id: int

    @staticmethod
    def create_from_json(json_student: ArtemisJSONStudent) -> "ArtemisStudent":
        """

        :param json_student:
        :return:
        """
        if json_student.get("lastName") is None:
            # PS: LMU exception ...
            return ArtemisStudent(
                id=json_student["id"],
                first_name=json_student["firstName"].split(" ")[0],
                last_name=json_student["firstName"].split(" ")[-1],
                email=json_student["email"],
            )
        return ArtemisStudent(
            id=json_student["id"],
            first_name=json_student["firstName"],
            last_name=json_student["lastName"],
            email=json_student["email"],
        )

    def __lt__(self, other: "ArtemisStudent") -> bool:
        return self.id < other.id
