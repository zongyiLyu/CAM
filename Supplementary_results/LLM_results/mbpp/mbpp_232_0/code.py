## main.py

from typing import List, Tuple

def trim_tuple(tuples: List[Tuple[int]], k: int) -> List[Tuple[int]]:
    """
    Trims each tuple in the given list to only include the last k elements.

    Parameters:
    tuples (List[Tuple[int]]): A list of tuples to be trimmed.
    k (int): The number of elements to retain from the end of each tuple.

    Returns:
    List[Tuple[int]]: A new list of tuples, each trimmed to the last k elements.
    """
    trimmed_tuples = []
    
    for tup in tuples:
        if k >= len(tup):
            # If k is greater than or equal to the length of the tuple, return the entire tuple
            trimmed_tuples.append(tup)
        else:
            # Otherwise, return the last k elements of the tuple
            trimmed_tuples.append(tup[-k:])
    
    return trimmed_tuples
