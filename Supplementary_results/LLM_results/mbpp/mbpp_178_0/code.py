## main.py

def set_left_most_unset_bit(n: int) -> int:
    """
    Sets the left most unset bit of the given integer.

    Parameters:
    n (int): The integer to manipulate.

    Returns:
    int: The integer with the left most unset bit set to 1.
         If all bits are set, returns -1.
    """
    # Check if the input is a negative number
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Find the position of the leftmost unset bit
    bit_position = 0
    while (1 << bit_position) <= n:
        bit_position += 1

    # Create a mask to set the leftmost unset bit
    mask = 1 << bit_position

    # If all bits are set, return -1
    if mask == 0:
        return -1

    # Return the new integer with the leftmost unset bit set
    return n | mask
