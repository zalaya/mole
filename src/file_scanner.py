import os
from src.rules.file_ignore import should_ignore_file
from src.io.file_support import is_supported_file

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