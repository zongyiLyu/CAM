## main.py

def fix_spaces(text: str) -> str:
    """ 
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with a hyphen.
    
    Args:
        text (str): The input string to be processed.
        
    Returns:
        str: The processed string with spaces replaced according to the rules.
    
    Examples:
        fix_spaces("Example") == "Example"
        fix_spaces("Example 1") == "Example_1"
        fix_spaces(" Example 2") == "_Example_2"
        fix_spaces(" Example   3") == "_Example-3"
    """
    # Strip leading and trailing spaces
    stripped_text = text.strip()
    
    # Replace multiple spaces with a hyphen
    while '  ' in stripped_text:
        stripped_text = stripped_text.replace('  ', '-')
    
    # Replace single spaces with underscores
    processed_text = stripped_text.replace(' ', '_')
    
    return processed_text
