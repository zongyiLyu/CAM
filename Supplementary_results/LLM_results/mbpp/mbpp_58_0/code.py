## main.py

from typing import List

def sort_sublists(input_list: List[List[str]]) -> List[List[str]]:
    """
    Sorts each sublist of strings in a given list of lists.

    Parameters:
    input_list (List[List[str]]): A list of lists containing strings.

    Returns:
    List[List[str]]: A new list where each sublist is sorted.

    Example:
    >>> sort_sublists([['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']])
    [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
    """
    # Initialize an empty list to hold the sorted sublists
    sorted_list = []
    
    # Iterate through each sublist in the input list
    for sublist in input_list:
        # Sort the current sublist and append it to the sorted_list
        sorted_list.append(sorted(sublist))
    
    return sorted_list
