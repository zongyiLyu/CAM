## main.py

def merge_dictionaries_three(dict1: dict, dict2: dict, dict3: dict) -> dict:
    """
    Merges three dictionaries into a single dictionary, keeping the last value for duplicate keys.

    Parameters:
    dict1 (dict): The first dictionary to merge.
    dict2 (dict): The second dictionary to merge.
    dict3 (dict): The third dictionary to merge.

    Returns:
    dict: A new dictionary containing all unique keys from the three input dictionaries.
    """
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict
