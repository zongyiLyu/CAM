## main.py
import re

def text_lowercase_underscore(input_string: str) -> str:
    """
    Checks if the input string contains sequences of lowercase letters joined with underscores.
    
    Parameters:
    input_string (str): The string to be checked.
    
    Returns:
    str: 'Found a match!' if the pattern is found, otherwise 'No match found.'
    """
    # Define the regex pattern to match sequences of lowercase letters separated by underscores
    pattern = r'^[a-z]+(_[a-z]+)*$'
    
    # Use re.match to check if the input_string matches the pattern
    if re.match(pattern, input_string):
        return 'Found a match!'
    else:
        return 'No match found.'
