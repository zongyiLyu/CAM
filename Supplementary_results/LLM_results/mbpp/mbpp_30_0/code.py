## main.py

def dif_Square(n: int) -> bool:
    """
    Check if the given number can be represented as the difference of two squares.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number can be expressed as the difference of two squares, False otherwise.

    Examples:
    >>> dif_Square(5)
    True
    >>> dif_Square(4)
    True
    >>> dif_Square(2)
    False
    >>> dif_Square(-1)
    False
    """
    # Check for negative numbers and zero
    if n < 0:
        return False
    # Check if n is even
    if n % 2 == 0:
        return True
    # Check if n is odd and not of the form 4k + 2
    if n % 4 != 2:
        return True
    return False
