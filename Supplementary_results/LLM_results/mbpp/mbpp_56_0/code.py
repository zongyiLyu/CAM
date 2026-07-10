## main.py

def snake_to_camel(snake_str: str) -> str:
    """
    Convert a snake case string to camel case.

    Parameters:
    snake_str (str): The input string in snake case format.

    Returns:
    str: The converted string in camel case format.

    Examples:
    >>> snake_to_camel('python_program')
    'PythonProgram'
    >>> snake_to_camel('')
    ''
    >>> snake_to_camel('singleword')
    'Singleword'
    """
    # Handle the case of an empty string
    if not snake_str:
        return ''

    # Split the string by underscores
    words = snake_str.split('_')

    # Capitalize the first letter of each word and join them
    camel_case_str = ''.join(word.capitalize() for word in words)

    return camel_case_str
