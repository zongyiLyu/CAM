## main.py

from typing import List

def find_Max_Num(digits: List[int], length: int) -> int:
    """Find the largest number that can be formed from a list of digits.

    Args:
        digits (List[int]): A list of integers representing the digits (e.g., [1, 2, 3]).
        length (int): An integer representing the number of digits to consider (e.g., 3).

    Returns:
        int: The largest number that can be formed (e.g., 321).

    Raises:
        ValueError: If any input is invalid, such as non-digit values or incorrect length.
    """
    # Validate input
    if not all(isinstance(digit, int) and 0 <= digit <= 9 for digit in digits):
        raise ValueError("All elements in the digits list must be integers between 0 and 9.")
    
    if length <= 0 or length > len(digits):
        raise ValueError("Length must be a positive integer and less than or equal to the number of digits provided.")

    # Sort digits in descending order
    sorted_digits = sorted(digits, reverse=True)

    # Concatenate sorted digits to form the largest number
    largest_number = int(''.join(map(str, sorted_digits)))

    return largest_number
