from pathlib import Path

from src.configuration.constants import OUTPUT_FILE_NAME


def write_output(content: str, output_file_path: Path = OUTPUT_FILE_NAME) -> None:
    try:
        output_file_path.write_text(content, encoding="utf-8")
    except OSError as error:
        print(f"Error writing to {output_file_path}: {error}")
