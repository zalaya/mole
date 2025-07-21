import os

from src.core.filters.file_filter import FileFilter


class HiddenFileFilter(FileFilter):

    def _handle(self, file_path: str) -> bool:
        for part in file_path.split(os.sep):
            if part.startswith("."):
                return False

        return True
