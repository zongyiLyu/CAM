## main.py
from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """ 
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Parameters:
    arr (List[int]): A list of integers.
    k (int): An integer representing the number of elements to consider from the start of arr.

    Returns:
    int: The sum of the elements with at most two digits.

    Raises:
    ValueError: If k is not a positive integer or if k is greater than the length of arr.

    Example:
        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3
    """
    # Validate inputs
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        raise ValueError("arr must be a list of integers.")
    if not isinstance(k, int) or k <= 0 or k > len(arr):
        raise ValueError("k must be a positive integer and less than or equal to the length of arr.")

    # Initialize sum
    total_sum = 0

    # Iterate through the first k elements of arr
    for i in range(k):
        if abs(arr[i]) < 100:  # Check if the element has at most two digits
            total_sum += arr[i]

    return total_sum
