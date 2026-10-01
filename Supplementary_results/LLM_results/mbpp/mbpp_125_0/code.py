## main.py

from typing import List, Any

def intersection_array(array1: List[Any], array2: List[Any]) -> List[Any]:
    """Finds the intersection of two arrays.

    Args:
        array1 (List[Any]): The first list of elements.
        array2 (List[Any]): The second list of elements.

    Returns:
        List[Any]: A list containing the common elements found in both input arrays.
    """
    # Convert both lists to sets to find the intersection
    set1 = set(array1)
    set2 = set(array2)
    
    # Find the intersection of both sets
    intersection = set1.intersection(set2)
    
    # Convert the result back to a list and return
    return list(intersection)

# Example usage (uncomment to test):
# print(intersection_array([1, 2, 3, 5, 7, 8, 9, 10], [1, 2, 4, 8, 9]))  # Returns [1, 2, 8, 9]
# print(intersection_array([], [1, 2, 4]))  # Returns []
# print(intersection_array([1, 2, 2, 3], [2, 2, 4]))  # Returns [2]
