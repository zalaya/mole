import os
import fnmatch

from src.core.filters.file_filter import FileFilter
from src.configuration.constants import IGNORE_FILE_NAME


class IgnorePatternFilter(FileFilter):

    def __init__(self, ignore_file: str = IGNORE_FILE_NAME):
        self.patterns = []

        if os.path.isfile(ignore_file):
            with open(ignore_file, "r", encoding="utf-8") as file:
                for line in file:
                    pattern = line.strip()

                    if pattern and not pattern.startswith("#"):
                        self.patterns.append(pattern)

    def _handle(self, file_path: str) -> bool:
        for pattern in self.patterns:
            if fnmatch.fnmatch(file_path, pattern):
                return False

        return True
