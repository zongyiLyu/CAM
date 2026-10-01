## main.py
from itertools import combinations
from typing import List

def combinations_list(elements: List) -> List[List]:
    """ 
    Generate all possible combinations of the elements in the given list.

    Parameters:
    elements (List): A list of elements to generate combinations from.

    Returns:
    List[List]: A list of lists, where each inner list represents a unique combination.
    """
    result = []
    # Generate combinations for all possible lengths from 0 to len(elements)
    for r in range(len(elements) + 1):
        # Use itertools.combinations to generate combinations of length r
        result.extend(list(combinations(elements, r)))
    
    # Convert tuples to lists for the final output
    return [list(comb) for comb in result]
