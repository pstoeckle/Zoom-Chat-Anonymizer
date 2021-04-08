"""
Main module.
"""
from logging import INFO, basicConfig, getLogger
from pathlib import Path as pathlib_Path
from sys import stdout
from typing import AbstractSet, Any, Sequence

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


@option("--tutor", "-t", multiple=True, default=None)
@option("--input_folder", "-i", default="", type=Path(file_okay=False, exists=True))
@option(
    "--output_folder", "-o", default="out", type=Path(file_okay=False, writable=True)
)
@main_group.command()
def anonymize_chat(input_folder: str, output_folder: str, tutor: Sequence[str]) -> None:
    """
    Anonymize Zoom chats.
    """
    input_folder_path = pathlib_Path(input_folder)
    output_folder_path = pathlib_Path(output_folder)
    tutor_set: AbstractSet[str] = frozenset(t.lower() for t in tutor)
    anonymize_chat_internal(input_folder_path, output_folder_path, tutor_set)


if __name__ == "__main__":
    main_group()
