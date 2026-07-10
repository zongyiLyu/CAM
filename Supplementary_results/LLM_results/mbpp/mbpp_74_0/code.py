## main.py

def sum_common_divisors(a: int, b: int) -> int:
    """
    Calculate the sum of common divisors of two integers.

    Parameters:
    a (int): The first integer.
    b (int): The second integer.

    Returns:
    int: The sum of common divisors of a and b. Returns 0 if either number is zero or negative.
    """
    # Check for edge cases where a or b is less than or equal to zero
    if a <= 0 or b <= 0:
        return 0

    # Function to find the common divisors
    def common_divisors(x: int, y: int) -> list:
        """
        Find all common divisors of two integers.

        Parameters:
        x (int): The first integer.
        y (int): The second integer.

        Returns:
        list: A list of common divisors of x and y.
        """
        divisors = []
        # Find the minimum of x and y to limit the range of divisor checking
        limit = min(x, y)
        for i in range(1, limit + 1):
            if x % i == 0 and y % i == 0:
                divisors.append(i)
        return divisors

    # Calculate the sum of common divisors
    common_divs = common_divisors(a, b)
    return sum(common_divs)
