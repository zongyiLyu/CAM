## main.py

def encode_shift(s: str) -> str:
    """Encodes a string by shifting each alphabetic character by 5 positions forward.

    Args:
        s (str): A string containing lowercase alphabetic characters and possibly non-alphabetic characters.

    Returns:
        str: A string where each alphabetic character is shifted by 5 positions in the alphabet, 
             with non-alphabetic characters preserved.
    """
    encoded_string = []
    shift = 5

    for char in s:
        if char.isalpha() and char.islower():
            # Shift character and wrap around using modulo
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encoded_string.append(shifted_char)
        else:
            # Preserve non-alphabetic characters
            encoded_string.append(char)

    return ''.join(encoded_string)


def decode_shift(s: str) -> str:
    """Decodes a string by shifting each alphabetic character back by 5 positions.

    Args:
        s (str): A string that has been encoded using encode_shift.

    Returns:
        str: A string where each alphabetic character is shifted back by 5 positions, 
             with non-alphabetic characters preserved.
    """
    decoded_string = []
    shift = 5

    for char in s:
        if char.isalpha() and char.islower():
            # Shift character back and wrap around using modulo
            shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            decoded_string.append(shifted_char)
        else:
            # Preserve non-alphabetic characters
            decoded_string.append(char)

    return ''.join(decoded_string)
