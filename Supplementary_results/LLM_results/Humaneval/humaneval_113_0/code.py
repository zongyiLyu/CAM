## main.py
from typing import List

def odd_count(lst: List[str]) -> List[str]:
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    :param lst: List of strings containing only digits.
    :return: List of formatted strings indicating the count of odd digits.
    """
    output = []
    
    for index, string in enumerate(lst):
        # Count odd digits in the current string
        odd_count = sum(1 for char in string if char.isdigit() and int(char) % 2 != 0)
        
        # Format the output string
        output_string = f"the number of odd elements {odd_count} in the str{index}ng {index} of the {index}nput."
        output.append(output_string)
    
    return output
