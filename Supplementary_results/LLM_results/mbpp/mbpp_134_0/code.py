## main.py

from sympy import isprime

def newman_prime(n: int) -> int:
    """Compute the nth Newman–Shanks–Williams prime number.

    Args:
        n (int): The position of the Newman prime to find (1-based index).

    Returns:
        int: The nth Newman–Shanks–Williams prime number.

    Raises:
        ValueError: If n is less than 1.
    """
    if n < 1:
        raise ValueError("Input must be a positive integer greater than 0.")

    # List to store found Newman primes
    newman_primes = []
    
    # Start checking natural numbers for Newman prime conditions
    candidate = 1
    while len(newman_primes) < n:
        if isprime(candidate):
            # Check if the candidate is a Newman prime
            if candidate == 2 or candidate == 3 or candidate == 5 or candidate == 7:
                newman_primes.append(candidate)
            elif candidate > 7:
                # Check if the candidate is of the form 6k ± 1
                if (candidate - 1) % 6 == 0 or (candidate + 1) % 6 == 0:
                    newman_primes.append(candidate)
        candidate += 1

    return newman_primes[-1]
