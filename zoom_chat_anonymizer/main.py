"""
Main module.
"""
from collections import Counter
from datetime import datetime
from logging import INFO, basicConfig, getLogger
from pathlib import Path
from re import DOTALL
from re import compile as re_compile
from sys import stdout
from typing import AbstractSet, Any, List, Optional, Sequence

from click import Context, echo, group, option
from datetime import timedelta
from typer import Argument, Exit, Option, Typer
from zoom_chat_anonymizer import __version__
from zoom_chat_anonymizer.classes.artemis import ArtemisStudent
from zoom_chat_anonymizer.logic.anonymize_chat import anonymize_chat_internal
from zoom_chat_anonymizer.logic.clean_artemis_file import clean_artemis_file_internal
from zoom_chat_anonymizer.logic.create_html_from_markdown import (
    create_html_from_markdown_internal,
)
from zoom_chat_anonymizer.logic.create_pdf_from_markdown import (
    create_pdf_from_markdown_internal,
)
from zoom_chat_anonymizer.logic.sort_moodle_csv import sort_moodle_csv_internal

app = Typer()


def _version_callback(value: bool) -> None:
    if value:
        echo(f"zoom-chat-anonymizer {__version__}")
        raise Exit()


@app.callback()
def _call_back(
    _: bool = Option(
        None,
        "--version",
        "-v",
        is_flag=True,
        callback=_version_callback,
        expose_value=False,
        is_eager=True,
        help="Version",
    )
) -> None:
    """

    :return:
    """


_LOGGER = getLogger(__name__)
basicConfig(
    format="%(levelname)s: %(asctime)s: %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=INFO,
    filename="pdf-link-checker.log",
    filemode="w",
)
_INPUT_FOLDER_OPTION = Argument(
    ".",
    file_okay=False,
    exists=True,
    resolve_path=True,
)
_INPLACE = Option(False, "--inplace", "-I", is_flag=True)


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


_PATTERN = re_compile(r"^([0-9:]+)\t(.*):\t(.*)\n$", DOTALL)


@app.command()
def convert_to_old_format(
    input_file: Path = Argument(
        None, help="The file to convert", exists=True, dir_okay=False
    ),
) -> None:
    """
    Convert to old format.
    :param input_file:
    :return:
    """
    with input_file.open() as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if len(line) > 0:
            if (match := _PATTERN.match(line)) is not None:
                t = datetime.strptime(match.group(1), "%H:%M:%S")
                new_t = t + timedelta(hours=13)
                new_lines.append(
                    f"{new_t.strftime('%H:%M:%S')} Von {match.group(2)} an Alle : {match.group(3)}\n"
                )
            else:
                echo(line)
    with input_file.open("w") as f:
        f.writelines(new_lines)


@app.command()
def anonymize_zoom_chats(
    input_folder: Path = _INPUT_FOLDER_OPTION,
    output_folder: Path = Option(
        "out",
        "--output-folder",
        "-o",
        file_okay=False,
        writable=True,
        resolve_path=True,
    ),
    tutor: List[str] = Option(None, "--tutor", "-t"),
    pause_file: Optional[Path] = Option(
        None, "--pause-file", "-p", dir_okay=False, resolve_path=True, exists=True
    ),
    starting_time: str = Option("14:15", "--starting-time", "-s"),
) -> None:
    """
    Anonymize Zoom chats.
    """
    tutor_set: AbstractSet[str] = frozenset(t.lower() for t in tutor)
    anonymize_chat_internal(
        input_folder, output_folder, tutor_set, pause_file, starting_time
    )


@app.command()
def create_html_from_markdown(
    input_folder: Path = _INPUT_FOLDER_OPTION,
    bib_file: Optional[Path] = Option(
        None, "--bib-file", exists=True, dir_okay=False, resolve_path=True
    ),
) -> None:
    """
    Create HTML files from the markdown files.
    """
    create_html_from_markdown_internal(bib_file, input_folder)


_INPUT_FILE = option(
    "--input_file", "-i", type=Path(dir_okay=False, resolve_path=True, exists=True)
)


def clean_artemis_file(input_file: Path, inplace: bool = _INPLACE) -> None:
    """
    Clean Artemis JSON.
    """
    clean_artemis_file_internal(inplace, input_file)


def sort_moodle_csv(input_file: Path) -> None:
    """
    Moodle.
    """
    sort_moodle_csv_internal(input_file)


# @option(
#     "--output-file",
#     "-o",
#     type=Path(dir_okay=False, resolve_path=True),
#     default="test.pdf",
# )
# @option(
#     "--latex-header",
#     "-l",
#     type=Path(exists=True, dir_okay=False, resolve_path=True),
#     default="",
# )
# @option(
#     "--markdown-file",
#     "-m",
#     multiple=True,
#     default=None,
#     type=Path(exists=True, dir_okay=False, resolve_path=True),
# )
# @option("--sheet-number", "-n", type=int, prompt=True)
# @option("--title", "-t", prompt=True)
# @option("--clean-up", "-c", is_flag=True, default=False)
def create_pdf_from_markdown(
    markdown_file: Optional[Sequence[str]],
    latex_header: str,
    output_file: str,
    sheet_number: int,
    title: str,
    clean_up: bool,
) -> None:
    """
    Use the markdown description of the exercises to create a PDF.
    """
    title = title.replace("&", r"\&")
    output_path = pathlib_Path(output_file)
    latex_path = pathlib_Path(latex_header)
    markdown_paths = (
        [] if markdown_file is None else [pathlib_Path(m) for m in markdown_file]
    )
    create_pdf_from_markdown_internal(
        clean_up, latex_path, markdown_paths, output_path, sheet_number, title
    )


if __name__ == "__main__":
    app()
