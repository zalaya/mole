import os

from src.core.filters.file_filter import FileFilter
from src.configuration.constants import ALLOWED_FILE_EXTENSIONS


class FileExtensionFilter(FileFilter):

    def _handle(self, file_path: str) -> bool:
        _, ext = os.path.splitext(file_path)
        return ext.lower() in ALLOWED_FILE_EXTENSIONS
