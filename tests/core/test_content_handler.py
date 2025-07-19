import pytest

from src.core.content_handler import concatenate_file_contents


@pytest.fixture
def files(tmp_path):
    contents = ["Content of file 1", "Content of file 2", ""]
    file_paths = []

    for i, content in enumerate(contents, start=1):
        file_path = tmp_path / f"file_{i}.txt"
        file_path.write_text(content, encoding="utf-8")
        file_paths.append(file_path)

    return file_paths


def test_given_existing_files_when_concatenate_file_contents_then_return_concatenated_contents(files):
    # Given
    expected_output = (
        "File: file_1.txt\n\nContent of file 1\n"
        "File: file_2.txt\n\nContent of file 2\n"
        "File: file_3.txt\n\n"
    )

    # When
    result = concatenate_file_contents(files)

    # Then
    assert result == expected_output
