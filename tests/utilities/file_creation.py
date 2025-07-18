from pathlib import Path


def create_files(base_directory: Path, file_names: list[str]) -> list[str]:
    """
    Creates files into a defined directory.

    :param base_directory: The base directory where the files will be created.
    :param file_names: The names of the files to be created.
    """
    paths = []

    for file_name in file_names:
        path = base_directory / file_name
        path.write_text("")
        paths.append(str(path))

    return paths
