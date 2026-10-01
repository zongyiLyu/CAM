## main.py

def iscube(a: int) -> bool:
    '''
    Check if the integer a is a perfect cube.
    
    Parameters:
    a (int): The integer to check.
    
    Returns:
    bool: True if a is a perfect cube, False otherwise.
    
    Examples:
    >>> iscube(1)
    True
    >>> iscube(2)
    False
    >>> iscube(-1)
    True
    >>> iscube(64)
    True
    >>> iscube(0)
    True
    >>> iscube(180)
    False
    '''
    cube_root = round(a ** (1/3))
    return cube_root ** 3 == a
