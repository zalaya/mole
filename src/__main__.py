import os

from src.core.content_writer import concatenate_file_contents
from src.core.file_scanner import find_file_paths


if __name__ == "__main__":
    base_directory = os.getcwd()
    text_file_paths = find_file_paths(base_directory)
    concatenate_file_contents(text_file_paths)
