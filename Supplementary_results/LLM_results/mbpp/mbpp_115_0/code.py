## main.py
from typing import List, Tuple, Dict

def check_occurences(tuples_list: List[Tuple[int, int]]) -> Dict[Tuple[int, int], int]:
    """Counts occurrences of unique tuples in a list.

    Args:
        tuples_list (List[Tuple[int, int]]): A list of tuples, where each tuple contains two integers.

    Returns:
        Dict[Tuple[int, int], int]: A dictionary where keys are unique tuples and values are their respective counts in the input list.
    """
    # Initialize an empty dictionary to store counts
    occurrences = {}

    # Iterate over each tuple in tuples_list
    for tup in tuples_list:
        # Check if tuple exists in dictionary
        if tup in occurrences:
            # Increment count for the tuple
            occurrences[tup] += 1
        else:
            # Add tuple to dictionary with count 1
            occurrences[tup] = 1

    # Return dictionary with counts
    return occurrences
