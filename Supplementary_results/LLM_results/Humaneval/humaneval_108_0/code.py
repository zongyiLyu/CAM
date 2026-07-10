## main.py
from typing import List

def count_nums(arr: List[int]) -> int:
    """ Count the number of integers in the array whose sum of digits is greater than zero.

    Args:
        arr (List[int]): A list of integers.

    Returns:
        int: The count of integers with a sum of digits > 0.

    Examples:
        >>> count_nums([])
        0
        >>> count_nums([-1, 11, -11])
        1
        >>> count_nums([1, 1, 2])
        3
    """
    def sum_of_digits(n: int) -> int:
        """ Calculate the sum of digits of an integer, considering negative signs.

        Args:
            n (int): The integer whose digits will be summed.

        Returns:
            int: The sum of the digits of the integer.
        """
        return sum(int(digit) for digit in str(abs(n)))

    count = 0
    for number in arr:
        if sum_of_digits(number) > 0:
            count += 1

    return count
