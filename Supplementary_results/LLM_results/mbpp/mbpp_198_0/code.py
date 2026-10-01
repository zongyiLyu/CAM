from typing import List
import heapq

def k_smallest_pairs(arr1: List[int], arr2: List[int], k: int) -> List[List[int]]:
    """Find the k smallest pairs from two arrays based on their sums.

    Args:
        arr1 (List[int]): First array of integers.
        arr2 (List[int]): Second array of integers.
        k (int): Number of smallest pairs to return.

    Returns:
        List[List[int]]: A list of k smallest pairs, where each pair is a list of two integers from arr1 and arr2.
                          Returns an empty list if either array is empty or if k is less than 1.
    """
    # Handle edge cases
    if not arr1 or not arr2 or k < 1:
        return []

    # Create a min-heap to store the pairs and their sums
    min_heap = []
    
    # Generate all possible pairs and their sums
    for num1 in arr1:
        for num2 in arr2:
            pair_sum = num1 + num2
            # Push the pair along with its sum into the heap
            heapq.heappush(min_heap, (pair_sum, [num1, num2]))
    
    # Extract the k smallest pairs from the heap
    result = []
    for _ in range(min(k, len(min_heap))):
        result.append(heapq.heappop(min_heap)[1])
    
    return result
