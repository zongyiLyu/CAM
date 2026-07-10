## main.py

def truncate_number(number: float) -> float:
    """ 
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    
    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.

    Examples:
        >>> truncate_number(3.5)
        0.5
        >>> truncate_number(2.75)
        0.75
        >>> truncate_number(5.0)
        0.0
    """
    if number < 0:
        raise ValueError("The number must be a positive floating point number.")
    
    integer_part = int(number)  # Get the integer part
    decimal_part = number - integer_part  # Calculate the decimal part
    return decimal_part
