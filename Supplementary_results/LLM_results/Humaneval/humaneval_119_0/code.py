## main.py
from typing import List

def match_parens(lst: List[str]) -> str:
    '''
    Check if two strings of parentheses can be concatenated to form a balanced string.

    Parameters:
    lst (List[str]): A list containing two strings of parentheses.

    Returns:
    str: 'Yes' if the strings can form a balanced string, 'No' otherwise.

    Examples:
    >>> match_parens(['()(', ')'])
    'Yes'
    >>> match_parens([')', ')'])
    'No'
    '''
    if len(lst) != 2:
        raise ValueError("Input list must contain exactly two strings.")

    first_string = lst[0]
    second_string = lst[1]

    # Count open and close parentheses in both strings
    open_count = first_string.count('(') + second_string.count('(')
    close_count = first_string.count(')') + second_string.count(')')

    # Check if the counts of open and close parentheses are equal
    if open_count == close_count:
        return 'Yes'
    else:
        return 'No'
