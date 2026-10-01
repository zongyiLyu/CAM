## main.py

def double_the_difference(lst: list[int]) -> int:
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    Args:
        lst (list[int]): A list of integers.

    Returns:
        int: The sum of squares of odd integers in the list. Returns 0 if no such integers exist.

    Examples:
        double_the_difference([1, 3, 2, 0]) == 10
        double_the_difference([-1, -2, 0]) == 0
        double_the_difference([9, -2]) == 81
        double_the_difference([0]) == 0  
        double_the_difference([]) == 0
    '''
    # Initialize sum
    total: int = 0
    
    # Iterate through the list
    for num in lst:
        # Check if the number is an integer and odd
        if isinstance(num, int) and num >= 0 and num % 2 != 0:
            total += num ** 2
            
    return total
