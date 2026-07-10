## main.py

def circular_shift(x: int, shift: int) -> str:
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    
    Args:
        x (int): The integer whose digits are to be shifted.
        shift (int): The number of positions to shift the digits.
    
    Returns:
        str: The resulting string after circular shifting the digits.
    
    Examples:
        >>> circular_shift(12, 1)
        '21'
        >>> circular_shift(12, 2)
        '12'
        >>> circular_shift(12345, 3)
        '34512'
        >>> circular_shift(12345, 10)
        '54321'
    """
    # Convert the integer to a string to manipulate its digits
    str_x = str(x)
    length = len(str_x)

    # Handle the case where shift is greater than the number of digits
    if shift >= length:
        # Reverse the digits if shift is greater than or equal to length
        return str_x[::-1]

    # Perform the circular shift
    # Calculate the effective shift
    effective_shift = shift % length
    # Create the new shifted string
    shifted_str = str_x[-effective_shift:] + str_x[:-effective_shift]

    return shifted_str
