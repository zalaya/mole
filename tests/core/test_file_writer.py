import pytest
import os

from src.core.file_writer import write_file_content


def test_given_valid_content_and_filename_when_write_file_content_then_file_is_written(tmp_path):
    # Given
    output_path = tmp_path / "output.txt"
    content = "This is test content"

    # When
    write_file_content(content, str(output_path))

    # Then
    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == content


def test_given_empty_content_when_write_file_content_then_creates_empty_file(tmp_path):
    # Given
    output_path = tmp_path / "empty.txt"
    content = ""

    # When
    write_file_content(content, str(output_path))

    # Then
    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == ""


def test_given_non_existent_directory_when_write_file_content_then_prints_error(tmp_path, capsys):
    # Given
    invalid_path = tmp_path / "nonexistent_dir" / "output.txt"
    content = "Test content"

    # When
    write_file_content(content, str(invalid_path))

    # Then
    captured = capsys.readouterr()
    assert f"Error writing to file {invalid_path}" in captured.out
    assert not invalid_path.exists()


def test_given_write_raises_exception_when_write_file_content_then_error_is_handled(
    monkeypatch, capsys
):
    # Given
    def mock_open(*args, **kwargs):
        raise IOError("Simulated error")

    monkeypatch.setattr("builtins.open", mock_open)
    output_file = "fake_output.txt"
    content = "Anything"

    # When
    write_file_content(content, output_file)

    # Then
    captured = capsys.readouterr()
    assert f"Error writing to file {output_file}: Simulated error" in captured.out
