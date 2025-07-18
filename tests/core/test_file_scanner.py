import pytest

from src.configuration.constants import ALLOWED_FILE_EXTENSIONS
from src.core.file_scanner import is_supported_file_extension, find_file_paths
from tests.utilities.file_creation import create_files


@pytest.mark.parametrize("extension", list(ALLOWED_FILE_EXTENSIONS))
def test_given_supported_extension_when_checked_then_returns_true(extension):
    # Given
    file_path = f"some/path/file{extension}"

    # When
    result = is_supported_file_extension(file_path)

    # Then
    assert result is True


@pytest.mark.parametrize("extension", [".exe", ".yaml", ".toml"])
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
    create_files(tmp_path, ["script.yaml", "note.md"])

    # When
    result = find_file_paths(str(tmp_path))

    # Then
    assert result == []


def test_given_mixed_directory_when_find_file_paths_then_returns_only_supported(tmp_path):
    # Given
    created_files = create_files(tmp_path, ["script.yaml", "note.txt"])

    # When
    result = find_file_paths(str(tmp_path))

    # Then
    assert created_files[1] in result
    assert len(result) == 1
