## main.py

def is_undulating(num_str: str) -> bool:
    """
    Check if the given string representation of a number is undulating.

    An undulating number alternates between two digits. For example:
    - '1212121' is undulating (alternates between 1 and 2)
    - '123' is not undulating

    Parameters:
    num_str (str): The string representation of the number to check.

    Returns:
    bool: True if the number is undulating, False otherwise.
    """
    # Check for empty input
    if not num_str:
        raise ValueError("Input cannot be empty")

    # Check if the input is a numeric string
    if not num_str.isdigit():
        raise ValueError("Input must be a numeric string")

    # Initialize variables to track the first two digits
    first_digit = num_str[0]
    second_digit = None

    # Iterate through the string to check for undulating pattern
    for i in range(1, len(num_str)):
        current_digit = num_str[i]
        
        # Determine the second digit if not already set
        if second_digit is None and current_digit != first_digit:
            second_digit = current_digit
        
        # Check for undulating pattern
        if (i % 2 == 1 and current_digit != first_digit) or (i % 2 == 0 and current_digit != second_digit):
            continue
        else:
            return False

    return True
