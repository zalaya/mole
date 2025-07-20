from abc import ABC, abstractmethod


class FileFilter(ABC):

    @abstractmethod
    def _handle(self, file_path: str) -> bool:
        pass

    def filter(self, file_path: str) -> bool:
        return self._handle(file_path)
