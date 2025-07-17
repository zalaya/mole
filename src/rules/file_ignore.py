import fnmatch


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