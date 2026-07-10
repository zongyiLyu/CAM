## main.py

from typing import List, Tuple

def max_length(lists: List[List]) -> Tuple[int, List]:
    """Find the index and the longest sublist in a list of lists.

    Parameters:
    lists (List[List]): A list containing sublists.

    Returns:
    Tuple[int, List]: A tuple containing the index of the longest sublist and the longest sublist itself.
    """
    max_index: int = -1
    max_length: int = 0
    longest_sublist: List = []

    for index, sublist in enumerate(lists):
        current_length: int = len(sublist)
        if current_length > max_length:
            max_length = current_length
            max_index = index
            longest_sublist = sublist

    return max_index, longest_sublist
