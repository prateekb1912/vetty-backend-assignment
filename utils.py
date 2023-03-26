import codecs

import chardet


def read_file(filepath, start_line=None, end_line=None):
    """
    Reads the contents of a file at the given file path and returns the contents as a string.

    Args:
        filepath (str): The path to the file to read.
        start_line (int, optional): The line number to start reading from. Defaults to None, which means start from the beginning of the file.
        end_line (int, optional): The line number to stop reading at (inclusive). Defaults to None, which means read until the end of the file.

    Returns:
        str: The contents of the file as a string.
    """
    with open(filepath, 'rb') as f:
        res = chardet.detect(f.read())

    encoding = res['encoding']

    with codecs.open(filepath, 'r+', encoding=encoding) as f:
        content = f.read()

    # Split the content into lines
    lines = content.splitlines()

    if start_line is not None:
        lines = lines[start_line-1:]
    if end_line is not None:
        lines = lines[:end_line]

    return '\n'.join(lines)
