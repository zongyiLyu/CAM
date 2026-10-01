## main.py

def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.

    Parameters:
    n (int): A positive integer representing the number of digits.

    Returns:
    int: The count of n-digit integers that start or end with 1.
    """
    # Validate input
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    # Count of n-digit integers starting with 1
    if n == 1:
        count_starting_with_1 = 1  # Only the number 1
    else:
        count_starting_with_1 = 10 ** (n - 1)  # 1 followed by (n-1) digits (0-9)

    # Count of n-digit integers ending with 1
    count_ending_with_1 = 9 * (10 ** (n - 1))  # (1-9) followed by (n-1) digits (0-9)

    # If n > 1, we need to subtract the overlap (numbers that both start and end with 1)
    if n > 1:
        overlap_count = 1  # Only the number 11
    else:
        overlap_count = 0

    # Total count
    total_count = count_starting_with_1 + count_ending_with_1 - overlap_count

    return total_count
