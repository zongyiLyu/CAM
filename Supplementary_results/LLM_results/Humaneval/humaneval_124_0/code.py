## main.py

import re

def valid_date(date: str) -> bool:
    """Validates a given date string.
    
    Returns True if the date is valid, otherwise False.
    The date is valid if:
    1. The date string is not empty.
    2. The number of days is valid for the given month.
    3. The month is between 1 and 12.
    4. The date is in the format: mm-dd-yyyy
    
    Args:
        date (str): The date string to validate.
        
    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # Check if the date string is empty
    if not date:
        return False
    
    # Regular expression to match the date format mm-dd-yyyy
    date_pattern = r'^(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])-(\d{4})$'
    
    # Validate the date format
    if not re.match(date_pattern, date):
        return False
    
    # Split the date into components
    month, day, year = map(int, date.split('-'))
    
    # Check for valid days in month
    if month in [4, 6, 9, 11] and day > 30:
        return False
    if month == 2:
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    
    return True
