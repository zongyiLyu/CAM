## main.py
from collections import Counter
from typing import List, Tuple

def count_Occurrence(tup: Tuple, lst: List) -> int:
    """
    Count the occurrences of elements in a list within a tuple.

    Parameters:
    tup (tuple): A tuple containing elements to be counted.
    lst (list): A list of elements to count in the tuple.

    Returns:
    int: The total count of occurrences of the list elements in the tuple.
    """
    # Initialize Counter from collections
    counter = Counter(tup)
    
    # Count occurrences of elements in lst within tup
    total_count = sum(counter[element] for element in lst)
    
    return total_count
