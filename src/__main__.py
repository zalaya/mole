import os

from src.core.content_handler import concatenate_file_contents
from src.core.file_scanner import find_file_paths
from src.core.file_writer import write_file_content


if __name__ == "__main__":
    base_directory = os.getcwd()
    text_file_paths = find_file_paths(base_directory)
    concatenated_content = concatenate_file_contents(text_file_paths)
    write_file_content(concatenated_content)
