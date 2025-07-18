import os

from src.configuration.constants import ALLOWED_FILE_EXTENSIONS


def is_supported_file_extension(file_path: str) -> bool:
    """
    Returns True if the given filepath points to a text file, False otherwise.

    :param file_path: The filepath to check.
    :return: True if the given filepath points to a text file, False otherwise.
    """
    _, extension = os.path.splitext(file_path)
    return extension.lower() in ALLOWED_FILE_EXTENSIONS


def find_file_paths(root_directory: str) -> list[str]:
    """
    Recursively finds all supported text files in the given directory.

    :param root_directory: The root directory to search.
    :return: A list of file paths.
    """
    text_file_paths = []

    for current_directory, _, file_names in os.walk(root_directory):
        for file_name in file_names:
            file_path = str(os.path.join(current_directory, file_name))

            if is_supported_file_extension(file_path):
                text_file_paths.append(file_path)

    return text_file_paths
