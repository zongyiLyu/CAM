## main.py

def find_length(binary_string: str, length: int) -> int:
    """
    Calculate the maximum difference between the number of 0s and 1s in any substring of the given binary string.

    Parameters:
    binary_string (str): The input binary string consisting of '0's and '1's.
    length (int): The length of the binary string.

    Returns:
    int: The maximum difference between the counts of 0s and 1s in any substring.
    """
    # Edge case: if the string is empty, return 0
    if length == 0:
        return 0

    # Transform the binary string into a numerical representation
    # where '0' is treated as -1 and '1' as +1
    transformed_array = [1 if char == '1' else -1 for char in binary_string]

    # Initialize variables for prefix sum and maximum difference
    max_difference = 0
    current_sum = 0
    sum_map = {0: -1}  # To handle the case when the entire prefix is valid

    # Calculate prefix sums and determine the maximum difference
    for index in range(length):
        current_sum += transformed_array[index]

        # Check if this prefix sum has been seen before
        if current_sum in sum_map:
            # Calculate the difference
            max_difference = max(max_difference, index - sum_map[current_sum])
        else:
            # Store the first occurrence of this prefix sum
            sum_map[current_sum] = index

    return max_difference
