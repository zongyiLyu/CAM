## main.py

from typing import Tuple, Union, List

def similar_elements(list1: Union[List[int], Tuple[int]], list2: Union[List[int], Tuple[int]]) -> Tuple[int]:
    """Finds the common elements in two lists or tuples.

    Args:
        list1 (Union[List[int], Tuple[int]]): The first list or tuple of elements.
        list2 (Union[List[int], Tuple[int]]): The second list or tuple of elements.

    Returns:
        Tuple[int]: A tuple containing the elements that are present in both inputs,
                     maintaining the order from list1.
    """
    # Convert list2 to a set for efficient membership testing
    set_list2 = set(list2)
    
    # Use a list comprehension to maintain the order of elements from list1
    common_elements = tuple(element for element in list1 if element in set_list2)
    
    return common_elements
