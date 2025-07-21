from pathlib import Path
from typing import List, Callable

from src.configuration.constants import ALLOWED_FILE_EXTENSIONS, IGNORE_FILE_NAME


def find_file_paths(root_directory: Path, ignore_file_path: Path = IGNORE_FILE_NAME) -> List[Path]:
    results: List[Path] = []
    patterns = _load_ignore_patterns(ignore_file_path)
    predicates = _build_predicates(patterns)

    for entry in root_directory.rglob("*"):
        is_valid = True

        for predicate in predicates:
            if not predicate(entry):
                is_valid = False
                break

        if is_valid:
            results.append(entry)

    return results


def _build_predicates(patterns: List[str]) -> List[Callable[[Path], bool]]:
    return [
        Path.is_file,
        lambda path: not _is_hidden(path),
        _has_allowed_extension,
        lambda path: not _should_ignore(path, patterns),
    ]


def _is_hidden(path: Path) -> bool:
    for part in path.parts:
        if part.startswith("."):
            return True

    return False


def _has_allowed_extension(path: Path) -> bool:
    return path.suffix.lower() in ALLOWED_FILE_EXTENSIONS


def _load_ignore_patterns(ignore_file_path: Path) -> List[str]:
    patterns: List[str] = []

    if not ignore_file_path.is_file():
        return patterns

    for line in ignore_file_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()

        if not stripped or stripped.startswith("#"):
            continue

        patterns.append(stripped)

    return patterns


def _should_ignore(path: Path, patterns: List[str]) -> bool:
    for pattern in patterns:
        if path.match(pattern) or path.match(f"**/{pattern}"):
            return True

    return False
