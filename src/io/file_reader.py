import os


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