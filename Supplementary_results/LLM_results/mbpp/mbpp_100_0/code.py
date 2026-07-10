## main.py

def sum_range_list(numbers: list[int], start_index: int, end_index: int) -> int:
    """
    Calculate the sum of numbers in a list within a specified range.

    Parameters:
    numbers (list[int]): A list of integers.
    start_index (int): The starting index of the range (inclusive).
    end_index (int): The ending index of the range (inclusive).

    Returns:
    int: The sum of the elements in the specified range.

    Raises:
    IndexError: If start_index or end_index is out of bounds.
    """
    # Validate indices
    if start_index < 0 or end_index >= len(numbers):
        raise IndexError("Start index or end index is out of bounds.")
    
    if start_index > end_index:
        raise ValueError("Start index cannot be greater than end index.")
    
    # Calculate the sum of the specified range
    total_sum = sum(numbers[start_index:end_index + 1])
    
    return total_sum
