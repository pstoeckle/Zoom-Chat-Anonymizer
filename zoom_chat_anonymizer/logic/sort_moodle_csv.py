"""
Sort.
"""
from csv import DictReader
from json import dumps
from logging import getLogger
from pathlib import Path
from typing import Sequence

from zoom_chat_anonymizer.classes.artemis import MoodleStudent
from zoom_chat_anonymizer.logic.clean_artemis_file import EnhancedJSONEncoder

_LOGGER = getLogger(__name__)


def sort_moodle_csv_internal(input_file_path: Path) -> None:
    """

    :param input_file_path:
    :return:
    """
    text = input_file_path.read_text(encoding="utf-8-sig")
    delimiter = "," if text.count(",") > text.count(";") else ";"
    with input_file_path.open(encoding="utf-8-sig") as f_read:
        students: Sequence[MoodleStudent] = [
            MoodleStudent.create_from_json(row)  # type: ignore
            for row in DictReader(f_read, delimiter=delimiter)
        ]
    students = sorted(students)
    new_file_path = Path(
        str(input_file_path).replace(input_file_path.suffix, ".clean.json")
    )
    _LOGGER.info(f"We have {len(students)} students in Moodle.")
    new_file_path.write_text(dumps(students, indent=4, cls=EnhancedJSONEncoder))
