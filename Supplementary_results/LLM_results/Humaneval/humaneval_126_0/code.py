## main.py
from typing import List

def is_sorted(lst: List[int]) -> bool:
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Parameters:
    lst (List[int]): A list of non-negative integers.

    Returns:
    bool: True if the list is sorted in ascending order and has no more than one duplicate of the same number, False otherwise.

    Examples:
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    seen_numbers = set()
    previous_number = None

    for number in lst:
        # Check if the current number is less than the previous number
        if previous_number is not None and number < previous_number:
            return False
        
        # Check for duplicates
        if number in seen_numbers:
            return False
        seen_numbers.add(number)
        
        previous_number = number

    return True
