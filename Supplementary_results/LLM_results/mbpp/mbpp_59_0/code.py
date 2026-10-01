## main.py

def count(input_list: list) -> int:
    """
    Counts the number of True boolean values in the given list.

    Parameters:
    input_list (list): A list containing boolean values.

    Returns:
    int: The count of True values in the list.

    Raises:
    ValueError: If the input is not a list.
    """
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list.")

    true_count = 0
    for item in input_list:
        if isinstance(item, bool):
            if item:
                true_count += 1
        else:
            raise ValueError("All elements in the list must be boolean values.")

    return true_count
