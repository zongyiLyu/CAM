## main.py

def string_to_list(input_string: str) -> list[str]:
    """
    Converts a string into a list of substrings split by spaces.

    Parameters:
    input_string (str): The string to be converted.

    Returns:
    list[str]: A list of substrings. If the input string is empty, returns an empty list.
    """
    return input_string.split() if input_string else []

# Example usage
if __name__ == "__main__":
    print(string_to_list("python programming"))  # Returns ['python', 'programming']
    print(string_to_list("   leading and trailing spaces   "))  # Returns ['leading', 'and', 'trailing', 'spaces']
    print(string_to_list(""))  # Returns []
    print(string_to_list("multiple   spaces"))  # Returns ['multiple', 'spaces']
