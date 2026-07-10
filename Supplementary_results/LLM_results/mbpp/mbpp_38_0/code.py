## main.py

def sequence(n: int) -> int:
    """
    Compute the nth number in the Newman Conway sequence.

    The Newman Conway sequence is defined as follows:
    - P(1) = 1
    - P(2) = 1
    - P(n) = P(P(n-1)) + P(n-1) for n > 2

    Parameters:
    n (int): The position in the sequence to compute (must be >= 1).

    Returns:
    int: The nth number in the Newman Conway sequence.

    Raises:
    ValueError: If n is less than 1.

    Examples:
    >>> sequence(1)
    1
    >>> sequence(2)
    1
    >>> sequence(10)
    6
    """
    if n < 1:
        raise ValueError("Input must be greater than or equal to 1.")

    # Initialize the sequence with the first two values
    P = [0] * (n + 1)
    P[1] = 1
    if n > 1:
        P[2] = 1

    # Compute the sequence iteratively
    for i in range(3, n + 1):
        P[i] = P[P[i - 1]] + P[i - 1]

    return P[n]
