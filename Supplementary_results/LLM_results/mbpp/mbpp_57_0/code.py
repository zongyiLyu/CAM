## main.py

from typing import Dict, Tuple

def eulerian_num(n: int, m: int, memo: Dict[Tuple[int, int], int] = None) -> int:
    """Calculate the Eulerian number A(n, m).

    Parameters:
    n (int): The number of elements.
    m (int): The number of permutations with exactly m ascents.

    Returns:
    int: The Eulerian number A(n, m).

    Raises:
    ValueError: If n or m is negative or if m is greater than n.
    """
    if memo is None:
        memo = {}

    # Validate inputs
    if n < 0 or m < 0 or m > n:
        raise ValueError("Invalid input: n and m must be non-negative and m must not exceed n.")

    # Base cases
    if m == 0 and n > 0:
        return 1 if n == 1 else 0
    if m == n:
        return 0
    if n == 0:
        return 0

    # Check if the result is already computed
    if (n, m) in memo:
        return memo[(n, m)]

    # Recursive calculation with memoization
    result = (n - m) * eulerian_num(n - 1, m - 1, memo) + (m + 1) * eulerian_num(n - 1, m, memo)
    
    # Store the result in the memo dictionary
    memo[(n, m)] = result
    return result
