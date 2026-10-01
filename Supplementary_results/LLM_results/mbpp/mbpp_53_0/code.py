## main.py

def decimal_to_binary(decimal_number: int) -> str:
    """Convert a decimal integer to its binary representation.

    Args:
        decimal_number (int): The decimal integer to convert.

    Returns:
        str: The binary representation of the decimal integer as a string.

    Raises:
        ValueError: If the input is a negative integer.
    
    Examples:
        >>> decimal_to_binary(8)
        '1000'
        >>> decimal_to_binary(0)
        '0'
        >>> decimal_to_binary(-5)
        ValueError('Negative numbers are not supported')
    """
    if decimal_number < 0:
        raise ValueError('Negative numbers are not supported')
    elif decimal_number == 0:
        return '0'
    else:
        binary_string = ''
        while decimal_number > 0:
            binary_string = str(decimal_number % 2) + binary_string
            decimal_number //= 2
        return binary_string
