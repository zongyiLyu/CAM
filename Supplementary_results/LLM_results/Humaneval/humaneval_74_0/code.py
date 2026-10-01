## main.py

def total_match(lst1: list[str], lst2: list[str]) -> list[str]:
    '''
    This function accepts two lists of strings and returns the list that has 
    a total number of characters in all strings of the list less than the other list.

    If the two lists have the same number of characters, it returns the first list.

    Parameters:
    lst1 (list[str]): The first list of strings.
    lst2 (list[str]): The second list of strings.

    Returns:
    list[str]: The list with fewer total characters, or the first list if they are equal.
    '''
    # Calculate total characters in the first list
    total_chars_lst1 = sum(len(s) for s in lst1)
    
    # Calculate total characters in the second list
    total_chars_lst2 = sum(len(s) for s in lst2)
    
    # Compare total character counts and return the appropriate list
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    else:
        return lst2
