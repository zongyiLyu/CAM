## main.py

def remove_odd(input_string: str) -> str:
    """
    Removes characters at odd indices from the input string.

    Parameters:
    input_string (str): The string from which to remove odd indexed characters.

    Returns:
    str: A new string containing only the characters at even indices.

    Examples:
    >>> remove_odd("python")
    'pto'
    >>> remove_odd("")
    ''
    >>> remove_odd("123456789")
    '13579'
    """
    # Using string slicing to get characters at even indices
    return input_string[::2]

# The following lines are for testing the function
if __name__ == "__main__":
    print(remove_odd("python"))      # Expected output: 'pto'
    print(remove_odd(""))              # Expected output: ''
    print(remove_odd("123456789"))    # Expected output: '13579'
