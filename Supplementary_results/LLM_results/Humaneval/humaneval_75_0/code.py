## main.py
from sympy import primerange, factorint

def is_multiply_prime(a: int) -> bool:
    """Check if the number 'a' is the product of exactly three prime numbers.

    Args:
        a (int): The number to check, must be less than 100.

    Returns:
        bool: True if 'a' is the product of three primes, False otherwise.

    Examples:
        >>> is_multiply_prime(30)
        True
        >>> is_multiply_prime(28)
        False
        >>> is_multiply_prime(1)
        False
    """
    # Check if the input number is less than 1 or greater than or equal to 100
    if a < 1 or a >= 100:
        return False

    # Generate all prime numbers less than 100
    primes = list(primerange(1, 100))

    # Factor the number 'a' into its prime factors
    prime_factors = factorint(a)

    # Count the number of unique prime factors
    unique_prime_count = len(prime_factors)

    # Check if the count of unique prime factors is exactly 3
    return unique_prime_count == 3
