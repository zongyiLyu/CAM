## main.py

def all_Bits_Set_In_The_Given_Range(number: int, start: int, end: int) -> bool:
    """
    Check if all bits are unset in the given range.

    Parameters:
    number (int): The number to check.
    start (int): The starting bit position (0-indexed).
    end (int): The ending bit position (0-indexed).

    Returns:
    bool: True if all bits in the range are unset, False otherwise.
    """
    # Create a mask with bits set to 1 in the specified range
    mask = ((1 << (end - start + 1)) - 1) << start
    
    # Use bitwise AND to check if the bits in the range are unset
    return (number & mask) == 0
