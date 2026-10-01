## main.py
import heapq

def larg_nnum(lst: list[int], n: int) -> list[int]:
    """
    Returns the n largest unique items from the input list.

    Parameters:
    lst (list[int]): A list of integers from which to find the largest items.
    n (int): The number of largest unique items to return.

    Returns:
    list[int]: A list containing the n largest unique integers from the input list.
    If n is greater than the number of unique items, returns all unique items sorted in descending order.
    """
    # Remove duplicates by converting the list to a set
    unique_items = set(lst)
    
    # If n is greater than the number of unique items, adjust n
    n = min(n, len(unique_items))
    
    # Use heapq to find the n largest unique items
    largest_items = heapq.nlargest(n, unique_items)
    
    return largest_items
