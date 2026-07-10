## main.py

def get_Char(input_string: str) -> str:
    """
    Computes the character corresponding to the sum of ASCII values of the input string modulo 26.
    
    Parameters:
    input_string (str): The input string to be processed.
    
    Returns:
    str: A single character resulting from the computation.
    """
    # Validate input
    if not isinstance(input_string, str):
        return "Error: Input must be a string"
    
    # Handle empty string case
    if len(input_string) == 0:
        return "Error: Input string cannot be empty"
    
    # Calculate the sum of ASCII values
    ascii_sum = sum(ord(char) for char in input_string)
    
    # Compute the character based on the modulo 26 of the sum
    result_char = chr((ascii_sum % 26) + ord('a'))
    
    return result_char
