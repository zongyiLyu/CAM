## main.py
from datetime import datetime

def change_date_format(date_str: str) -> str:
    """
    Converts a date from 'yyyy-mm-dd' format to 'dd-mm-yyyy' format.

    Parameters:
    date_str (str): A date string in 'yyyy-mm-dd' format.

    Returns:
    str: A date string in 'dd-mm-yyyy' format.

    Raises:
    ValueError: If the input date_str is not in the correct format or is an invalid date.
    """
    # Validate input format
    try:
        # Parse the date string into a datetime object
        date_object = datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Input date_str must be in 'yyyy-mm-dd' format and a valid date.") from e

    # Rearrange components to 'dd-mm-yyyy'
    formatted_date = date_object.strftime('%d-%m-%Y')
    
    return formatted_date
