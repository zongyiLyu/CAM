## main.py
from typing import List
from sympy import isprime

def sum_of_digits_of_largest_prime(lst: List[int]) -> int:
    """Returns the sum of the digits of the largest prime number in the list.

    Args:
        lst (List[int]): A list of integers.

    Returns:
        int: The sum of the digits of the largest prime number, or 0 if no prime exists.
    """
    largest_prime = None

    # Identify primes in the list
    for number in lst:
        if number > 1 and isprime(number):  # Only consider numbers greater than 1
            if largest_prime is None or number > largest_prime:
                largest_prime = number

    # If no prime was found, return 0
    if largest_prime is None:
        return 0

    # Calculate the sum of the digits of the largest prime
    return sum(int(digit) for digit in str(largest_prime))
