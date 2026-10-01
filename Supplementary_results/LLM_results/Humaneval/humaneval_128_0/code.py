## main.py
from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    """
    Calculate the sum of magnitudes of integers multiplied by the product of their signs.

    Parameters:
    arr (List[int]): A list of integers.

    Returns:
    Optional[int]: The computed value or None if the input list is empty.

    Example:
    >>> prod_signs([1, 2, 2, -4])
    -9
    >>> prod_signs([0, 1])
    0
    >>> prod_signs([])
    None
    """
    if not arr:
        return None

    total_sum = 0
    product_sign = 1

    for number in arr:
        if number > 0:
            total_sum += number
        elif number < 0:
            total_sum += -number
            product_sign *= -1
        # If number is zero, we do not change the total_sum or product_sign

    return total_sum * product_sign
