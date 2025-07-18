def read_file_content(file_path: str) -> str:
    """
    Reads the given file content from the given path.

    :param file_path: The file path.
    :return: Content of the given file path.
    :raises: OSError if the file cannot be read.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
