## main.py

from typing import Union

def median_trapezium(a: float, b: float, c: float) -> float:
    """Calculate the median length of a trapezium given three lengths.

    Args:
        a (float): The length of the first side.
        b (float): The length of the second side.
        c (float): The length of the third side.

    Returns:
        float: The median length of the three provided lengths.

    Raises:
        ValueError: If any of the lengths are not numeric or are negative.
    """
    # Validate inputs
    for length in (a, b, c):
        if not isinstance(length, (int, float)) or length < 0:
            raise ValueError("Invalid input: lengths must be non-negative numbers.")

    # Calculate the median
    lengths = [a, b, c]
    lengths.sort()
    median_length = lengths[1]  # The middle value after sorting

    return median_length
