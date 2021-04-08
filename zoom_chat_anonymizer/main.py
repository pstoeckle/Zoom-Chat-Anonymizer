"""
Main module.
"""
from logging import INFO, basicConfig, getLogger
from os import walk
from os.path import join
from pathlib import Path as pathlib_Path
from subprocess import call
from sys import stdout
from typing import AbstractSet, Any, Optional, Sequence

from click import Context, Path, echo, group, option

from zoom_chat_anonymizer import __version__
from zoom_chat_anonymizer.anonymize_chat import anonymize_chat_internal

_LOGGER = getLogger(__name__)
basicConfig(
    format="%(levelname)s: %(asctime)s: %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=INFO,
    stream=stdout,
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

    :return:
    """


_INPUT_FOLDER_OPTION = option(
    "--input_folder",
    "-i",
    default="",
    type=Path(file_okay=False, exists=True, resolve_path=True),
)


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
    _LOGGER.info(f"Processing folder {folder_path}")
    for markdown_file in folder_path.glob("**/*.md"):
        html_file = str(markdown_file).replace(".md", ".html")
        command_to_execute = [
            "pandoc",
            str(markdown_file),
            "-o",
            html_file,
        ]
        if bib_file is not None:
            command_to_execute += ["--bibliography", bib_file]
        _LOGGER.info(f"Converting {markdown_file} to {html_file}")
        call(command_to_execute)


if __name__ == "__main__":
    main_group()
