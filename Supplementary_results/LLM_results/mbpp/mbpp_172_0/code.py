## main.py
from typing import List, Tuple

def start_withp(words: List[str]) -> Tuple[str, str]:
    """Find the first two words starting with 'p' from a list of strings.

    Args:
        words (List[str]): A list of strings where each string may contain multiple words.

    Returns:
        Tuple[str, str]: A tuple containing the first two words that start with the letter 'p'.

    Raises:
        ValueError: If fewer than two words starting with 'p' are found.
    """
    # Initialize a list to hold words that start with 'p'
    p_words = []

    # Iterate through each string in the input list
    for sentence in words:
        # Split the string into individual words
        for word in sentence.split():
            # Check if the word starts with 'p' (case-sensitive)
            if word.startswith('p'):
                p_words.append(word)
                # Stop if we have found two words
                if len(p_words) == 2:
                    return tuple(p_words)

    # If fewer than two words were found, raise a ValueError
    raise ValueError('Not enough words starting with p')
