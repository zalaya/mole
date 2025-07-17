from src.constants import DEFAULT_OUTPUT_FILENAME
from src.io.file_reader import read_file_content


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