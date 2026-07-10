## main.py
import re

def file_name_check(file_name: str) -> str:
    """Check if the given file name is valid based on specific criteria.

    Parameters:
    file_name (str): The name of the file to validate.

    Returns:
    str: 'Yes' if the file name is valid, 'No' otherwise.
    """
    # Define the regular expression for a valid file name
    # Criteria: 
    # 1. Must start with a letter or underscore
    # 2. Can contain letters, digits, underscores, and dots
    # 3. Cannot end with a dot
    # 4. Cannot have more than 3 consecutive digits
    pattern = r'^[A-Za-z_][A-Za-z0-9_.]*[^.]$'
    
    # Check for the pattern match
    if not re.match(pattern, file_name):
        return 'No'
    
    # Check for more than 3 consecutive digits
    if re.search(r'\d{4,}', file_name):
        return 'No'
    
    return 'Yes'
