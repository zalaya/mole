import os
import fnmatch
from src.constants import TEXT_FILE_EXTENSIONS, DEFAULT_OUTPUT_FILENAME


def is_supported_file(file_path: str) -> bool:
    """
    Returns True if the given filepath points to a text file, False otherwise.
    :param file_path: The filepath to check.
    :return: True if the given filepath points to a text file, False otherwise.
    """
    _, extension = os.path.splitext(file_path)
    return extension.lower() in TEXT_FILE_EXTENSIONS

def should_ignore_file(file_path: str, ignore_patterns: list[str]) -> bool:
    """
    Returns True if the given filepath points to a text file, False otherwise.
    :param file_path: The filepath to check.
    :param ignore_patterns: A list of patterns to ignore.
    :return: True if the given filepath points to a text file, False otherwise.
    """
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return True

    return False


def find_file_paths(root_directory: str) -> list[str]:
    """
    Recursively finds all supported text files in the given directory.
    :param root_directory: The root directory to search.
    :return: A list of file paths.
    """
    text_file_paths = []
    ignore_patterns = []

    for current_directory, _, file_names in os.walk(root_directory):
        for file_name in file_names:
            file_path = str(os.path.join(current_directory, file_name))

            if is_supported_file(file_path) and not should_ignore_file(file_path, ignore_patterns):
                text_file_paths.append(file_path)

    return text_file_paths


def read_file_content(file_path: str) -> str:
    """
    Reads the given file content from the given path.
    :param file_path: The file path.
    :return: Content of the given file path.
    """
    with open(file_path, "r", encoding = "utf-8") as file:
        return file.read()


def read_ignore_file_patterns(file_path: str = ".moleignore") -> list[str]:
    """
    Reads the given file patterns from the given path.
    :param file_path: The file path.
    :return: A list of file patterns.
    """
    if not os.path.isfile(file_path):
        return []

    patterns = []

    with open(file_path, "r", encoding = "utf-8") as file:
        for line in file:
            stripped_line = line.strip()

            if stripped_line and not stripped_line.startswith("#"):
                patterns.append(stripped_line)

        return patterns


def concatenate_file_contents(file_paths: list[str]) -> None:
    """
    Concatenates the given file contents.
    :param file_paths: The list of file paths.
    """
    with open(DEFAULT_OUTPUT_FILENAME, "w", encoding = "utf-8") as output_file:
        for file_path in file_paths:
            try:
                content = read_file_content(file_path)
                output_file.write(content)
            except Exception as exception:
                print(exception)