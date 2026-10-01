## main.py

import math

def sum_div(n: int) -> int:
    """Returns the sum of all divisors of the given integer n.
    Handles negative numbers and zero gracefully by returning 0.
    
    Args:
        n (int): The integer for which to calculate the sum of divisors.
    
    Returns:
        int: The sum of all divisors of n.
    """
    if n <= 0:
        return 0
    
    total_sum = 0
    # Iterate through possible divisors up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If i is a divisor
            total_sum += i  # Add the divisor
            if i != n // i:  # Check if the corresponding divisor is different
                total_sum += n // i  # Add the corresponding divisor
    
    return total_sum
