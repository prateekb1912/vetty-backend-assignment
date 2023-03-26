import codecs

import chardet


def read_file(filepath, start_line, end_line):
    """
    Reads the contents of a file at the given file path and returns the contents as a string.

    Args:
        filepath (str): The path to the file to read.
        start_line (int): The line number to start reading from. 
        end_line (int): The line number to stop reading at (inclusive).

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

    start_line = max(0, min(len(content) - 1, start_line-1))

    return ''.join(lines[start_line:end_line])
