import pytest

from src.core.content_handler import concatenate_file_contents


@pytest.fixture
def files(tmp_path):
    file_paths = [
        tmp_path / "file_1.txt",
        tmp_path / "file_2.txt",
        tmp_path / "file_3.txt"
    ]

    file_contents = {
        file_paths[0]: "Content of file 1",
        file_paths[1]: "Content of file 2",
        file_paths[2]: ""
    }

    for file_path, content in file_contents.items():
        file_path.write_text(content, encoding="utf-8")

    return tmp_path, file_paths, file_contents


def test_concatenate_file_contents(files):
    # Given
    tmp_path, file_paths, file_contents = files

    expected_content = (
        "File: file_1.txt\n\nContent of file 1\n\n"
        "File: file_2.txt\n\nContent of file 2\n\n"
        "File: file_3.txt\n\n"
    )

    # When
    concatenated_content = concatenate_file_contents(file_paths)

    normalized_expected = "\n".join(line.strip() for line in expected_content.splitlines() if line.strip())
    normalized_actual = "\n".join(line.strip() for line in concatenated_content.splitlines() if line.strip())

    # Then
    assert normalized_actual == normalized_expected
