## main.py

from typing import Dict, Tuple

def get_total_number_of_sequences(m: int, n: int) -> int:
    """Calculate the total number of valid sequences of length n.

    A valid sequence is defined as a sequence where each element is a 
    positive integer that is at least twice the previous element and 
    at most m.

    Args:
        m (int): A positive integer representing the upper limit for 
                 the sequence elements.
        n (int): A positive integer representing the length of the 
                 sequence.

    Returns:
        int: The number of valid sequences of length n.
    """
    # Validate inputs
    if m <= 0 or n <= 0:
        raise ValueError("Both m and n must be positive integers.")

    # Memoization dictionary to store results of subproblems
    memo: Dict[Tuple[int, int], int] = {}

    def count_sequences(last_element: int, remaining_length: int) -> int:
        """Recursive helper function to count valid sequences.

        Args:
            last_element (int): The last element in the current sequence.
            remaining_length (int): The remaining length of the sequence to fill.

        Returns:
            int: The count of valid sequences from this state.
        """
        # Base case: if no more elements to add, return 1
        if remaining_length == 0:
            return 1
        
        # Check if the result is already computed
        if (last_element, remaining_length) in memo:
            return memo[(last_element, remaining_length)]

        total_count = 0
        # Start the next element from at least double the last element
        next_element = last_element * 2
        
        # Count valid sequences for all valid next elements
        while next_element <= m:
            total_count += count_sequences(next_element, remaining_length - 1)
            next_element += 1  # Increment to check the next possible element

        # Store the computed result in the memoization dictionary
        memo[(last_element, remaining_length)] = total_count
        return total_count

    # Start counting sequences with the first element being 1
    return count_sequences(1, n)
