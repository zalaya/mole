from pathlib import Path
from typing import List, Tuple


def concatenate_file_contents(file_entries: List[Tuple[Path, str]]) -> str:
    segments: List[str] = []

    for path, content in file_entries:
        segments.append(f"File: {path.name}\n\n")
        content = content.rstrip()

        if content:
            segments.append(f"{content}\n\n")
        else:
            segments.append(content)

    return "".join(segments)
