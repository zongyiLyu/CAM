## main.py

def is_nested(string: str) -> bool:
    '''
    This function checks if there is a valid subsequence of square brackets in the input string
    where at least one bracket is nested.

    Parameters:
    string (str): A string containing only square brackets.

    Returns:
    bool: True if there is at least one nested bracket, False otherwise.
    '''
    # Initialize a counter to track the depth of nested brackets
    depth_counter = 0
    
    # Iterate through each character in the string
    for char in string:
        if char == '[':
            # Increment the counter for an opening bracket
            depth_counter += 1
            # Check if we have found a nested bracket
            if depth_counter > 1:
                return True
        elif char == ']':
            # Decrement the counter for a closing bracket
            depth_counter -= 1
            # If the counter goes negative, it indicates an unmatched closing bracket
            if depth_counter < 0:
                return False
    
    # If we finish iterating and the counter is not zero, it indicates unmatched opening brackets
    return False if depth_counter > 0 else False
