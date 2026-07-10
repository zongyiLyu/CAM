## main.py
from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """ Sorts the given list of integers in ascending order according to the sum of their digits.
    If two integers have the same digit sum, they retain their original order.

    Args:
        nums (List[int]): A list of integers to be sorted.

    Returns:
        List[int]: A new list of integers sorted by the sum of their digits.
    """
    
    def digit_sum(n: int) -> int:
        """Calculates the sum of the digits of an integer.

        Args:
            n (int): The integer whose digits will be summed.

        Returns:
            int: The sum of the digits of the integer.
        """
        return sum(int(digit) for digit in str(abs(n)))

    # Sort the numbers based on the digit sum and maintain original order for ties
    sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), nums.index(x)))
    
    return sorted_nums
