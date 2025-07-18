from src.configuration.constants import OUTPUT_FILE_NAME


def write_file_content(content: str, output_file_name: str = OUTPUT_FILE_NAME) -> None:
    """
    Writes the given content to the specified output file.

    :param content: The content to write.
    :param output_file_name: The name of the output file.
    """
    try:
        with open(output_file_name, "w", encoding="utf-8") as file:
            file.write(content)
    except Exception as exception:
        print(f"Error writing to file {output_file_name}: {exception}")
