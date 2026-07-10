## main.py

def string_xor(a: str, b: str) -> str:
    """ 
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    
    :param a: A binary string consisting of 1s and 0s.
    :param b: A binary string consisting of 1s and 0s.
    :return: A binary string representing the XOR result of a and b.
    
    >>> string_xor('010', '110')
    '100'
    >>> string_xor('1010', '110')
    '1000'
    >>> string_xor('', '110')
    '110'
    >>> string_xor('101', '')
    '101'
    >>> string_xor('', '')
    ''
    """
    # Pad the shorter string with leading zeros
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)

    # Perform XOR operation
    result = []
    for bit_a, bit_b in zip(a, b):
        result_bit = '1' if bit_a != bit_b else '0'
        result.append(result_bit)

    return ''.join(result)
