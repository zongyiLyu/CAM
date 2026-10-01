## main.py

from math import comb

def count_binary_seq(n: int) -> float:
    """
    Calculate the number of binary sequences of length 2n where the sum of the first n bits equals the sum of the last n bits.

    Parameters:
    n (int): The half-length of the binary sequence (length of each half is n).

    Returns:
    float: The count of valid binary sequences.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer.")
    
    # The number of valid binary sequences of length 2n
    # is given by the binomial coefficient C(2n, n) / (n + 1)
    # which is the nth Catalan number.
    return float(comb(2 * n, n) // (n + 1))
