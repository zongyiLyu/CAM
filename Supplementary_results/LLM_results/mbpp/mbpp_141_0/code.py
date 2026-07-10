## main.py

def find_star_num(n: int) -> int:
    """
    Calculate the n-th star number.

    A star number is defined by the formula:
    S(n) = n(6n - 6 + 1)/2

    Parameters:
    n (int): The index of the star number to calculate. Must be a non-negative integer.

    Returns:
    int: The n-th star number.

    Raises:
    ValueError: If n is negative or not an integer.

    Examples:
    >>> find_star_num(3)
    37
    >>> find_star_num(0)
    1
    >>> find_star_num(1)
    1
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Calculate the n-th star number using the formula
    star_number = n * (6 * n - 6 + 1) // 2
    return star_number
