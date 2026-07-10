## main.py

def check(num: int) -> bool:
    """
    Check if a given number is one less than twice its reverse.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the condition is met, False otherwise.
    """
    # Handle edge cases: negative numbers and single-digit inputs
    if num < 0:
        return False
    
    # Convert the number to string to reverse it
    reversed_num_str = str(num)[::-1]
    
    # Convert the reversed string back to an integer
    reversed_num = int(reversed_num_str)
    
    # Check if the original number is one less than twice the reversed number
    return num == (2 * reversed_num) - 1
