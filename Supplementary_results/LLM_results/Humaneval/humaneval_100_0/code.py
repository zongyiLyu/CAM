## main.py

from typing import List

def make_a_pile(n: int) -> List[int]:
    """ 
    Given a positive integer n, returns a list of the number of stones in each level of a pile.
    The first level has n stones. The next levels depend on whether the last level's stones are odd or even.
    
    Parameters:
    n (int): A positive integer representing the number of levels.
    
    Returns:
    List[int]: A list where each element represents the number of stones in each level.
    """
    # Initialize the list with the first level stones
    stones_per_level = [n]
    
    # Loop through levels to calculate stones
    for level in range(1, n):
        if stones_per_level[level - 1] % 2 == 0:
            # If the last level's stones are even, add the next even number
            next_stones = stones_per_level[level - 1] + 2
        else:
            # If the last level's stones are odd, add the next odd number
            next_stones = stones_per_level[level - 1] + 1
        
        stones_per_level.append(next_stones)
    
    return stones_per_level
