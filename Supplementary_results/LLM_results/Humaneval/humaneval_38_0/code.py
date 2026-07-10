## main.py

def encode_cyclic(s: str) -> str:
    """Returns encoded string by cycling groups of three characters.

    Args:
        s (str): The input string to be encoded.

    Returns:
        str: The encoded string.
    """
    encoded = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            # Cycle the characters in the group
            encoded.append(group[2] + group[0] + group[1])
        else:
            # If the group is less than 3, keep it as is
            encoded.append(group)
    return ''.join(encoded)

def decode_cyclic(s: str) -> str:
    """Takes as input string encoded with encode_cyclic function. Returns decoded string.

    Args:
        s (str): The encoded string to be decoded.

    Returns:
        str: The decoded string.
    """
    decoded = []
    for i in range(0, len(s), 3):
        group = s[i:i+3]
        if len(group) == 3:
            # Reverse the cycling of characters in the group
            decoded.append(group[1] + group[2] + group[0])
        else:
            # If the group is less than 3, keep it as is
            decoded.append(group)
    return ''.join(decoded)
