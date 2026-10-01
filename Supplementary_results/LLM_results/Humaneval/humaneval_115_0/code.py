## main.py
from typing import List

def max_fill(grid: List[List[int]], capacity: int) -> int:
    """ 
    Calculate the number of times buckets need to be lowered to empty the wells in the grid.
    
    Parameters:
    grid (List[List[int]]): A 2D list representing the grid of wells where 1 represents a unit of water.
    capacity (int): The capacity of each bucket.
    
    Returns:
    int: The total number of times buckets need to be lowered.
    """
    total_water = 0
    
    # Iterate through each row in the grid
    for row in grid:
        # Count 1s in each row and add to total_water
        total_water += sum(row)
    
    # Calculate times_lowered
    times_lowered = total_water // capacity
    
    return times_lowered
