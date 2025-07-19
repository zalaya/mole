import pytest

from pathlib import Path
from src.configuration.constants import ALLOWED_FILE_EXTENSIONS
from src.core.file_scanner import is_supported_file_extension, find_file_paths


@pytest.mark.parametrize("extension", list(ALLOWED_FILE_EXTENSIONS))
def test_given_supported_extension_when_checked_then_returns_true(extension):
    # Given
    file_path = f"some/path/file{extension}"

    # When
    result = is_supported_file_extension(file_path)

    # Then
    assert result is True


@pytest.mark.parametrize("extension", [".png", ".jpg", ".exe"])
def test_given_unsupported_extension_when_checked_then_returns_false(extension):
    # Given
    file_path = f"some/path/file{extension}"

    # When
    result = is_supported_file_extension(file_path)

    # Then
    assert result is False


def test_given_directory_with_supported_files_when_find_file_paths_then_returns_them(tmp_path):
    # Given
    created_files = create_files(tmp_path, ["script.py", "note.txt"])

    # When
    result = find_file_paths(str(tmp_path))

    # Then
    assert created_files[0] in result
    assert created_files[1] in result
    assert len(result) == 2


def test_given_directory_with_unsupported_files_when_find_file_paths_then_ignores_them(tmp_path):
    # Given
    create_files(tmp_path, ["start.exe", "icon.png"])

    # When
    result = find_file_paths(str(tmp_path))

    # Then
    assert result == []


def test_given_mixed_directory_when_find_file_paths_then_returns_only_supported(tmp_path):
    # Given
    created_files = create_files(tmp_path, ["start.exe", "note.txt"])

    # When
    result = find_file_paths(str(tmp_path))

    # Then
    assert created_files[1] in result
    assert len(result) == 1


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
