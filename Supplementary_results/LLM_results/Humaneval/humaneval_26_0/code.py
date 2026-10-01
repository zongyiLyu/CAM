## main.py
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers possibly containing duplicates.
    
    Returns:
        List[int]: A list of integers with duplicates removed, maintaining the original order.
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1])
        []
    """
    seen = set()  # Set to track seen elements
    result = []   # List to store the result

    for number in numbers:
        if number not in seen:
            seen.add(number)  # Add number to seen set
            result.append(number)  # Append number to result list

    return result  # Return the final result list
