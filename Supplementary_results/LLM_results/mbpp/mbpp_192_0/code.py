## main.py

def extract_freq(tuples_list: list[tuple]) -> int:
    """
    Extracts the number of unique tuples from the given list.

    Parameters:
    tuples_list (list[tuple]): A list of tuples to analyze.

    Returns:
    int: The count of unique tuples in the list.
    """
    # Create a set from the tuples_list to filter out unique tuples
    unique_tuples = set(tuples_list)
    
    # Return the count of unique tuples
    return len(unique_tuples)
