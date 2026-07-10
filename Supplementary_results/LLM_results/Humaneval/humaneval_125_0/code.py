## main.py
from typing import List, Union

def split_words(txt: str) -> Union[List[str], int]:
    '''
    Given a string of words, return a list of words split on whitespace. 
    If no whitespaces exist in the text, split on commas ','. 
    If neither is present, return the number of lower-case letters with odd order in the alphabet, 
    ord('a') = 0, ord('b') = 1, ... ord('z') = 25.

    Args:
        txt (str): A string containing words and possibly punctuation.

    Returns:
        List[str]: A list of words if found, otherwise int representing the count of lower-case letters with odd order.
    '''
    # Check for whitespace and split the string
    if ' ' in txt:
        return txt.split()
    
    # Check for commas and split the string
    elif ',' in txt:
        return txt.split(',')
    
    # If no whitespace or commas, count lowercase letters with odd positions
    else:
        odd_position_count = sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 1)
        return odd_position_count
