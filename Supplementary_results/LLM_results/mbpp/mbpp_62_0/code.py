## main.py

def odd_Equivalent(binary_string: str, rotations: int) -> int:
    """
    Counts the number of odd values obtained by rotating a binary string a specified number of times.

    Parameters:
    binary_string (str): A string consisting of '0's and '1's representing a binary number.
    rotations (int): The number of times to rotate the binary string.

    Returns:
    int: The count of unique odd values obtained from the rotations.
    """
    # Validate input for non-binary characters
    if not all(char in '01' for char in binary_string):
        raise ValueError("Input string must be a binary string containing only '0' and '1'.")

    # Initialize a set to store unique odd values
    odd_values = set()

    # Perform rotations
    length = len(binary_string)
    for i in range(rotations):
        # Rotate the binary string
        rotated_string = binary_string[i % length:] + binary_string[:i % length]
        
        # Convert rotated string to integer
        integer_value = int(rotated_string, 2)
        
        # Check if integer is odd
        if integer_value % 2 == 1:
            odd_values.add(integer_value)

    # Return the count of unique odd values
    return len(odd_values)
