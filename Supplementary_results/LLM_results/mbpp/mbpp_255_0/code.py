## main.py

from typing import List

def find_remainder(arr: List[int], n: int, m: int) -> int:
    """Calculate the product of an array modulo a number.

    Parameters:
    arr (List[int]): A list of integers to multiply.
    n (int): The number to take the product modulo.
    m (int): An additional parameter that is not used in the calculation but included for compatibility with the user requirement.

    Returns:
    int: The product of the array elements modulo n.

    Raises:
    ValueError: If arr is empty.
    """
    if not arr:
        raise ValueError("The input array is empty.")

    product = 1
    for element in arr:
        product *= element

    return product % n
