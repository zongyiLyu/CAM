## main.py

from typing import List, Dict

def empty_dit(dict_list: List[Dict]) -> bool:
    """Check if all dictionaries in the provided list are empty.

    Parameters:
    dict_list (List[Dict]): A list of dictionaries to check.

    Returns:
    bool: True if all dictionaries are empty, False otherwise.
    """
    # If the list is empty, return True
    if not dict_list:
        return True
    
    # Iterate through each dictionary in the list
    for d in dict_list:
        # Check if the current item is a dictionary
        if not isinstance(d, dict):
            raise ValueError("All items in the list must be dictionaries.")
        
        # If any dictionary is not empty, return False
        if d:
            return False
    
    # If all dictionaries are empty, return True
    return True
