## main.py

from typing import List

def sum_of_digits(numbers: List[int]) -> int:
    """Calculate the sum of all digits in a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        int: The sum of all digits in the list.

    Raises:
        ValueError: If the input is not a list or contains non-integer values.
    
    Example:
        >>> sum_of_digits([10, 2, 56])
        14
    """
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise ValueError("Input must be a list of integers")
    
    total_sum = 0
    
    for number in numbers:
        # Check if each item in the list is an integer
        if not isinstance(number, int):
            raise ValueError("All items in the list must be integers")
        
        # Convert the number to string to iterate through each digit
        for digit in str(number):
            total_sum += int(digit)  # Convert each character back to integer and add to total_sum
    
    return total_sum
