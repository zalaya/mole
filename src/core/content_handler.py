import os

from src.core.file_reader import read_file_content


def concatenate_file_contents(file_paths: list[str]) -> str:
    """
    Concatenates the given file contents.

    :param file_paths: The list of file paths.
    :return: The concatenated file contents.
    """
    concatenated_content = ""

    for file_path in file_paths:
        try:
            content = read_file_content(file_path)
            file_name = os.path.basename(file_path)
            concatenated_content += f"File: {file_name}\n"

            if content.strip():
                concatenated_content += f"\n{content}\n"
            else:
                concatenated_content += f"{content}\n"
        except Exception as exception:
            print(f"Error reading file {file_path}: {exception}")

    return concatenated_content
