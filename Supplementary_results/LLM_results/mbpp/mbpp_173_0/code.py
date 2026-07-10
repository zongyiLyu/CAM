## main.py
from typing import List

def max_sum_increasing_subseq(arr: List[int], n: int, i: int, k: int) -> int:
    """Calculate the maximum sum of increasing subsequences including the kth element.

    Args:
        arr (List[int]): A list of integers representing the sequence.
        n (int): The length of the list.
        i (int): The index up to which the increasing subsequence is considered.
        k (int): The index of the element that must be included in the sum (k > i).

    Returns:
        int: The maximum sum of the increasing subsequence including the kth element.
    """
    # Handle edge cases
    if n == 0 or i < 0 or k < 0 or k >= n or i >= n:
        return 0

    # Initialize the dp array
    dp = [0] * n

    # Base case: the maximum sum at each index is the value at that index
    for j in range(n):
        dp[j] = arr[j]

    # Build the dp array considering only elements up to index i
    for j in range(1, i + 1):
        for m in range(j):
            if arr[j] > arr[m]:
                dp[j] = max(dp[j], dp[m] + arr[j])

    # Ensure the kth element is included in the sum
    max_sum = dp[k]
    for j in range(k):
        if arr[k] > arr[j]:
            max_sum = max(max_sum, dp[j] + arr[k])

    return max_sum
