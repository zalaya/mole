from pathlib import Path
from typing import List, Tuple


def read_files(file_paths: List[Path]) -> List[Tuple[Path, str]]:
    entries: List[Tuple[Path, str]] = []

    for path in file_paths:
        try:
            content = path.read_text(encoding="utf-8")
            entries.append((path, content))
        except OSError as error:
            print(f"Failed to read {path}: {error}")

    return entries
