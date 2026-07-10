## main.py
import typing

def max_Abs_Diff(arr: typing.Union[list, tuple], length: int) -> int:
    """Calculate the maximum absolute difference between any two elements in a given array.

    Args:
        arr (Union[list, tuple]): A list or tuple of integers or floats.
        length (int): An integer representing the expected length of the array.

    Returns:
        int: The maximum absolute difference between any two elements in the array.

    Raises:
        ValueError: If the input is not a list or tuple, or if the length does not match.
    """
    # Validate input type
    if not isinstance(arr, (list, tuple)):
        raise ValueError('Invalid input type: expected list or tuple.')

    # Check if length matches
    if len(arr) != length:
        raise ValueError(f'Expected length {length}, but got {len(arr)}.')

    # Calculate maximum absolute difference
    max_value = max(arr)
    min_value = min(arr)
    max_abs_diff = abs(max_value - min_value)

    return max_abs_diff
