import os
from src.constants import TEXT_FILE_EXTENSIONS


def is_supported_file(file_path: str) -> bool:
    """
    Returns True if the given filepath points to a text file, False otherwise.
    :param file_path: The filepath to check.
    :return: True if the given filepath points to a text file, False otherwise.
    """
    _, extension = os.path.splitext(file_path)
    return extension.lower() in TEXT_FILE_EXTENSIONS
