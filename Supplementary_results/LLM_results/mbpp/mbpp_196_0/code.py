## main.py

def find_Parity(num: int) -> str:
    """
    Determines the parity of a given integer.
    
    Parameters:
    num (int): The number to check for parity.
    
    Returns:
    str: 'Even Parity' if the number is even, 'Odd Parity' if the number is odd, 
         or an error message for invalid input.
    """
    if not isinstance(num, int):
        return 'Invalid input, please enter an integer.'
    
    if num % 2 == 0:
        return 'Even Parity'
    else:
        return 'Odd Parity'
