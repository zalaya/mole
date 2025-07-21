from pathlib import Path

from src.core.io.reader import read_files
from src.core.io.writer import write_output
from src.core.scanner.scanner import find_file_paths
from src.core.aggregator import concatenate_file_contents


if __name__ == "__main__":
    root_directory = Path.cwd()
    paths = find_file_paths(root_directory)
    file_entries = read_files(paths)
    concatenated_content = concatenate_file_contents(file_entries)
    write_output(concatenated_content)
