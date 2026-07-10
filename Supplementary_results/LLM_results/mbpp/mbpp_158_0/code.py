## main.py
from typing import List

def max_sub_array_sum_repeated(arr: List[int], k: int, n: int) -> int:
    """ 
    Calculate the maximum subarray sum in an array that is repeated k times.

    Parameters:
    arr (List[int]): The input array of integers.
    k (int): The number of times to repeat the array.
    n (int): The length of the original array.

    Returns:
    int: The maximum sum of a contiguous subarray in the repeated array.
    """
    if n == 0 or k == 0:
        return 0

    # Calculate the maximum subarray sum using Kadane's algorithm
    def kadane(array: List[int]) -> int:
        max_ending_here = max_so_far = array[0]
        for x in array[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Calculate the total sum of the original array
    total_sum = sum(arr)
    
    # Calculate the maximum subarray sum for the original array
    max_subarray_sum = kadane(arr)

    # If k is 1, return the maximum subarray sum of the original array
    if k == 1:
        return max_subarray_sum

    # Calculate the maximum subarray sum for the array repeated twice
    max_subarray_sum_twice = kadane(arr + arr)

    # If the total sum is positive, we can add it to the maximum subarray sum
    if total_sum > 0:
        return max(max_subarray_sum, max_subarray_sum_twice, max_subarray_sum + (k - 2) * total_sum)
    else:
        return max(max_subarray_sum, max_subarray_sum_twice)

# Example usage (uncomment to test):
# result = max_sub_array_sum_repeated([1, -2, 1], 3, 3)
# print(result)  # Expected output: 3
