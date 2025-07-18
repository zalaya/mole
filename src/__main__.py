import os
from src.constants import ALLOWED_FILE_EXTENSIONS, OUTPUT_FILENAME


def is_supported_file(file_path: str) -> bool:
    """
    Returns True if the given filepath points to a text file, False otherwise.
    :param file_path: The filepath to check.
    :return: True if the given filepath points to a text file, False otherwise.
    """
    _, extension = os.path.splitext(file_path)
    return extension.lower() in ALLOWED_FILE_EXTENSIONS


def read_file_content(file_path: str) -> str:
    """
    Reads the given file content from the given path.
    :param file_path: The file path.
    :return: Content of the given file path.
    """
    with open(file_path, "r", encoding = "utf-8") as file:
        return file.read()


def concatenate_file_contents(file_paths: list[str]) -> None:
    """
    Concatenates the given file contents.
    :param file_paths: The list of file paths.
    """
    with open(OUTPUT_FILENAME, "w", encoding = "utf-8") as output_file:
        for file_path in file_paths:
            try:
                content = read_file_content(file_path)
                output_file.write(content)
            except Exception as exception:
                print(exception)


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

            if is_supported_file(file_path):
                text_file_paths.append(file_path)

    return text_file_paths


if __name__ == "__main__":
    text_file_paths = find_file_paths(os.getcwd())
    concatenate_file_contents(text_file_paths)