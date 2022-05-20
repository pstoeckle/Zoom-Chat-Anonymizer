"""
create_html_from_markdown.
"""
from logging import getLogger
from pathlib import Path
from subprocess import call
from typing import Optional

_LOGGER = getLogger(__name__)


def create_html_from_markdown_internal(
    bib_file: Optional[Path], folder_path: Path
) -> None:
    """

    :param bib_file:
    :param folder_path:
    :return:
    """
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
            command_to_execute += ["--bibliography", str(bib_file)]
        _LOGGER.info(f"Converting {markdown_file} to {html_file}")
        call(command_to_execute)
