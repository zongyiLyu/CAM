## main.py

from typing import List, Optional

def largest_neg(numbers: List[int]) -> Optional[int]:
    """Find the largest negative number in a list.

    Parameters:
    numbers (List[int]): A list of integers.

    Returns:
    Optional[int]: The largest negative number if present, otherwise None.
    """
    # Filter out negative numbers from the list
    negative_numbers = [num for num in numbers if num < 0]
    
    # Return the largest negative number if the list is not empty, otherwise return None
    return max(negative_numbers) if negative_numbers else None
