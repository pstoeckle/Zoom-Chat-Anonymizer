"""
Main module.
"""
from dataclasses import asdict, dataclass, is_dataclass
from json import JSONEncoder, dumps, loads
from logging import INFO, basicConfig, getLogger
from pathlib import Path as pathlib_Path
from sys import stdout
from typing import AbstractSet, Any, Mapping, Optional, Sequence, TypedDict

from click import Context, Path, echo, group, option

from zoom_chat_anonymizer import __version__
from zoom_chat_anonymizer.logic.anonymize_chat import anonymize_chat_internal
from zoom_chat_anonymizer.logic.create_html_from_markdown import (
    create_html_from_markdown_internal,
)

_LOGGER = getLogger(__name__)
basicConfig(
    format="%(levelname)s: %(asctime)s: %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=INFO,
    stream=stdout,
)
_INPUT_FOLDER_OPTION = option(
    "--input_folder",
    "-i",
    default="",
    type=Path(file_okay=False, exists=True, resolve_path=True),
)


def _print_version(ctx: Context, _: Any, value: Any) -> None:
    """

    :param ctx:
    :param _:
    :param value:
    :return:
    """
    if not value or ctx.resilient_parsing:
        return
    echo(__version__)
    ctx.exit()


@group()
@option(
    "--version",
    is_flag=True,
    callback=_print_version,
    expose_value=False,
    is_eager=True,
    help="Version",
)
def main_group() -> None:
    """
    Helpful script to process Zoom chats.
    """


@option("--tutor", "-t", multiple=True, default=None)
@_INPUT_FOLDER_OPTION
@option(
    "--output_folder",
    "-o",
    default="out",
    type=Path(file_okay=False, writable=True, resolve_path=True),
)
@main_group.command()
def anonymize_zoom_chats(
    input_folder: str, output_folder: str, tutor: Sequence[str]
) -> None:
    """
    Anonymize Zoom chats.
    """
    input_folder_path = pathlib_Path(input_folder)
    output_folder_path = pathlib_Path(output_folder)
    tutor_set: AbstractSet[str] = frozenset(t.lower() for t in tutor)
    anonymize_chat_internal(input_folder_path, output_folder_path, tutor_set)


@_INPUT_FOLDER_OPTION
@option(
    "--bib_file",
    type=Path(exists=True, dir_okay=False, resolve_path=True),
    default=None,
)
@main_group.command()
def create_html_from_markdown(input_folder: str, bib_file: Optional[str]) -> None:
    """
    Create HTML files from the markdown files.
    """
    folder_path = pathlib_Path(input_folder)
    create_html_from_markdown_internal(bib_file, folder_path)


class EnhancedJSONEncoder(JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


class ArtemisJSONStudent(TypedDict):
    id: int
    firstName: str
    lastName: str
    email: str


@dataclass(frozen=True)
class ArtemisStudent(object):
    id: int
    first_name: str
    last_name: str
    email: str

    @staticmethod
    def create_from_json(json_student: ArtemisJSONStudent) -> "ArtemisStudent":
        return ArtemisStudent(
            id=json_student["id"],
            first_name=json_student["firstName"],
            last_name=json_student["lastName"],
            email=json_student["email"],
        )

    def __lt__(self, other: "ArtemisStudent"):
        return self.id < other.id


@option("--input_file", "-i", type=Path(dir_okay=False, resolve_path=True, exists=True))
@option("--inplace", "-I", is_flag=True, default=False)
@main_group.command()
def clean_artemis_file(input_file: str, inplace: bool) -> None:
    input_file_path = pathlib_Path(input_file)

    content: Sequence[ArtemisJSONStudent] = loads(input_file_path.read_text())
    students = [ArtemisStudent.create_from_json(a) for a in content]
    students = sorted(students)

    new_file_path = pathlib_Path(
        input_file.replace(input_file_path.suffix, ".clean.json")
        if inplace
        else input_file
    )
    new_file_path.write_text(dumps(students, indent=4, cls=EnhancedJSONEncoder))


if __name__ == "__main__":
    main_group()
