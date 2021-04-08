"""
Copy.
"""
from datetime import time
from functools import partial
from os import linesep
from pathlib import Path
from re import compile as re_compile
from typing import AbstractSet, List, Mapping, MutableMapping

from zoom_chat_anonymizer.classes.message import Message

_PATTERN = re_compile(r"^([0-9:]+)\s+Von\s+(.*) : (.*)$")
_REFERENCE = re_compile(r"@([^:]+):")


def anonymize_chat_internal(
    input_folder_path: Path, output_folder_path: Path, tutor_set: AbstractSet[str]
) -> None:
    """

    :param input_folder_path:
    :param output_folder_path:
    :param tutor_set:
    :return:
    """
    if not output_folder_path.is_dir():
        output_folder_path.mkdir()
    files = [
        f
        for f in input_folder_path.iterdir()
        if f.is_file() and not f.stem.startswith(".")
    ]
    for file in files:
        new_file = output_folder_path.joinpath(file.stem + ".md")
        _anonymize_single_file(file, new_file, tutor_set)


def _find_name_in_dict_with_tutors(
    c_name: str, tutors: AbstractSet[str], author_to_anonymised_name: Mapping[str, str]
) -> str:
    """

    :param c_name:
    :param tutors:
    :param author_to_anonymised_name:
    :return:
    """
    strip = c_name.lower().strip()
    if strip in author_to_anonymised_name.keys():
        return author_to_anonymised_name[strip]
    for key, value in author_to_anonymised_name.items():
        if strip in key.lower().replace(" ", ""):
            return value
    if strip == "everyone" or strip == "everybody":
        return "everyone"
    for tutor in tutors:
        if strip in tutor:
            return c_name
    raise Exception(f"Name {c_name} is not known!")


def _anonymize_single_file(
    input_file: Path, output_file: Path, tutors: AbstractSet[str]
) -> None:
    """

    :param tutors:
    :param input_file:
    :param output_file:
    :return:
    """
    with input_file.open() as f_read:
        content = f_read.readlines()
    content = [line.strip() for line in content]
    messages: List[Message] = []
    author_to_anonymised_name: MutableMapping[str, str] = {}
    find_name_in_dict = partial(
        _find_name_in_dict_with_tutors,
        tutors=tutors,
        author_to_anonymised_name=author_to_anonymised_name,
    )

    last_message = None
    was_the_last_message_a_private_message = False
    for line in content:
        match = _PATTERN.match(line)
        if match:
            time_string = match.group(1)
            parts = time_string.split(":")
            c_hour = int(parts[0])
            c_minute = int(parts[1])
            c_second = int(parts[2])
            message = Message(
                match.group(3),
                time(hour=c_hour, minute=c_minute, second=c_second),
                match.group(2),
                "",
            )
            if "(privat)" not in message.author.lower():
                if message.author.lower() in tutors:
                    message.anonymized_author = message.author
                else:
                    if message.author.lower() not in author_to_anonymised_name.keys():
                        author_to_anonymised_name[
                            message.author.lower()
                        ] = "Student {}".format(len(author_to_anonymised_name.keys()))
                    message.anonymized_author = author_to_anonymised_name[
                        message.author.lower()
                    ]
                references: List[str] = _REFERENCE.findall(message.text)
                if len(references) > 0:
                    for reference in references:
                        if "+" in reference:
                            names = reference.split("+")

                            name_dict = {n.strip(): find_name_in_dict(n) for n in names}
                            for name, anonymized_name in name_dict.items():
                                message.text = message.text.replace(
                                    name, anonymized_name
                                )
                        else:
                            anonymized_name = find_name_in_dict(reference)
                            message.text = message.text.replace(
                                reference, anonymized_name
                            )
                messages.append(message)
                last_message = message
                was_the_last_message_a_private_message = False
            else:
                was_the_last_message_a_private_message = True
        else:
            if not was_the_last_message_a_private_message and last_message is not None:
                last_message.text += linesep + line
    for message in messages:
        message.sanitize()
    with output_file.open("w") as f_write:
        for message in messages:
            f_write.write(str(message) + linesep + linesep)
