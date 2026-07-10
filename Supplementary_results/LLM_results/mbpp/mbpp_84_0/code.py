## main.py

def is_Sum_Of_Powers_Of_Two(n: int) -> bool:
    """
    Check if the given number can be represented as a sum of distinct powers of 2.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if the number can be represented as a sum of distinct powers of 2, False otherwise.
    """
    # A number can be expressed as a sum of distinct powers of two if its binary representation
    # contains only one bit set to 1, which means it is a power of two.
    # We also need to ensure that the number is non-negative.
    
    if n < 0:
        return False
    
    # Check if n is a power of two by using the property that
    # a power of two has exactly one bit set in its binary representation.
    return n > 0 and (n & (n - 1)) == 0

