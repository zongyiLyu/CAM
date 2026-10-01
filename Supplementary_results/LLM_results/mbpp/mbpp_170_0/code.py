## main.py

def dict_depth(d: dict) -> int:
    """
    Calculate the maximum depth of a nested dictionary.

    Parameters:
    d (dict): The input dictionary to evaluate.

    Returns:
    int: The maximum depth of the dictionary. Returns 0 for empty dictionaries.
    """
    # Check if the input dictionary is empty
    if not d:
        return 0

    # Initialize the maximum depth
    max_depth = 1

    # Iterate over each value in the dictionary
    for value in d.values():
        # If the value is a dictionary, recursively calculate its depth
        if isinstance(value, dict):
            current_depth = dict_depth(value) + 1
            # Update max_depth if the current depth is greater
            max_depth = max(max_depth, current_depth)

    return max_depth
