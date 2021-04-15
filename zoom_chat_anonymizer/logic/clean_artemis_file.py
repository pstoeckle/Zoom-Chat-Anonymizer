"""
Clean Artemis file.
"""
from dataclasses import asdict, is_dataclass
from json import JSONEncoder, dumps, loads
from logging import getLogger
from pathlib import Path
from typing import Any, Sequence

from zoom_chat_anonymizer.classes.artemis import ArtemisJSONStudent, ArtemisStudent

_LOGGER = getLogger(__name__)


class EnhancedJSONEncoder(JSONEncoder):
    """
    JSON.
    """

    def default(self, o: Any) -> Any:
        """

        :param o:
        :return:
        """
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


def clean_artemis_file_internal(inplace: bool, input_file_path: Path) -> None:
    """

    :param inplace:
    :param input_file_path:
    :return:
    """
    content: Sequence[ArtemisJSONStudent] = loads(input_file_path.read_text())
    students = [ArtemisStudent.create_from_json(a) for a in content]
    students = sorted(students)
    new_file_path = Path(
        str(input_file_path).replace(input_file_path.suffix, ".clean.json")
        if not inplace
        else str(input_file_path)
    )
    _LOGGER.info(f"We have {len(students)} students in Artemis.")
    new_file_path.write_text(dumps(students, indent=4, cls=EnhancedJSONEncoder))
