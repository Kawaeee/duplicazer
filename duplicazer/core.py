import re


def normalize_linefeed(input_text: str):
    """
    normalize_linefeed : normalize End Of Line sequence from Windows to generic

    Parameters
    ----------
    input_text : str
        Raw text that need to normalize

    Returns
    -------
    str
        Normalized EOL text
    """
    return re.sub(r"\r\n|\n", "\n", input_text)


def remove_duplicate(input_text: str):
    """
    remove_duplicate : remove all duplicate lines from raw text

    Parameters
    ----------
    input_text : str
        Raw text that need to remove duplicate lines

    Returns
    -------
    str
        Text that only have unique lines
    """
    input_text = normalize_linefeed(input_text)
    input_text_list = [l.strip() for l in input_text.split("\n")]
    return "\n".join(list(dict.fromkeys(input_text_list)))


def find_duplicate(input_text: str):
    """
    find_duplicate : find duplicate lines from raw text

    Parameters
    ----------
    input_text : str
        Raw text that need to find duplicate lines

    Returns
    -------
    str
        Text that only have duplicate lines
    """
    input_text = normalize_linefeed(input_text)
    input_text_list = [l.strip() for l in input_text.split("\n")]

    duplicates = []

    for index in input_text_list:
        if input_text_list.count(index) > 1:
            if index not in duplicates:
                duplicates.append(index)

    return "\n".join(duplicates)
