## main.py

def sumofFactors(n: int) -> int:
    """
    Calculate the sum of even factors of a given integer.

    Parameters:
    n (int): The integer for which to find the sum of even factors.

    Returns:
    int: The sum of even factors. Returns 0 for negative numbers and zero.
    """
    if n <= 0:
        return 0

    even_factor_sum = 0
    # Iterate through possible factors up to the square root of n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:  # Check if i is a factor
            if i % 2 == 0:  # Check if the factor is even
                even_factor_sum += i
            corresponding_factor = n // i
            if corresponding_factor != i and corresponding_factor % 2 == 0:  # Check the corresponding factor
                even_factor_sum += corresponding_factor

    return even_factor_sum
