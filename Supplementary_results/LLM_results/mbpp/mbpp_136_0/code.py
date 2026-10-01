## main.py

def split_two_parts(lst: list, L: int) -> tuple:
    """Splits a list into two parts based on the specified length.

    Args:
        lst (list): A list of elements to be split.
        L (int): An integer representing the length of the first part.

    Returns:
        tuple: A tuple containing two lists. The first list contains the first L elements,
               and the second list contains the remaining elements. If L exceeds the length
               of the list, returns a message indicating the error.
    """
    if L < 0:
        return 'L cannot be negative'
    if L > len(lst):
        return 'L exceeds list length'
    
    first_part = lst[:L]
    second_part = lst[L:]
    
    return first_part, second_part
