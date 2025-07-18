import pytest

from src.core.file_reader import read_file_content


def test_given_existing_file_when_read_file_content_then_returns_expected_content(tmp_path):
    # Given
    file_path = tmp_path / "file.txt"
    expected_content = "This is the expected content."
    file_path.write_text(expected_content, encoding = "utf-8")

    # When
    result = read_file_content(str(file_path))

    # Then
    assert result == expected_content


def test_given_existing_empty_file_when_read_file_content_then_returns_expected_content(tmp_path):
    # Given
    file_path = tmp_path / "file.txt"
    file_path.write_text("", encoding="utf-8")

    # When
    result = read_file_content(str(file_path))

    # Then
    assert result == ""


def test_given_non_existent_file_when_read_file_content_then_raises_oserror(tmp_path):
    # Given
    file_path = tmp_path / "file.txt"

    # When / Then
    with pytest.raises(OSError):
        read_file_content(str(file_path))
