## main.py
from typing import List
import heapq

def minPath(grid: List[List[int]], k: int) -> List[int]:
    """ 
    Given a grid with N rows and N columns (N >= 2) and a positive integer k, 
    each cell of the grid contains a value. Every integer in the range [1, N * N]
    inclusive appears exactly once on the cells of the grid.

    You have to find the minimum path of length k in the grid. You can start
    from any cell, and in each step you can move to any of the neighbor cells,
    in other words, you can go to cells which share an edge with your current
    cell.
    A path A (of length k) is considered less than a path B (of length k) if
    lst_A is lexicographically less than lst_B.
    Return an ordered list of the values on the cells that the minimum path go through.
    """
    
    # Directions for moving in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n = len(grid)
    min_path = None

    def dfs(x: int, y: int, path: List[int]) -> None:
        nonlocal min_path
        # If the path length is equal to k, check if it's the minimum path
        if len(path) == k:
            if min_path is None or path < min_path:
                min_path = path.copy()
            return
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                path.append(grid[nx][ny])
                dfs(nx, ny, path)
                path.pop()  # Backtrack

    # Start DFS from each cell in the grid
    for i in range(n):
        for j in range(n):
            dfs(i, j, [grid[i][j]])

    return min_path if min_path is not None else []
