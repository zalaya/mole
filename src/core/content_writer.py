from src.configuration.constants import OUTPUT_FILE_NAME
from src.core.file_reader import read_file_content


def concatenate_file_contents(file_paths: list[str], output_file_name: str = OUTPUT_FILE_NAME) -> None:
    """
    Concatenates the given file contents.

    :param file_paths: The list of file paths.
    :param output_file_name: The output file name.
    """
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        for file_path in file_paths:
            try:
                content = read_file_content(file_path)
                output_file.write(f"File: {file_path}\n")

                if content.strip():
                    output_file.write(f"\n{content}\n")
                else:
                    output_file.write(f"{content}\n")
            except Exception as exception:
                print(exception)
