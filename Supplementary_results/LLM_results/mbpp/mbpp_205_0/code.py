## main.py
from typing import List, Tuple

def max_Product(arr: List[int]) -> Tuple[int, int]:
    """
    Finds the pair of integers in the array that have the highest product.

    Parameters:
    arr (List[int]): A list of integers.

    Returns:
    Tuple[int, int]: A tuple containing the pair of integers with the highest product.
    If the array has fewer than two elements, returns an empty tuple.

    Examples:
    >>> max_Product([1, 2, 3, 4, 7, 0, 8, 4])
    (7, 8)
    >>> max_Product([-10, -20, 1, 2])
    (-10, -20)
    >>> max_Product([0])
    ()
    >>> max_Product([])
    ()
    """
    # Check if the array has fewer than two elements
    if len(arr) < 2:
        return ()

    # Sort the array
    arr.sort()

    # Calculate the product of the two largest numbers
    max_product1 = arr[-1] * arr[-2]

    # Calculate the product of the two smallest numbers (to account for negative values)
    max_product2 = arr[0] * arr[1]

    # Determine which product is greater and return the corresponding pair
    if max_product1 > max_product2:
        return (arr[-2], arr[-1])
    else:
        return (arr[0], arr[1])
