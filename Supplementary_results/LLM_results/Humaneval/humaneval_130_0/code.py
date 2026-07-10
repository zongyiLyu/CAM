## main.py
from typing import List

def tri(n: int) -> List[int]:
    """Generate the first n + 1 numbers of the Tribonacci sequence.
    
    The sequence is defined as follows:
    - tri(0) = 1
    - tri(1) = 3
    - tri(n) = 1 + n // 2, if n is even.
    - tri(n) = tri(n - 1) + tri(n - 2) + tri(n - 3), if n is odd.
    
    Args:
        n (int): A non-negative integer.
    
    Returns:
        List[int]: A list containing the first n + 1 numbers of the Tribonacci sequence.
    
    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    # Base cases
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 3]
    
    # Initialize the sequence list
    sequence = [0] * (n + 1)
    sequence[0] = 1
    sequence[1] = 3
    
    for i in range(2, n + 1):
        if i % 2 == 0:  # Even case
            sequence[i] = 1 + i // 2
        else:  # Odd case
            sequence[i] = sequence[i - 1] + sequence[i - 2] + sequence[i - 3]
    
    return sequence
