## main.py

def remove_Occ(s: str, char: str) -> str:
    """
    Removes the first and last occurrence of a specified character from a string.

    Parameters:
    s (str): The input string from which characters will be removed.
    char (str): The character to be removed from the string.

    Returns:
    str: The modified string with the first and last occurrences of the character removed.

    Raises:
    ValueError: If the character is not found in the string.

    Examples:
    >>> remove_Occ("hello", "l")
    'heo'
    >>> remove_Occ("hello", "x")
    ValueError: Character not found in the string.
    """
    # Check if the character is in the string
    if char not in s:
        raise ValueError("Character not found in the string.")

    # Remove the first occurrence of the character
    first_occurrence_index = s.index(char)
    s = s[:first_occurrence_index] + s[first_occurrence_index + 1:]

    # Remove the last occurrence of the character
    last_occurrence_index = s.rindex(char)
    s = s[:last_occurrence_index] + s[last_occurrence_index + 1:]

    return s
