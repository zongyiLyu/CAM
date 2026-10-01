## main.py

def even_bit_set_number(n: int) -> int:
    """
    Sets all even bits of the given integer n to 1.

    Parameters:
    n (int): The input integer whose even bits are to be set.

    Returns:
    int: The integer with all even bits set to 1.

    Examples:
    >>> even_bit_set_number(10)
    10
    >>> even_bit_set_number(0)
    0
    >>> even_bit_set_number(-1)
    -1
    """
    # Create a mask with all even bits set to 1
    mask = 0xAAAAAAAA  # This is a hexadecimal representation where even bits are set to 1

    # Use bitwise OR to set the even bits of n
    result = n | mask

    return result
