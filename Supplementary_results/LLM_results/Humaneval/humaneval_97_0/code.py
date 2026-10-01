## main.py

def multiply(a: int, b: int) -> int:
    """Calculate the product of the unit digits of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of the unit digits of 'a' and 'b'.
    """
    # Extract the unit digits using the modulus operator
    unit_digit_a = abs(a) % 10
    unit_digit_b = abs(b) % 10
    
    # Calculate the product of the unit digits
    product = unit_digit_a * unit_digit_b
    
    return product
