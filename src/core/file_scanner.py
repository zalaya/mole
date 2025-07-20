import os

from typing import List
from src.configuration.constants import IGNORE_FILE_NAME
from src.core.filters.file_extension_filter import FileExtensionFilter
from src.core.filters.ignore_pattern_filter import IgnorePatternFilter
from src.core.filters.hidden_file_filter import HiddenFileFilter


def find_file_paths(root_directory: str, ignore_file: str = IGNORE_FILE_NAME) -> List[str]:
    """
    Recursively traverse a directory and return all file paths that match the configured filters.

    :param root_directory: Root directory to start the search.
    :param ignore_file: Path to the ignore-patterns file (e.g., .moleignore).
    :return: List of file paths that pass all filters.
    """
    file_filters = _initialize_file_filters(ignore_file)
    file_paths: List[str] = []

    for current_directory, subdirectories, filenames in os.walk(root_directory):
        _exclude_hidden_directories(current_directory, subdirectories)

        for filename in filenames:
            file_path = str(os.path.join(current_directory, filename))

            if _passes_all_filters(file_path, file_filters):
                file_paths.append(file_path)

    return file_paths


def _initialize_file_filters(ignore_file: str) -> List:
    """
    Instantiate and return the ordered list of file filters.

    :param ignore_file: Path to the ignore-patterns file.
    :return: List of file filter instances.
    """
    return [
        FileExtensionFilter(),
        IgnorePatternFilter(ignore_file),
        HiddenFileFilter(),
    ]


def _exclude_hidden_directories(current_directory: str, subdirectories: List[str]) -> None:
    """
    Remove hidden directories (those starting with a dot) from the os.walk traversal.

    :param current_directory: The directory being walked.
    :param subdirectories: List of subdirectory names (modified in-place).
    """
    hidden_filter = HiddenFileFilter()
    visible_subdirectories: List[str] = []

    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(current_directory, subdirectory)
        
        if hidden_filter.filter(subdirectory_path):
            visible_subdirectories.append(subdirectory)

    subdirectories[:] = visible_subdirectories


def _passes_all_filters(file_path: str, filters: List) -> bool:
    """
    Check if the given file_path is accepted by every filter in the list.

    :param file_path: Full path to the file being evaluated.
    :param filters: List of file filter instances.
    :return: True if the file passes every filter; False otherwise.
    """
    for file_filter in filters:
        if not file_filter.filter(file_path):
            return False
        
    return True
