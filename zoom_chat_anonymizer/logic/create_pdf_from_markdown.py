"""
Markdown to PDFs.

"""
from logging import getLogger
from os import linesep, remove
from pathlib import Path
from subprocess import call
from typing import MutableSequence, Optional, Sequence

_LOGGER = getLogger(__name__)


def create_pdf_from_markdown_internal(
    clean_up: bool,
    latex_path: Path,
    markdown_paths: Sequence[Path],
    output_path: Path,
    sheet_number: int,
    title: str,
) -> None:
    """

    :param clean_up:
    :param latex_path:
    :param markdown_paths:
    :param output_path:
    :param sheet_number:
    :param title:
    :return:
    """
    tex_paths: MutableSequence[Path] = []
    for markdown_path in markdown_paths:
        _LOGGER.info(f"Translating {markdown_path} into LaTex...")
        tex_path = markdown_path.parent.joinpath(markdown_path.stem + ".tex")
        call(
            [
                "pandoc",
                str(markdown_path),
                "--to",
                "latex",
                "--no-highlight",
                "-o",
                str(tex_path),
            ]
        )
        tex_paths.append(tex_path)
        _LOGGER.info(f"Done!")
    output_tex_path = output_path.parent.joinpath(output_path.stem + ".tex")
    _LOGGER.info(f"Writing {output_tex_path}...")
    with output_tex_path.open("w") as f_read:
        f_read.write(
            r"\providecommand{\mysheetnumber}{" + str(sheet_number) + "}" + linesep
        )
        f_read.write(r"\providecommand{\mysheettitle}{" + str(title) + "}" + linesep)
        f_read.write(latex_path.read_text())

        f_read.write(r"\begin{document}" + linesep)
        for tex_path in tex_paths:
            f_read.write(r"\input{" + str(tex_path) + "}" + linesep)
        f_read.write(r"\end{document}")
    _LOGGER.info("... done!")
    _LOGGER.info(f"Translating {output_tex_path} into PDF...")
    call(
        ["pdflatex", f"-output-directory={output_path.parent}", str(output_tex_path),]
    )
    call(
        ["pdflatex", f"-output-directory={output_path.parent}", str(output_tex_path),]
    )
    _LOGGER.info("... done!")
    if clean_up:
        _LOGGER.info("Removing intermediate files.")
        for tex_path in tex_paths:
            remove(tex_path)
        remove(output_tex_path)
        _LOGGER.info("... done!")
        for p in output_path.parent.glob(output_path.stem + "*"):
            if p.suffix.strip().casefold().endswith("pdf"):
                continue
            _LOGGER.info(f"Removing {p}")
            remove(p)
